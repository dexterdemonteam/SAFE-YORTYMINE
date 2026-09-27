#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IDOR Checker (READ-ONLY)
Cek pola ID di URL + referensi link manual.
Tidak melakukan auto-exploit — cuma pattern detection.
"""
import re
from urllib.parse import urlparse

from utils.colors import C, section, label, ok, warn, info, err


# Pattern ID yang umum ditemukan di URL
PATTERNS = {
    "Query ?id=":        r"[?&](?:\w*id)\=(\d+)",
    "Path /123":         r"/(\d+)(?:/|$)",
    "Query ?uid=":       r"[?&](?:uid|user|user_id)\=(\d+)",
    "Query ?pid=":       r"[?&](?:pid|product|product_id|item)\=(\d+)",
    "Query ?oid=":       r"[?&](?:oid|order|order_id)\=(\d+)",
    "UUID":              r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
    "Base64-ish token":  r"[A-Za-z0-9+/=_-]{20,}",
}


def run(prompt_target):
    raw = input(f"  {C.BCYN}[?]{C.RST} URL dengan ID (contoh: /user/123 atau ?id=5) : ").strip()
    if not raw:
        warn("Kosong.")
        return
    if not raw.startswith(("http://", "https://")):
        raw = "https://" + raw

    info(f"Cek pola ID: {C.BCYN}{raw}{C.RST}")
    print()

    u = urlparse(raw)
    hits = []

    section("Pattern Detection")
    full = raw
    for name, pat in PATTERNS.items():
        m = re.search(pat, full)
        if m:
            val = m.group(1) if m.groups() else m.group(0)
            hits.append((name, val))
            label(name, f"{C.BGRN}» {val}{C.RST}")

    if not hits:
        warn("Tidak ada pola ID terdeteksi di URL.")
        return

    # generate candidate ID range untuk manual test
    section("Candidate Range (manual)")
    print(f"  {C.DIM}Untuk verifikasi manual, coba akses ID di sekitar nilai asli.{C.RST}")
    print()

    for name, val in hits:
        if val.isdigit():
            n = int(val)
            candidates = [n - 2, n - 1, n, n + 1, n + 2]
            print(f"  {C.BCYN}{name}{C.RST}  nilai asli: {C.BLD}{n}{C.RST}")
            for c in candidates:
                if c == n:
                    marker = f"{C.DIM}(asli){C.RST}"
                else:
                    marker = f"{C.BYEL}(coba ini!){C.RST}"
                new_url = full.replace(str(n), str(c), 1)
                print(f"    {C.GRN}[{c:>6}]{C.RST}  {new_url}  {marker}")
            print()

    # warning
    section("Catatan Penting")
    print(f"  {C.BYEL}[!]{C.RST} Ini cuma {C.BLD}pattern detection{C.RST} — bukan eksploit.")
    print(f"  {C.BYEL}[!]{C.RST} Verifikasi manual: buka 2 ID, bandingin isinya.")
    print(f"  {C.BYEL}[!]{C.RST} Kalau kamu bisa liat data user lain → IDOR valid.")
    print(f"  {C.BYEL}[!]{C.RST} Test HANYA pada target dengan izin tertulis.")
    print()

    # export
    c = input(f"  {C.BCYN}[?]{C.RST} Simpan list URL ke file? (y/N) : ").strip().lower()
    if c == "y":
        from pathlib import Path
        out = Path(f"idor_report_{int(__import__('time').time())}.txt")
        lines = ["# IDOR Candidate URLs", f"# Base: {raw}", ""]
        for name, val in hits:
            if val.isdigit():
                n = int(val)
                for d in (-2, -1, 0, 1, 2):
                    lines.append(full.replace(str(n), str(n + d), 1))
        out.write_text("\n".join(lines), encoding="utf-8")
        ok(f"Saved → {C.BCYN}{out.name}{C.RST}")

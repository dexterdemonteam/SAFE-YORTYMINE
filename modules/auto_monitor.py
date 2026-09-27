#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auto Monitor — fetch URL berkala, log perubahan response.
"""
import time
import hashlib
from pathlib import Path
from datetime import datetime

from utils.colors import C, section, ok, info, warn, err
from utils.http_client import get


def _hash(text):
    return hashlib.md5(text.encode(errors="ignore")).hexdigest()[:12]


def run(prompt_target):
    url = prompt_target()
    if not url:
        return

    try:
        interval = int(input(f"  {C.BCYN}[?]{C.RST} Interval detik [10] : ").strip() or "10")
        loops = int(input(f"  {C.BCYN}[?]{C.RST} Jumlah loop [5] : ").strip() or "5")
    except Exception:
        interval, loops = 10, 5

    info(f"Monitoring {C.BCYN}{url}{C.RST} "
         f"({loops}x, tiap {interval}s)")

    Path("monitor_log").mkdir(exist_ok=True)
    host = url.split("//")[-1].split("/")[0]
    log = Path(f"monitor_log/{host}_{int(time.time())}.log")

    prev_sig = None
    prev_len = None

    print()
    print(f"  {C.BLD}{C.HI}┌─ MONITOR ──────────────────────────────┐{C.RST}")

    try:
        for i in range(1, loops + 1):
            ts = datetime.now().strftime("%H:%M:%S")
            try:
                r = get(url, timeout=15)
                sig = _hash(r.text)
                blen = len(r.content)
                changed = ""

                if prev_sig and sig != prev_sig:
                    changed = f"  {C.BYEL}[CHANGED]{C.RST}"
                if prev_len is not None and blen != prev_len:
                    diff = blen - prev_len
                    sign = "+" if diff > 0 else ""
                    changed += f"  {C.DIM}(len {sign}{diff}){C.RST}"

                status_color = C.BGRN if r.ok else C.BYEL
                print(f"  {C.DIM}│{C.RST} [{i:>2}/{loops}] {ts} "
                      f"{status_color}{r.status_code}{C.RST}  "
                      f"len={blen:<7} sig={C.DIM}{sig}{C.RST}{changed}")

                # log
                with log.open("a", encoding="utf-8") as f:
                    f.write(f"{ts} | {r.status_code} | len={blen} | sig={sig}\n")

                prev_sig = sig
                prev_len = blen
            except Exception as e:
                print(f"  {C.DIM}│{C.RST} [{i:>2}/{loops}] {ts} "
                      f"{C.BRED}ERR{C.RST}  {C.DIM}{str(e)[:50]}{C.RST}")

            if i < loops:
                time.sleep(interval)
    except KeyboardInterrupt:
        print(f"\n  {C.BYEL}[!]{C.RST} Monitoring dihentikan.")

    print(f"  {C.BLD}{C.HI}└────────────────────────────────────────┘{C.RST}")
    print()
    ok(f"Log tersimpan → {C.BCYN}{log}{C.RST}")

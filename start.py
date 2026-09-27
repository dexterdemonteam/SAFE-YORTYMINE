#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SAFE-YORTYMINE v1.0.0
Web Reconnaissance & Security Audit Toolkit
by Dexter Demon Team
"""

import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from utils.colors import C, info, warn, err, ok
from modules import banner as banner_mod
from modules import recon
from modules import fetch
from modules import headers
from modules import dns_lookup
from modules import whois_lookup
from modules import port_scan
from modules import dir_scan
from modules import ssl_info
from modules import subdomain
from modules import tech_detect
from modules import robots_sitemap
from modules import auto_monitor
from modules import idor_checker
from modules import payload_ref

from auth import prompt_login

MODE = "user"
W = 58


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    print()
    input(f"  {C.DIM}ENTER untuk kembali...{C.RST}")


def prompt_target():
    t = input(f"  {C.BCYN}[?]{C.RST} Target URL (https://example.com) : ").strip()
    if not t:
        warn("Target kosong.")
        return None
    if not t.startswith(("http://", "https://")):
        t = "https://" + t
    return t


# ==========================================================
#  Box helpers
# ==========================================================
def _strip_ansi(s):
    import re
    return re.sub(r"\033\[[0-9;]*m", "", s)


def _row(col):
    plain = _strip_ansi(col)
    pad = W - len(plain) - 2
    if pad < 0:
        pad = 0
    print(f"  {C.BCYN}|{C.RST} {col}{' ' * pad} {C.BCYN}|{C.RST}")


def _top():
    print(f"  {C.BCYN}+{'-' * W}+{C.RST}")


def _bot():
    print(f"  {C.BCYN}+{'-' * W}+{C.RST}")


def _section(title, items):
    print()
    print(f"  {C.BCYN}+--- {C.BLD}{C.HI}{title:<10}{C.RST}"
          f"{C.BCYN}{'-' * (W - len(title) - 6)}+{C.RST}")
    for num, name, desc in items:
        _row(f"{C.BCYN}[{num:>2}]{C.RST}  "
             f"{C.BLD}{C.HI}{name:<22}{C.RST}  "
             f"{C.DIM}{desc}{C.RST}")
    print(f"  {C.BCYN}+{'-' * W}+{C.RST}")


def menu():
    clear()
    banner_mod.print_banner()
    _top()
    _row(f"{C.BLD}{C.HI}SAFE-YORTYMINE  v1.0.0  -  by Dexter Demon Team{C.RST}")
    _row(f"{C.BGRN}[+]{C.RST} Status: {C.BLD}{C.BCYN}GUEST{C.RST}"
         f"  |  {C.BGRN}All features available{C.RST}")
    _bot()

    _section("RECON", [
        ("1",  "Full Recon",       "IP, headers, SSL"),
        ("2",  "Fetch Source",     "grab HTML page"),
        ("3",  "HTTP Headers",     "response headers"),
        ("4",  "DNS Lookup",       "A/MX/NS/TXT records"),
        ("5",  "WHOIS Lookup",     "domain info"),
    ])

    _section("SCAN", [
        ("6",  "Port Scan",        "top 18 common ports"),
        ("7",  "Directory Scan",   "public wordlist"),
        ("8",  "Subdomain Enum",   "OSINT subdomains"),
        ("9",  "SSL / TLS Info",   "cert & cipher"),
        ("10", "Tech Detect",      "CMS / framework"),
    ])

    _section("UTILITY", [
        ("11", "Robots & Sitemap", "public files"),
        ("12", "Auto Monitor",     "real-time fetch"),
        ("13", "IDOR Checker",     "pattern only"),
        ("14", "Payload Reference","educational library"),
    ])

    print()
    _top()
    _row(f"{C.BRED}[00]{C.RST}  {C.BLD}{C.HI}Exit{C.RST}")
    _bot()
    print()


def main():
    global MODE
    clear()
    banner_mod.print_banner()
    print(f"  {C.DIM}v1.0.0  -  by Dexter Demon Team{C.RST}")

    MODE = prompt_login()
    time.sleep(0.8)

    actions = {
        "1":  ("Full Recon",        recon.run),
        "2":  ("Fetch Source",      fetch.run),
        "3":  ("HTTP Headers",      headers.run),
        "4":  ("DNS Lookup",        dns_lookup.run),
        "5":  ("WHOIS Lookup",      whois_lookup.run),
        "6":  ("Port Scan",         port_scan.run),
        "7":  ("Directory Scan",    dir_scan.run),
        "8":  ("Subdomain Enum",    subdomain.run),
        "9":  ("SSL / TLS Info",    ssl_info.run),
        "10": ("Tech Detect",       tech_detect.run),
        "11": ("Robots & Sitemap",  robots_sitemap.run),
        "12": ("Auto Monitor",      auto_monitor.run),
        "13": ("IDOR Checker",      idor_checker.run),
        "14": ("Payload Reference", payload_ref.run),
    }

    # fitur yang gak butuh target URL
    no_target = {"13", "14"}

    while True:
        menu()
        choice = input(f"  {C.BCYN}safe-yortymine>{C.RST} ").strip()

        if choice in ("0", "00"):
            print()
            ok("Stay stealth. 🕶️")
            print()
            sys.exit(0)

        if choice not in actions:
            err("Pilihan tidak valid.")
            time.sleep(1)
            continue

        name, fn = actions[choice]
        clear()
        banner_mod.print_mini()
        print(f"  {C.BLD}{C.HI}» {name}{C.RST}")
        print()

        try:
            if choice in no_target:
                fn(prompt_target)
            else:
                fn(prompt_target)
        except KeyboardInterrupt:
            print()
            warn("Dibatalkan.")
        except Exception as e:
            err(f"Error: {e}")

        pause()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        warn("Keluar.")
        sys.exit(0)

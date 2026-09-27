#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SAFE-YORTYMINE — Auth
Password optional. Mode user = akses penuh (kecuali ai_dump yang gak ada).
"""
from utils.colors import C


def prompt_login() -> str:
    print()
    print(f"  {C.BCYN}╔══════════════════════════════════════════╗{C.RST}")
    print(f"  {C.BCYN}║{C.RST}      SAFE-YORTYMINE  ACCESS           {C.BCYN}║{C.RST}")
    print(f"  {C.BCYN}╚══════════════════════════════════════════╝{C.RST}")
    print()
    print(f"  {C.GRY}[i]{C.RST} Enter password (kosong = guest).")
    print(f"  {C.GRY}[i]{C.RST} Public build — semua fitur kecuali AI Dump.")
    print()

    try:
        pw = input(f"  {C.BCYN}┌─ Password :{C.RST} ").strip()
    except (EOFError, KeyboardInterrupt):
        print()
        return "user"

    if pw == "dexter-demon":
        print(f"\n  {C.BGRN}[+]{C.RST} Owner mode active.")
        return "owner"

    print(f"\n  {C.BCYN}[*]{C.RST} Guest mode.")
    return "user"

import os
from urllib.parse import urlparse

from utils.colors import C, section, label, ok, err, info
from utils.http_client import get

OUTPUT_DIR = "safe_fetch_dump"


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    info(f"Fetching: {C.BCYN}{url}{C.RST}")
    try:
        r = get(url, timeout=15)
    except Exception as e:
        err(f"Fetch gagal: {e}")
        return

    section("Response")
    label("Status", f"{r.status_code} {r.reason}")
    label("Length", f"{len(r.content)} bytes")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    host = urlparse(url).hostname or "target"
    fname = os.path.join(OUTPUT_DIR, f"{host}_index.html")
    with open(fname, "w", encoding="utf-8", errors="ignore") as f:
        f.write(r.text)
    ok(f"Saved → {C.BCYN}{fname}{C.RST}")

    section("Preview (first 25 lines)")
    for ln in r.text.splitlines()[:25]:
        print(f"  {C.DIM}{ln[:140]}{C.RST}")

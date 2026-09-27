from utils.colors import C, section, info, err
from utils.http_client import get


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    info(f"Fetching headers dari {C.BCYN}{url}{C.RST}")
    try:
        r = get(url, timeout=12)
    except Exception as e:
        err(f"Gagal: {e}")
        return
    section(f"HTTP Response Headers ({r.status_code})")
    for k, v in r.headers.items():
        print(f"  {C.BCYN}{k}{C.RST}: {v}")
    print(f"\n  {C.DIM}Total: {len(r.headers)} header{C.RST}")

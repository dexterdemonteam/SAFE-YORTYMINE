from urllib.parse import urljoin
from utils.colors import C, section, ok, info, warn
from utils.http_client import get

FILES = ["robots.txt", "sitemap.xml", "sitemap_index.xml",
         ".well-known/security.txt"]


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    if not url.endswith("/"):
        url += "/"
    info(f"Robots & Sitemap: {C.BCYN}{url}{C.RST}")

    for f in FILES:
        target = urljoin(url, f)
        section(f)
        try:
            r = get(target, timeout=8)
            if r.status_code == 200 and r.text.strip():
                ok(f"FOUND ({len(r.content)} bytes)")
                for ln in r.text.splitlines()[:40]:
                    print(f"  {C.DIM}{ln[:140]}{C.RST}")
            else:
                warn(f"Not found (status {r.status_code})")
        except Exception as e:
            warn(f"Error: {e}")

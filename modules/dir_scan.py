import concurrent.futures
from urllib.parse import urljoin
from utils.colors import C, section, ok, info, err
from utils.http_client import get

WORDLIST = [
    "admin", "login", "dashboard", "wp-admin", "wp-login.php",
    "backup", "config", "test", "api", "api/v1", "uploads",
    "files", "assets", "static", "js", "css", "images", "docs",
    "robots.txt", "sitemap.xml", "phpinfo.php", "info.php",
    "server-status", "cpanel", "webmail", "phpmyadmin",
]


def _check(base, path):
    url = urljoin(base, path)
    try:
        r = get(url, timeout=6, allow_redirects=False)
        return path, r.status_code, len(r.content)
    except Exception:
        return path, None, 0


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    if not url.endswith("/"):
        url += "/"
    info(f"Directory Scan: {C.BCYN}{url}{C.RST}  ({len(WORDLIST)} path)")

    found = []
    section("Scanning")
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as ex:
        futures = [ex.submit(_check, url, p) for p in WORDLIST]
        for fut in concurrent.futures.as_completed(futures):
            path, status, size = fut.result()
            if status is None:
                continue
            if status in (200, 201, 204, 301, 302, 307, 401, 403):
                color = C.BGRN if status == 200 else C.BYEL if status in (301, 302) else C.BRED
                print(f"  {color}[{status}]{C.RST} {path}  {C.DIM}({size}b){C.RST}")
                found.append((path, status, size))
            else:
                print(f"  {C.GRY}[{status}]{C.RST} {C.DIM}{path}{C.RST}")

    section("Result")
    if found:
        ok(f"{len(found)} endpoint menarik.")
    else:
        err("Tidak ada endpoint menarik.")

import concurrent.futures
import socket
from urllib.parse import urlparse
from utils.colors import C, section, ok, info

COMMON_SUBS = [
    "www", "mail", "ftp", "webmail", "smtp", "pop", "ns1", "ns2",
    "dev", "test", "staging", "beta", "api", "app", "apps",
    "admin", "portal", "vpn", "cdn", "static", "assets", "media",
    "img", "docs", "blog", "shop", "store", "secure", "cpanel",
    "git", "jenkins", "monitor", "status", "dashboard", "db",
]


def _resolve(sub, domain):
    full = f"{sub}.{domain}"
    try:
        return full, socket.gethostbyname(full)
    except Exception:
        return full, None


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    domain = urlparse(url).hostname
    if domain.startswith("www."):
        domain = domain[4:]
    info(f"Subdomain Enum: {C.BCYN}*.{domain}{C.RST}  ({len(COMMON_SUBS)} kandidat)")

    found = []
    section("Scanning")
    with concurrent.futures.ThreadPoolExecutor(max_workers=25) as ex:
        futures = [ex.submit(_resolve, s, domain) for s in COMMON_SUBS]
        for fut in concurrent.futures.as_completed(futures):
            full, ip = fut.result()
            if ip:
                print(f"  {C.BGRN}[FOUND]{C.RST} {full:<35} {C.DIM}→ {ip}{C.RST}")
                found.append((full, ip))
            else:
                print(f"  {C.GRY}[----]{C.RST}  {C.DIM}{full}{C.RST}")

    section("Result")
    if found:
        ok(f"{len(found)} subdomain aktif.")
    else:
        info("Tidak ada subdomain dari wordlist aktif.")

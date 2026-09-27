import socket
import ssl
from urllib.parse import urlparse

from utils.colors import C, section, label, ok, warn, err, info
from utils.http_client import get

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "X-XSS-Protection",
]


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    host = urlparse(url).hostname
    info(f"Target: {C.BCYN}{url}{C.RST}")

    section("IP Address")
    try:
        label("IPv4", socket.gethostbyname(host), C.BGRN)
    except Exception as e:
        err(f"Resolve gagal: {e}")

    section("Server Response")
    try:
        r = get(url, timeout=12)
        label("Status", f"{r.status_code} {r.reason}",
              C.BGRN if r.ok else C.BYEL)
        label("Server", r.headers.get("Server", "-"))
        label("Content-Type", r.headers.get("Content-Type", "-"))
    except Exception as e:
        err(f"Request gagal: {e}")
        return

    section("Security Headers")
    missing = 0
    for h in SECURITY_HEADERS:
        v = r.headers.get(h)
        if v:
            label(h, "✓ " + v[:60], C.BGRN)
        else:
            label(h, "✗ MISSING", C.BRED)
            missing += 1
    if missing:
        warn(f"{missing} header keamanan hilang.")

    section("SSL Certificate")
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with socket.create_connection((host, 443), timeout=8) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                label("Issuer", str(cert.get("issuer", "-"))[:80])
                label("Valid Until", cert.get("notAfter", "-"))
                label("TLS", ssock.version())
    except Exception as e:
        warn(f"SSL info tidak tersedia: {e}")

    print()
    ok("Recon selesai.")

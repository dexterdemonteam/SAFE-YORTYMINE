import socket
import ssl
from urllib.parse import urlparse
from utils.colors import C, section, label, info, err


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    host = urlparse(url).hostname
    info(f"SSL/TLS: {C.BCYN}{host}:443{C.RST}")
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        with socket.create_connection((host, 443), timeout=8) as sock:
            with ctx.wrap_socket(sock, server_hostname=host) as ssock:
                cert = ssock.getpeercert()
                cipher = ssock.cipher()
                section("Connection")
                label("TLS Version", ssock.version(), C.BGRN)
                label("Cipher", cipher[0] if cipher else "-")
                section("Certificate")
                label("Subject", str(cert.get("subject", "-"))[:80])
                label("Issuer", str(cert.get("issuer", "-"))[:80])
                label("Valid From", cert.get("notBefore", "-"))
                label("Valid Until", cert.get("notAfter", "-"))
                section("Subject Alt Names")
                for typ, val in cert.get("subjectAltName", []):
                    print(f"  {C.GRN}»{C.RST} {typ}: {val}")
    except Exception as e:
        err(f"SSL check gagal: {e}")

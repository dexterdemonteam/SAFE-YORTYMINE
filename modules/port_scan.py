import socket
import concurrent.futures
from urllib.parse import urlparse

from utils.colors import C, section, ok, info, err

TOP_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
    80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 445: "SMB",
    3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL", 6379: "Redis",
    8080: "HTTP-Alt", 8443: "HTTPS-Alt", 27017: "MongoDB",
}


def _scan(host, port, timeout=1.5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return port, True
    except Exception:
        return port, False


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    host = urlparse(url).hostname
    info(f"Port Scan: {C.BCYN}{host}{C.RST}  ({len(TOP_PORTS)} port)")

    open_ports = []
    section("Scanning")
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as ex:
        futures = [ex.submit(_scan, host, p) for p in TOP_PORTS]
        for fut in concurrent.futures.as_completed(futures):
            port, is_open = fut.result()
            if is_open:
                open_ports.append(port)
                print(f"  {C.BGRN}[OPEN]{C.RST} {port:<6} {C.DIM}{TOP_PORTS[port]}{C.RST}")
            else:
                print(f"  {C.GRY}[----]{C.RST} {port:<6} {C.DIM}{TOP_PORTS[port]}{C.RST}")

    section("Result")
    if open_ports:
        ok(f"{len(open_ports)} port terbuka: {open_ports}")
    else:
        err("Tidak ada port terbuka.")

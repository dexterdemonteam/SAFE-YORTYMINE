from urllib.parse import urlparse
import dns.resolver
from utils.colors import C, section, info

RECORD_TYPES = ["A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA"]


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    host = urlparse(url).hostname
    info(f"DNS Lookup: {C.BCYN}{host}{C.RST}")

    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    resolver.lifetime = 5

    for rtype in RECORD_TYPES:
        section(f"Record {rtype}")
        try:
            for a in resolver.resolve(host, rtype):
                print(f"  {C.GRN}»{C.RST} {a.to_text()}")
        except Exception as e:
            print(f"  {C.DIM}(tidak ada: {e}){C.RST}")

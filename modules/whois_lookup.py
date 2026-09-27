from urllib.parse import urlparse
import whois
from utils.colors import C, section, label, info, err


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    host = urlparse(url).hostname
    info(f"WHOIS Lookup: {C.BCYN}{host}{C.RST}")
    try:
        w = whois.whois(host)
    except Exception as e:
        err(f"WHOIS gagal: {e}")
        return
    section("Domain Info")
    for f in ["domain_name", "registrar", "creation_date",
              "expiration_date", "updated_date", "name_servers",
              "emails", "org", "country", "status"]:
        v = w.get(f) if isinstance(w, dict) else getattr(w, f, None)
        if v:
            label(f, str(v)[:120])

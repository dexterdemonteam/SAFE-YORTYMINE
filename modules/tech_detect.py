import re
from utils.colors import C, section, label, info, err
from utils.http_client import get

SIGNATURES = {
    "WordPress":  [r"wp-content", r"wp-includes", r"/wp-json"],
    "Joomla":     [r"/components/com_", r"joomla"],
    "Drupal":     [r"Drupal\.settings", r"/sites/default/files"],
    "Shopify":    [r"cdn\.shopify\.com"],
    "React":      [r"__REACT_DEVTOOLS", r"react-dom"],
    "Vue.js":     [r"vue\.js", r"__vue__"],
    "Next.js":    [r"__NEXT_DATA__", r"/_next/"],
    "jQuery":     [r"jquery(?:-|\.)min\.js"],
    "Bootstrap":  [r"bootstrap(?:\.min)?\.css"],
    "Cloudflare": [r"cloudflare"],
    "PHP":        [r"\.php"],
}


def run(prompt_target):
    url = prompt_target()
    if not url:
        return
    info(f"Tech Detect: {C.BCYN}{url}{C.RST}")
    try:
        r = get(url, timeout=12)
    except Exception as e:
        err(f"Gagal: {e}")
        return

    body = r.text
    blob = (body + "\n" + str(r.headers)).lower()

    section("Server")
    label("Server", r.headers.get("Server", "-"))
    label("X-Powered-By", r.headers.get("X-Powered-By", "-"))

    section("Detected Technologies")
    detected = []
    for name, pats in SIGNATURES.items():
        for p in pats:
            if re.search(p, blob, re.I):
                detected.append(name)
                break

    if detected:
        for d in detected:
            print(f"  {C.BGRN}[+]{C.RST} {d}")
    else:
        print(f"  {C.DIM}(tidak ada signature){C.RST}")

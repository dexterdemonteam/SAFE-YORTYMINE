
<div align="center">

```

███████╗ █████╗ ███████╗███████╗    ██╗   ██╗ ██████╗ ██████╗ ████████╗██╗   ██╗███╗   ███╗██╗███╗   ██╗███████╗
██╔════╝██╔══██╗██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██╔══██╗╚══██╔══╝╚██╗ ██╔╝████╗ ████║██║████╗  ██║██╔════╝
███████╗███████║█████╗  █████╗       ╚████╔╝ ██║   ██║██████╔╝   ██║    ╚████╔╝ ██╔████╔██║██║██╔██╗ ██║█████╗
╚════██║██╔══██║██╔══╝  ██╔══╝        ╚██╔╝  ██║   ██║██╔══██╗   ██║     ╚██╔╝  ██║╚██╔╝██║██║██║╚██╗██║██╔══╝
███████║██║  ██║██║     ███████╗       ██║   ╚██████╔╝██║  ██║   ██║      ██║   ██║ ╚═╝ ██║██║██║ ╚████║███████╗
╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝       ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝

```

### Web Reconnaissance & Security Audit Toolkit

**v1.0.0 · by Dexter Demon Team**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](./LICENSE)
[![Copyright](https://img.shields.io/badge/©%202024-Dexter%20Demon%20Team-black?style=for-the-badge)]()
[![Copyright](https://img.shields.io/badge/©%202024-Dexter%20Demon%20Team-black?style=for-the-badge)]()
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Termux-orange?style=for-the-badge)](https://termux.dev)
[![Status](https://img.shields.io/badge/Status-Educational-red?style=for-the-badge)]()
[![Made with](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red?style=for-the-badge)]()

</div>

---

## 🎯 Tentang SAFE-YORTYMINE

**SAFE-YORTYMINE** adalah toolkit CLI untuk **passive reconnaissance** dan **audit keamanan web**. Dirancang untuk:

- 🔍 **Security Researcher** yang butuh tool recon cepat
- 🐛 **Bug Bounty Hunter** untuk fase information gathering
- 🎓 **Pemula** yang mau belajar web security
- 🏢 **Tim Internal** yang audit aset sendiri

> ⚠️ **Tool ini adalah versi PUBLIC/SAFE** — tidak mengandung auto-exploit, auto-inject, atau auto-dump database. Fitur serangan aktif sengaja dihilangkan demi keamanan publik.

---

## ✨ Fitur Lengkap

<table>
<tr>
<td width="50%">

### 🔍 RECON
| # | Fitur | Deskripsi |
|---|-------|-----------|
| 1 | Full Recon | IP, server, security headers, SSL |
| 2 | Fetch Source | Grab HTML page |
| 3 | HTTP Headers | Analisis response header |
| 4 | DNS Lookup | A / AAAA / MX / NS / TXT / CNAME / SOA |
| 5 | WHOIS Lookup | Domain & registrar info |

</td>
<td width="50%">

### 📡 SCAN
| # | Fitur | Deskripsi |
|---|-------|-----------|
| 6 | Port Scan | Top 18 port umum |
| 7 | Directory Scan | Wordlist publik |
| 8 | Subdomain Enum | OSINT subdomain |
| 9 | SSL / TLS Info | Cert, cipher, SAN |
| 10 | Tech Detect | CMS / framework fingerprint |

</td>
</tr>
<tr>
<td width="50%">

### 🛠️ UTILITY
| # | Fitur | Deskripsi |
|---|-------|-----------|
| 11 | Robots & Sitemap | File publik |
| 12 | Auto Monitor | Real-time fetch + diff |
| 13 | IDOR Checker | Pattern detection (read-only) |

</td>
<td width="50%">

### 📚 LIBRARY
| # | Fitur | Deskripsi |
|---|-------|-----------|
| 14 | Payload Reference | Educational payload library |

Cakupan:
- SQLi (UNION / ORDER BY / Boolean / Time / WAF Bypass)
- NoSQL Injection
- Path Traversal
- SSTI
- SSRF
- Command Injection
- XXE
- JWT Attacks

</td>
</tr>
</table>

---

## 🖥️ Preview Tampilan

### Menu Utama

```

[ASCII Demon Banner]

+----------------------------------------------------------+

| SAFE-YORTYMINE  v1.0.0  -  by Dexter Demon Team          |

| [+] Status: GUEST  |  All features available             |
+----------------------------------------------------------+

+--- RECON ------------------------------------------------+

| [ 1]  Full Recon           IP, headers, SSL              |

| [ 2]  Fetch Source         grab HTML page                |

| [ 3]  HTTP Headers         response headers              |

| [ 4]  DNS Lookup           A/MX/NS/TXT records           |

| [ 5]  WHOIS Lookup         domain info                   |
+----------------------------------------------------------+

+--- SCAN -------------------------------------------------+

| [ 6]  Port Scan            top 18 common ports           |

| [ 7]  Directory Scan       public wordlist               |

| [ 8]  Subdomain Enum       OSINT subdomains              |

| [ 9]  SSL / TLS Info       cert & cipher                 |

| [10]  Tech Detect          CMS / framework               |
+----------------------------------------------------------+

+--- UTILITY ----------------------------------------------+

| [11]  Robots & Sitemap     public files                  |

| [12]  Auto Monitor         real-time fetch               |

| [13]  IDOR Checker         pattern only                  |

| [14]  Payload Reference    educational library           |
+----------------------------------------------------------+

+----------------------------------------------------------+

| [00]  Exit                                               |
+----------------------------------------------------------+

```

### Contoh Output — Full Recon

```

▎Target
Input                  https://example.com
IPv4                   93.184.216.34

▎Server Response
Status                 200 OK
Server                 ECS (dcb/7F84)
Content-Type           text/html; charset=UTF-8

▎Security Headers
Strict-Transport-Security    ✓ max-age=31536000
Content-Security-Policy      ✗ MISSING
X-Frame-Options              ✗ MISSING
X-Content-Type-Options       ✓ nosniff
Referrer-Policy              ✗ MISSING
Permissions-Policy           ✗ MISSING
X-XSS-Protection             ✗ MISSING

[!] 5 header keamanan hilang.

▎SSL Certificate
Issuer                 DigiCert Inc
Valid Until            Mar 15 12:00:00 2027 GMT
TLS                    1.3

[+] Recon selesai.

```

### Contoh Output — Auto Monitor

```

[*] Monitoring https://example.com (5x, tiap 10s)

┌─ MONITOR ──────────────────────────────┐
│ [ 1/5] 14:23:01  200  len=1256   sig=a8f3c2e1b9d0
│ [ 2/5] 14:23:11  200  len=1256   sig=a8f3c2e1b9d0
│ [ 3/5] 14:23:21  200  len=1289   sig=b7e1d4a8c3f2  [CHANGED]  (len +33)
│ [ 4/5] 14:23:31  200  len=1289   sig=b7e1d4a8c3f2
│ [ 5/5] 14:23:41  200  len=1256   sig=a8f3c2e1b9d0  [CHANGED]  (len -33)
└────────────────────────────────────────┘

[+] Log tersimpan → monitor_log/example.com_1736789012.log

```

---

## 📦 Instalasi

### 🔧 Prasyarat

| Requirement | Versi |
|-------------|-------|
| Python | 3.8+ |
| pip | latest |
| OS | Linux / macOS / Termux / WSL |

### 📥 Cara Install

**1. Clone repository**

```bash
git clone https://github.com/USERNAME/SAFE-YORTYMINE.git
cd SAFE-YORTYMINE
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

Kalau pakai Termux / Debian baru dan kena error externally-managed-environment:

```bash
pip install --break-system-packages -r requirements.txt
```

Atau pakai virtualenv (recommended):

```bash
python3 -m venv venv
source venv/bin/activate    # Linux/macOS/Termux
# venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Jalankan

```bash
python start.py
```

---

🚀 Cara Pakai

1️⃣ Login

Saat pertama kali jalan, kamu akan diminta password. Untuk versi publik:

· Guest mode → langsung Enter (akses semua fitur public)
· Owner mode → password khusus (kalau punya)

2️⃣ Pilih Fitur

Dari menu utama, ketik nomor fitur (1-14) → Enter.

3️⃣ Masukkan Target

```
[?] Target URL (https://example.com) :
```

Contoh input yang valid:

Input Hasil
example.com auto jadi https://example.com
https://example.com dipakai langsung
http://testphp.vulnweb.com HTTP (bukan HTTPS)

4️⃣ Lihat Hasil

Output muncul dengan warna & struktur rapi. Tekan Enter untuk kembali ke menu.

---

📂 Struktur Project

```
SAFE-YORTYMINE/
├── README.md                    ← Dokumentasi ini
├── LEGAL.md                     ← Legal notice
├── requirements.txt             ← Dependencies
├── .gitignore                   ← Git ignore rules
├── start.py                     ← Main entry point
├── auth.py                      ← Login handler
│
├── modules/                     ← Fitur modules
│   ├── __init__.py
│   ├── banner.py                ← ASCII banner
│   ├── recon.py                 ← [1] Full Recon
│   ├── fetch.py                 ← [2] Fetch Source
│   ├── headers.py               ← [3] HTTP Headers
│   ├── dns_lookup.py            ← [4] DNS Lookup
│   ├── whois_lookup.py          ← [5] WHOIS
│   ├── port_scan.py             ← [6] Port Scan
│   ├── dir_scan.py              ← [7] Directory Scan
│   ├── ssl_info.py              ← [8] SSL Info
│   ├── subdomain.py             ← [9] Subdomain Enum
│   ├── tech_detect.py           ← [10] Tech Detect
│   ├── robots_sitemap.py        ← [11] Robots
│   ├── auto_monitor.py          ← [12] Auto Monitor
│   ├── idor_checker.py          ← [13] IDOR Checker
│   └── payload_ref.py           ← [14] Payload Reference
│
└── utils/                       ← Utility modules
    ├── __init__.py
    ├── colors.py                ← Terminal colors
    └── http_client.py           ← HTTP helper
```

---

⚖️ Legal Notice

<div align="center">

🚨 BACA SEBELUM PAKAI 🚨

Tool ini hanya untuk tujuan EDUKASI dan AUDIT KEAMANAN yang SAH.

</div>

✅ Legal Use

Boleh dipakai untuk:

· 🏠 Aset sendiri — server, aplikasi, domain yang kamu miliki
· 🐛 Bug bounty program — sesuai scope & policy yang berlaku
· 🎓 Lab / CTF — target yang sengaja dibuat rentan
· 📝 Kontrak pentest — dengan izin tertulis dari pemilik aset

❌ Dilarang Keras

· ❌ Scan / serang situs orang lain tanpa izin
· ❌ DDoS, spam, atau flooding
· ❌ Pencurian data pribadi
· ❌ Stalking, doxing, harassment
· ❌ Aktivitas ilegal lainnya

🌏 Pasal-Pasal Hukum

<details>
<summary><b>🇮🇩 Indonesia</b></summary>

Pasal Isi Ancaman
UU ITE No. 11/2008 Pasal 30 Akses komputer/ sistem elektronik tanpa izin 6-8 tahun + denda Rp 600-800 juta
UU ITE Pasal 32 Transfer informasi tanpa izin 8-10 tahun + denda Rp 2-5 miliar
UU ITE Pasal 33 Gangguan sistem elektronik (DDoS) 10 tahun + denda Rp 10 miliar
UU ITE Pasal 35 Manipulasi data elektronik 12 tahun + denda Rp 12 miliar
UU PDP No. 27/2022 Pasal 65 Pengumpulan data pribadi ilegal 5 tahun + denda Rp 5 miliar
UU PDP Pasal 67 Pengungkapan data pribadi 5 tahun + denda Rp 5 miliar
KUHP Pasal 362 Pencurian data 5 tahun + denda
KUHP Pasal 406 Perusakan 2 tahun 8 bulan

</details>

<details>
<summary><b>🇺🇸 United States</b></summary>

Pasal Isi Ancaman
CFAA 18 U.S.C. § 1030 Unauthorized computer access 5-20 tahun federal prison
DMCA § 1201 Circumvention of protections 5 tahun + $500,000
Wire Fraud 18 U.S.C. § 1343 Fraud via electronic communication 20 tahun + $250,000
Stored Communications Act Unauthorized access to stored data 5 tahun
State Laws Bervariasi per negara bagian Bervariasi

</details>

<details>
<summary><b>🇬🇧 United Kingdom</b></summary>

Pasal Isi Ancaman
Computer Misuse Act 1990 § 1 Unauthorized access 2 tahun + unlimited fine
CMA § 2 Unauthorized access with intent 5 tahun
CMA § 3 Unauthorized modification 10 tahun
CMA § 3ZA Impairment of computer 14 tahun
Data Protection Act 2018 Data privacy violation Unlimited fine
GDPR Art. 83 Data protection breach €20 million / 4% revenue

</details>

<details>
<summary><b>🇩🇪 Germany</b></summary>

Pasal Isi Ancaman
StGB § 202a Data espionage 3 tahun
StGB § 202b Interception of data 2 tahun
StGB § 202c Preparing data espionage 1 tahun
StGB § 303a Data modification 2 tahun
StGB § 303b Computer sabotage 5 tahun
BDSG (GDPR) Privacy violation €20 million

</details>

<details>
<summary><b>🇦🇺 Australia</b></summary>

Pasal Isi Ancaman
Criminal Code Act 1995 § 477.1 Unauthorized access 2 tahun
§ 477.2 Unauthorized modification 10 tahun
§ 477.3 Unauthorized impairment 10 tahun
§ 478.1 Unauthorized access to data 2 tahun
Privacy Act 1988 Privacy violation AUD 50 million

</details>

<details>
<summary><b>🇸🇬 Singapore</b></summary>

Pasal Isi Ancaman
Computer Misuse Act § 3 Unauthorized access SGD 5,000 + 2 tahun
CMA § 4 Access with intent SGD 50,000 + 10 tahun
CMA § 5 Unauthorized modification SGD 10,000 + 3 tahun
CMA § 7 Unauthorized use of computer SGD 50,000 + 7 tahun
PDPA Data privacy violation SGD 1 million

</details>

<details>
<summary><b>🇯🇵 Japan</b></summary>

Pasal Isi Ancaman
刑法 第168条の2 Unauthorized access 3 tahun + ¥1 juta
刑法 第168条の3 Access with intent 5 tahun + ¥1 juta
不正アクセス禁止法 § 3 Unauthorized access 1 tahun + ¥1 juta
個人情報保護法 Data privacy violation ¥100 juta

</details>

<details>
<summary><b>🇲🇾 Malaysia</b></summary>

Pasal Isi Ancaman
Computer Crimes Act 1997 § 3 Unauthorized access RM 50,000 + 5 tahun
CCA § 4 Access with intent RM 150,000 + 10 tahun
CCA § 5 Unauthorized modification RM 100,000 + 7 tahun
PDPA 2010 Data privacy violation RM 500,000 + 3 tahun

</details>

📜 Disclaimer

```
Dexter Demon Team tidak bertanggung jawab atas penyalahgunaan tool ini.
Dengan mengunduh, menginstall, atau menggunakan tool ini, kamu setuju:

1. Bertanggung jawab penuh atas semua aksimu
2. Mematuhi semua hukum yang berlaku di negaramu
3. Menggunakan hanya untuk tujuan yang sah & legal
4. Tidak menyalahgunakan untuk aktivitas kriminal
5. Menerima bahwa author tidak bertanggung jawab atas konsekuensi apapun

Kalau tidak setuju → JANGAN PAKAI TOOL INI.
```

---

🧪 Target Latihan Legal

Buat latihan, gunakan target yang sengaja dibuat rentan:

Target URL Scope
🎯 Acunetix Demo testphp.vulnweb.com Legal, sengaja rentan
🎯 IBM Demo demo.testfire.net Legal, sengaja rentan
🎯 OWASP Juice Shop juice-shop.herokuapp.com Legal, sengaja rentan
🎯 DVWA self-host Bikin sendiri
🎯 HackTheBox hackthebox.com Paid, legal
🎯 TryHackMe tryhackme.com Free & paid, legal

JANGAN pakai situs random — itu ilegal!

---

❓ FAQ

<details>
<summary><b>Q: Kenapa tool ini gak ada auto-exploit?</b></summary>

A: Ini versi PUBLIC/SAFE. Fitur serangan aktif sengaja dihilangkan supaya:

· Aman diupload ke GitHub
· Gak disalahgunakan
· Tetap fokus ke edukasi & recon

</details>

<details>
<summary><b>Q: Beda dengan versi privat?</b></summary>

A: Versi privat punya fitur tambahan:

· Auto SQLi injection
· Auto database dump
· AI reasoning engine
· Multi-dataset payload

Gak akan di-release ke publik.

</details>

<details>
<summary><b>Q: Kenapa scan saya lambat?</b></summary>

A: Cek:

1. Koneksi internet
2. Target server (mungkin lambat / block)
3. Firewall lokal
4. Coba naikin timeout di kode

</details>

<details>
<summary><b>Q: Error "ModuleNotFoundError"?</b></summary>

A: Install dependencies:

```bash
pip install -r requirements.txt
```

Kalau kena externally-managed-environment:

```bash
pip install --break-system-packages -r requirements.txt
```

</details>

<details>
<summary><b>Q: Bisa dipakai di Windows?</b></summary>

A: Bisa, tapi rekomendasi Linux/macOS/Termux. Windows pakai WSL atau Git Bash buat tampilan warna.

</details>

<details>
<summary><b>Q: Bisa buat scan situs orang?</b></summary>

A: TIDAK. Itu ilegal. Cek Legal Notice di atas.

</details>

---

🤝 Kontribusi

Pull request welcome. Tapi ikutin rules:

· ✅ Fitur passive atau defensive aja
· ✅ Ada dokumentasi jelas
· ✅ Gak ada auto-exploit
· ✅ Test dulu sebelum submit

---

📝 Changelog

v1.0.0 — Current

· ✨ Initial public release
· 🎯 14 fitur (recon, scan, utility, library)
· 🎨 Colored CLI dengan box drawing
· 📚 Payload reference library
· 📡 Auto monitor real-time
· 🔒 Safe for public release

---

📄 Lisensi

MIT License

```
Copyright (c) 2026 Dexter Demon Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

👤 Author

<div align="center">

Dexter Demon Team

🌐 GitHub: @USERNAME
📧 Email: dexter-demon@example.com

---

Made with ❤️ for the security community

⭐ Kalau tool ini berguna, kasih star di GitHub!

https://img.shields.io/github/stars/USERNAME/SAFE-YORTYMINE?style=social
https://img.shields.io/github/forks/USERNAME/SAFE-YORTYMINE?style=social

---

⚠️ Remember: With great power comes great responsibility.

Use ethically. Hack ethically. Stay legal.

```
  ██████╗ ███████╗██╗  ██╗████████╗███████╗██████╗ 
  ██╔══██╗██╔════╝╚██╗██╔╝╚══██╔══╝██╔════╝██╔══██╗
  ██║  ██║█████╗   ╚███╔╝    ██║   █████╗  ██████╔╝
  ██║  ██║██╔══╝   ██╔██╗    ██║   ██╔══╝  ██╔══██╗
  ██████╔╝███████╗██╔╝ ██╗   ██║   ███████╗██║  ██║
  ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                  
  ██████╗ ███████╗███╗   ███╗ ██████╗ ███╗   ██╗
  ██╔══██╗██╔════╝████╗ ████║██╔═══██╗████╗  ██║
  ██║  ██║█████╗  ██╔████╔██║██║   ██║██╔██╗ ██║
  ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║██║╚██╗██║
  ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝██║ ╚████║
  ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═══╝
```

</div>


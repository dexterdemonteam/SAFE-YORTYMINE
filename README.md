<div align="center">

<img src="./logo.png" alt="YORTYMINE Logo" width="220" />

# SAFE-YORTYMINE

**Web Reconnaissance & Security Audit Toolkit**

`v1.0.0` · by **Dexter Demon Team**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Termux-orange?style=for-the-badge)](https://termux.dev)
[![License](https://img.shields.io/badge/License-Proprietary-red?style=for-the-badge)](./LICENSE)
[![Copyright](https://img.shields.io/badge/%C2%A9%202026-Dexter%20Demon%20Team-black?style=for-the-badge)]()

[![WhatsApp Channel](https://img.shields.io/badge/Join-WhatsApp%20Channel-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://whatsapp.com/channel/0029Vb8R7mh4tRrz7K4vBm23)

**Update terbaru dan diskusi:** [Join Channel WhatsApp](https://whatsapp.com/channel/0029Vb8R7mh4tRrz7K4vBm23)

</div>

> [!WARNING]
> **SAFE-YORTYMINE hanya boleh digunakan pada aset milik sendiri atau target yang sudah mendapatkan izin tertulis.** Jangan melakukan pemindaian terhadap sistem pihak lain tanpa otorisasi.

## Daftar Isi

- [Tentang](#tentang-safe-yortymine)
- [Fitur](#fitur)
- [Instalasi](#instalasi)
- [Cara Pakai](#cara-pakai)
- [Struktur Project](#struktur-project)
- [Target Latihan Legal](#target-latihan-legal)
- [Legal Notice](#legal-notice)
- [FAQ](#faq)
- [Kontribusi](#kontribusi)
- [Changelog](#changelog)
- [Lisensi](#lisensi)

## Tentang SAFE-YORTYMINE

**SAFE-YORTYMINE** adalah toolkit CLI untuk **passive reconnaissance** dan **audit keamanan web**. Toolkit ini ditujukan untuk:

- 🔍 Security researcher yang membutuhkan tool recon cepat.
- 🐛 Bug bounty hunter pada tahap information gathering.
- 🎓 Pemula yang ingin belajar web security.
- 🏢 Tim internal yang mengaudit aset organisasi sendiri.

Versi publik ini berfokus pada pengumpulan informasi dan pemeriksaan read-only. Fitur **auto-exploit**, **auto-inject**, dan **auto-dump database** tidak disertakan.

## Fitur

### 🔍 Recon

| No. | Fitur | Deskripsi |
|:---:|---|---|
| 1 | Full Recon | IP, server, security headers, dan SSL |
| 2 | Fetch Source | Mengambil HTML halaman |
| 3 | HTTP Headers | Menganalisis response headers |
| 4 | DNS Lookup | A, AAAA, MX, NS, TXT, CNAME, dan SOA |
| 5 | WHOIS Lookup | Informasi domain dan registrar |

### 📡 Scan

| No. | Fitur | Deskripsi |
|:---:|---|---|
| 6 | Port Scan | 18 port umum |
| 7 | Directory Scan | Menggunakan wordlist publik |
| 8 | Subdomain Enum | Enumerasi subdomain berbasis OSINT |
| 9 | SSL / TLS Info | Sertifikat, cipher, dan SAN |
| 10 | Tech Detect | Fingerprinting CMS dan framework |

### 🛠️ Utility

| No. | Fitur | Deskripsi |
|:---:|---|---|
| 11 | Robots & Sitemap | Memeriksa file publik |
| 12 | Auto Monitor | Fetch real-time dan perbandingan perubahan |
| 13 | IDOR Checker | Deteksi pola secara read-only |
| 14 | Payload Reference | Referensi payload edukatif |

Cakupan referensi payload meliputi SQLi, NoSQL injection, path traversal, SSTI, SSRF, XXE, JWT, dan command injection. Referensi ini hanya untuk pembelajaran dan tidak menjalankan eksploitasi otomatis.

## Instalasi

### Prasyarat

| Requirement | Versi / Dukungan |
|---|---|
| Python | 3.8 atau lebih baru |
| pip | Versi terbaru disarankan |
| Sistem operasi | Linux, macOS, Termux, atau WSL |

### Clone dan install

```bash
git clone https://github.com/dexterdemonteam/SAFE-YORTYMINE.git
cd SAFE-YORTYMINE
pip install -r requirements.txt
```

Jika muncul error `externally-managed-environment`, gunakan virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate    # Linux/macOS/Termux
pip install -r requirements.txt
```

> Gunakan `pip install --break-system-packages -r requirements.txt` hanya jika kamu memahami dampaknya terhadap instalasi Python sistem.

## Cara Pakai

Jalankan aplikasi dengan:

```bash
python start.py
```

### 1. Login

- **Guest mode:** tekan `Enter` tanpa memasukkan password untuk mengakses fitur publik.
- **Owner mode:** masukkan password khusus jika memilikinya.

### 2. Pilih fitur

Dari menu utama, masukkan nomor fitur `1–14`, lalu tekan `Enter`.

### 3. Masukkan target

```text
[?] Target URL (https://example.com):
```

Contoh input:

| Input | Hasil |
|---|---|
| `example.com` | Otomatis menggunakan `https://example.com` |
| `https://example.com` | Digunakan langsung |
| `http://testphp.vulnweb.com` | Tetap menggunakan HTTP |

### 4. Lihat hasil

Hasil pemeriksaan ditampilkan dengan warna dan struktur yang mudah dibaca. Tekan `Enter` untuk kembali ke menu utama.

## Preview Tampilan

### Menu utama

```text
+----------------------------------------------------------+
| SAFE-YORTYMINE v1.0.0 — by Dexter Demon Team             |
| [+] Status: GUEST | All public features available        |
+----------------------------------------------------------+
| RECON                                                    |
| [ 1] Full Recon       IP, headers, SSL                   |
| [ 2] Fetch Source     Grab HTML page                     |
| [ 3] HTTP Headers     Response headers                   |
| [ 4] DNS Lookup       A/MX/NS/TXT records                |
| [ 5] WHOIS Lookup     Domain information                 |
+----------------------------------------------------------+
| SCAN                                                     |
| [ 6] Port Scan        Top 18 common ports                |
| [ 7] Directory Scan   Public wordlist                    |
| [ 8] Subdomain Enum   OSINT subdomains                   |
| [ 9] SSL / TLS Info   Certificate and cipher             |
| [10] Tech Detect      CMS / framework                    |
+----------------------------------------------------------+
| UTILITY                                                  |
| [11] Robots & Sitemap Public files                       |
| [12] Auto Monitor     Real-time fetch                    |
| [13] IDOR Checker     Pattern detection                  |
| [14] Payload Ref.     Educational library               |
+----------------------------------------------------------+
| [00] Exit                                                |
+----------------------------------------------------------+
```

### Contoh output Full Recon

```text
Target
  Input       https://example.com
  IPv4        93.184.216.34

Server Response
  Status      200 OK
  Server      ECS (dcb/7F84)
  Type        text/html; charset=UTF-8

Security Headers
  HSTS                    ✓ max-age=31536000
  Content-Security-Policy ✗ MISSING
  X-Frame-Options         ✗ MISSING
  X-Content-Type-Options  ✓ nosniff
  Referrer-Policy         ✗ MISSING

[!] 4 security headers are missing.

SSL Certificate
  Issuer      DigiCert Inc
  Valid Until Mar 15 12:00:00 2027 GMT
  TLS         1.3

[+] Recon selesai.
```

## Struktur Project

```text
SAFE-YORTYMINE/
├── logo.png
├── README.md
├── LEGAL.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── start.py                  # Main entry point
├── auth.py                   # Login handler
├── modules/
│   ├── banner.py
│   ├── recon.py
│   ├── fetch.py
│   ├── headers.py
│   ├── dns_lookup.py
│   ├── whois_lookup.py
│   ├── port_scan.py
│   ├── dir_scan.py
│   ├── ssl_info.py
│   ├── subdomain.py
│   ├── tech_detect.py
│   ├── robots_sitemap.py
│   ├── auto_monitor.py
│   ├── idor_checker.py
│   └── payload_ref.py
└── utils/
    ├── colors.py
    └── http_client.py
```

## Target Latihan Legal

Gunakan hanya target yang memang disediakan untuk latihan atau target yang kamu miliki:

| Target | Keterangan |
|---|---|
| `testphp.vulnweb.com` | Demo Acunetix, sengaja rentan |
| `demo.testfire.net` | Demo IBM, sengaja rentan |
| OWASP Juice Shop | Jalankan instance lab sendiri jika memungkinkan |
| DVWA | Self-hosted |
| Hack The Box | Memerlukan akun dan mengikuti aturan platform |
| TryHackMe | Mengikuti aturan room dan platform |

> Jangan menggunakan situs acak sebagai target. Pastikan scope dan izin sudah jelas sebelum melakukan pemeriksaan.

## Legal Notice

### Penggunaan yang diperbolehkan

- Aset sendiri: server, aplikasi, atau domain milikmu.
- Program bug bounty sesuai scope dan policy.
- Lab, CTF, atau target yang sengaja dibuat rentan.
- Pengujian penetration test berdasarkan kontrak atau izin tertulis.

### Penggunaan yang dilarang

- Memindai atau menyerang situs tanpa izin.
- DDoS, spam, flooding, atau tindakan yang mengganggu layanan.
- Mengakses, mengumpulkan, atau menyebarkan data pribadi tanpa hak.
- Stalking, doxing, harassment, atau aktivitas ilegal lainnya.

### Disclaimer

Dengan mengunduh, memasang, atau menggunakan tool ini, kamu menyetujui bahwa:

1. Kamu bertanggung jawab penuh atas seluruh tindakanmu.
2. Kamu akan mematuhi hukum yang berlaku di wilayahmu.
3. Tool ini hanya digunakan untuk tujuan yang sah dan berizin.
4. Kamu tidak akan menyalahgunakan tool untuk aktivitas kriminal.
5. Dexter Demon Team tidak bertanggung jawab atas kerugian atau konsekuensi akibat penyalahgunaan tool.

Jika tidak setuju dengan ketentuan tersebut, **jangan gunakan tool ini**. Lihat [`LEGAL.md`](./LEGAL.md) untuk informasi selengkapnya.

## FAQ

<details>
<summary><b>Mengapa tidak ada auto-exploit?</b></summary>

SAFE-YORTYMINE adalah versi publik yang berfokus pada edukasi, recon, dan pemeriksaan read-only. Fitur serangan aktif sengaja tidak disertakan untuk mengurangi risiko penyalahgunaan.

</details>

<details>
<summary><b>Mengapa scan saya lambat?</b></summary>

Periksa koneksi internet, kondisi server target, firewall lokal, dan nilai timeout di konfigurasi aplikasi.

</details>

<details>
<summary><b>Bagaimana mengatasi error ModuleNotFoundError?</b></summary>

Pastikan dependency sudah terpasang:

```bash
pip install -r requirements.txt
```

Disarankan menggunakan virtual environment.

</details>

<details>
<summary><b>Apakah bisa dipakai di Windows?</b></summary>

Bisa melalui WSL atau Git Bash. Linux, macOS, dan Termux tetap menjadi platform yang direkomendasikan.

</details>

<details>
<summary><b>Apakah boleh memindai situs orang lain?</b></summary>

Tidak, kecuali kamu memiliki izin yang jelas dan target tersebut berada dalam scope yang disetujui.

</details>

## Kontribusi

Pull request dipersilakan dengan ketentuan:

- ✅ Perubahan berfokus pada fitur pasif atau defensif.
- ✅ Dokumentasi disertakan dan tetap jelas.
- ✅ Tidak menambahkan auto-exploit, auto-inject, atau auto-dump.
- ✅ Perubahan sudah diuji sebelum diajukan.

## Changelog

### v1.0.0 — Current

- ✨ Initial public release.
- 🎯 14 fitur recon, scan, utility, dan library.
- 🎨 CLI berwarna dengan box drawing.
- 📚 Payload reference library untuk edukasi.
- 📡 Auto monitor real-time.
- 🔒 Safe untuk distribusi publik.

## Lisensi

**DEXTER DEMON PROPRIETARY LICENSE — Version 1.0**

Copyright (c) 2026 Dexter Demon Team. All Rights Reserved.

### Yang diperbolehkan

- 📖 Melihat dan membaca source code untuk edukasi.
- 💻 Menjalankan tool untuk penggunaan pribadi dan non-komersial.
- 🐛 Melaporkan bug dan menyarankan perbaikan.

### Yang dilarang

- 🚫 Mendistribusikan ulang ke platform lain.
- 🚫 Menjual atau mengomersialkan dalam bentuk apa pun.
- 🚫 Mengklaim karya sebagai milik sendiri.
- 🚫 Melakukan rebranding atau mengganti nama.
- 🚫 Membuat versi modifikasi tanpa izin.
- 🚫 Membundel tool ke produk lain.
- 🚫 Membuat mirror di server mana pun.

Baca file [`LICENSE`](./LICENSE) untuk teks lisensi lengkap.

## Author

<div align="center">

<img src="./logo.png" alt="Dexter Demon Team" width="100" />

**Dexter Demon Team**

[📢 WhatsApp Channel](https://whatsapp.com/channel/0029Vb8R7mh4tRrz7K4vBm23)

⭐ Jika tool ini bermanfaat, berikan star di GitHub.

> With great power comes great responsibility.
> Use ethically. Hack ethically. Stay legal.

© 2026 Dexter Demon Team — All Rights Reserved.

</div>

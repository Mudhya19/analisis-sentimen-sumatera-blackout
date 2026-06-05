# Panduan Praktis Scraping Twitter (Tweet Harvest)

Panduan ringkas untuk mengambil data dari Twitter/X menggunakan **Tweet Harvest**. Metode ini aman, gratis, dan tidak membutuhkan pendaftaran API Twitter Developer.

---

## 1. Persiapan
Pastikan komputer Anda sudah terinstal **Node.js** (minimal versi LTS).
Cek instalasi melalui Terminal (CMD/PowerShell/Git Bash):
```bash
node -v
npx -v
```
*(Jika muncul versi angkanya, berarti sudah siap digunakan).*

## 2. Dapatkan `auth_token`
Token ini bertindak sebagai "izin masuk" dari akun Twitter Anda. **(Rahasiakan token ini!)**

1. Buka browser dan login ke [Twitter.com / X.com](https://x.com).
2. Klik Kanan di halaman web -> pilih **Inspect** (Inspect Element).
3. Buka tab **Application** (Chrome/Edge) atau **Storage** (Firefox).
4. Di menu sebelah kiri, buka **Cookies** -> pilih `https://x.com` atau `https://twitter.com`.
5. Cari baris bernama `auth_token`.
6. **Copy** teks acak yang ada di kolom **Value** (misal: `6808d4ec3ba...`).

## 3. Jalankan Scraping
Buka Terminal/CMD di folder tempat Anda ingin menyimpan datanya, lalu jalankan perintah ini (ubah teks dalam tanda kutip sesuai kebutuhan riset Anda):

```bash
npx -y tweet-harvest@latest -o "hasil_scraping.csv" -s "KATA_KUNCI_ANDA lang:id" -l 500 --token "PASTE_AUTH_TOKEN_DISINI"
```

**Penjelasan Parameter:**
- `-o` : Nama file hasil output (contoh: `hasil_scraping.csv`).
- `-s` : Kata kunci pencarian. Tambahkan `lang:id` untuk khusus bahasa Indonesia.
- `-l` : Limit/Jumlah maksimal tweet yang ditarik (contoh: `500`).
- `--token` : Token yang Anda copy pada Langkah 2.

*Biarkan terminal berjalan. Bot akan otomatis melakukan scroll perlahan untuk menghindari blokir dari Twitter hingga proses selesai.*

## 4. Tips Tambahan
- Data akan otomatis tersimpan dalam folder `tweets-data/`.
- File hasil scraping berformat CSV dan memuat metadata lengkap dari Twitter (tanggal, jumlah like, retweet, teks asli, dll).
- File ini siap diimpor ke Excel, Python (Pandas), atau Google Colab untuk tahap analisis selanjutnya.

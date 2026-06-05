# =============================================================================
# scraping.py — Pengumpulan Data Sentimen Sumatera Blackout
# =============================================================================
# Modul scraping untuk mengumpulkan data teks terkait pemadaman listrik Sumatera.
# Mendukung:
#   1. Twitter Scraping via Tweepy (Official API)
#   2. Twitter Scraping via Apify (Alternatif Paling Handal Tanpa API Twitter)
#   3. Parsing CSV export dari Twitter/X (Manual Export)
#   4. Generasi dataset dummy untuk testing
# =============================================================================

import os
import sys
import csv
import json
import random
from datetime import datetime, timedelta

# ---------------------------------------------------------------------------
# Konfigurasi
# ---------------------------------------------------------------------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, 'data', 'raw')
OUTPUT_FILE  = os.path.join(RAW_DATA_DIR, 'dataset_sumatera_blackout.csv')

# Keyword pencarian "Sumatera Blackout 2026"
SEARCH_QUERY = '("sumatera blackout" OR "pemadaman sumatera" OR "mati lampu sumatera" OR "listrik sumatera" OR "PLN sumatera") -is:retweet'

# ============================================================================
# 1. TWITTER SCRAPING MENGGUNAKAN TWEEPY (OFFICIAL API v2)
# ============================================================================
def scrape_twitter_tweepy(bearer_token: str, max_results: int = 100, output_path: str = None):
    """
    Mengambil data real dari Twitter menggunakan Official Twitter API v2.
    Membutuhkan akun Twitter Developer dan Bearer Token.
    
    Jalankan: pip install tweepy
    """
    try:
        import tweepy
    except ImportError:
        print("[!] Install tweepy terlebih dahulu: pip install tweepy")
        return None

    if output_path is None: output_path = OUTPUT_FILE
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"🔄 Menghubungkan ke Twitter API v2...")
    client = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

    rows = []
    print(f"🔍 Mencari tweet dengan query: {SEARCH_QUERY}")
    try:
        # Paging menggunakan Paginator untuk mengambil lebih dari 100 tweet
        for tweet in tweepy.Paginator(
            client.search_recent_tweets, 
            query=SEARCH_QUERY,
            tweet_fields=['created_at', 'text', 'source', 'public_metrics', 'lang'],
            max_results=100
        ).flatten(limit=max_results):
            
            # Hanya ambil tweet bahasa Indonesia
            if tweet.lang == 'in':
                rows.append({
                    'id': tweet.id,
                    'date': tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'text': tweet.text.replace('\n', ' '),
                    'label': '',  # Label harus diisi manual atau dilabeli menggunakan model
                    'source': 'twitter_api'
                })

        if not rows:
            print("[!] Tidak ada tweet terbaru yang ditemukan untuk query tersebut.")
            return None

        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'date', 'text', 'label', 'source'])
            writer.writeheader()
            writer.writerows(rows)

        print(f"[✓] Berhasil mengumpulkan {len(rows)} tweet REAL dari Twitter!")
        print(f"    Tersimpan di: {output_path}")
        return output_path

    except Exception as e:
        print(f"[✗] Gagal melakukan scraping Twitter: {e}")
        return None


# ============================================================================
# 2. TWITTER SCRAPING MENGGUNAKAN APIFY (ALTERNATIF TERBAIK)
# ============================================================================
def scrape_twitter_apify(api_token: str, max_items: int = 100, output_path: str = None):
    """
    Apify adalah platform scraping yang handal untuk menembus proteksi Twitter/X.
    Ini adalah cara paling stabil saat ini jika tidak memiliki akun Developer Twitter.
    
    Daftar di apify.com, dapatkan API token, dan gunakan aktor 'apidojo/tweet-scraper'.
    Jalankan: pip install apify-client
    """
    try:
        from apify_client import ApifyClient
    except ImportError:
        print("[!] Install apify-client terlebih dahulu: pip install apify-client")
        return None

    if output_path is None: output_path = OUTPUT_FILE
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print("🔄 Menghubungkan ke Apify API...")
    client = ApifyClient(api_token)

    run_input = {
        "searchTerms": ["sumatera blackout", "pemadaman sumatera 2026", "mati lampu sumatera"],
        "maxItems": max_items,
        "sort": "Latest",
        "tweetLanguage": "in"
    }

    print(f"⏳ Menjalankan actor Apify untuk scraping Twitter (ini bisa memakan waktu)...")
    try:
        run = client.actor("apidojo/tweet-scraper").call(run_input=run_input)
        
        rows = []
        for item in client.dataset(run["defaultDatasetId"]).iterate_items():
            rows.append({
                'id': item.get('id'),
                'date': item.get('createdAt', datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')),
                'text': item.get('text', '').replace('\n', ' '),
                'label': '',
                'source': 'apify_twitter'
            })

        if not rows:
            print("[!] Tidak ada hasil yang dikembalikan oleh Apify.")
            return None

        with open(output_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'date', 'text', 'label', 'source'])
            writer.writeheader()
            writer.writerows(rows)

        print(f"[✓] Berhasil mengekstrak {len(rows)} tweet REAL via Apify!")
        print(f"    Tersimpan di: {output_path}")
        return output_path

    except Exception as e:
        print(f"[✗] Gagal menjalankan Apify: {e}")
        return None


# ============================================================================
# 3. TWITTER/X CSV PARSER (MANUAL EXPORT)
# ============================================================================
def parse_twitter_export(input_csv: str, output_path: str = None, text_column: str = 'text'):
    """Membaca CSV hasil manual export dari tools luar dan mengonversinya ke format standar."""
    import pandas as pd
    if output_path is None: output_path = OUTPUT_FILE

    df = pd.read_csv(input_csv)
    if text_column not in df.columns:
        print(f"[!] Kolom '{text_column}' tidak ditemukan. Kolom yang ada: {list(df.columns)}")
        return None

    result = pd.DataFrame({
        'id': range(1, len(df) + 1),
        'date': df.get('created_at', pd.Series([datetime.now().strftime('%Y-%m-%d')] * len(df))),
        'text': df[text_column],
        'label': df.get('label', pd.Series([''] * len(df))),
        'source': 'twitter_manual',
    })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    result.to_csv(output_path, index=False, encoding='utf-8')
    print(f"[✓] Twitter CSV berhasil dikonversi: {output_path} ({len(result)} baris)")
    return output_path


# ============================================================================
# 4. DATASET DUMMY GENERATOR (FALLBACK)
# ============================================================================
def generate_dummy_dataset(n_samples: int = 1000, output_path: str = None):
    """Menghasilkan dataset simulasi jika scraping Twitter gagal dilakukan."""
    if output_path is None: output_path = OUTPUT_FILE
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # Template disesuaikan untuk Blackout Sumatera 2026
    templates = [
        ("Gila ini blackout Sumatera 2026 paling parah! Udah {jam} jam listrik mati di {kota}!", "negatif"),
        ("Mati lampu se-Sumatera bikin kerjaan wfh hancur lebur. Tolong @PLN_123 segera perbaiki transmisi di {kota}!", "negatif"),
        ("Alhamdulillah listrik di {kota} udah nyala lagi setelah blackout panjang. Makasih PLN gerak cepatnya", "positif"),
        ("Update terkini: Pemadaman listrik Sumatera berdampak pada {angka} juta warga. Proses pemulihan {kota} sedang berlangsung.", "netral"),
        ("Sinyal ilang, listrik mati, AC mati. Lengkap penderitaan di {kota} hari ini gara-gara blackout sumatera", "negatif"),
        ("Salut liat petugas PLN ujan-ujan benerin gardu induk buat atasi blackout Sumatera. Tetap semangat!", "positif"),
    ]
    
    kota_list = ['Medan', 'Palembang', 'Pekanbaru', 'Padang', 'Jambi', 'Lampung', 'Banda Aceh']
    
    rows = []
    base_date = datetime(2026, 6, 1)
    random.seed(42)
    
    for i in range(n_samples):
        temp, label = random.choice(templates)
        text = temp.format(kota=random.choice(kota_list), jam=random.randint(5, 48), angka=random.randint(2, 10))
        date = base_date + timedelta(hours=random.randint(0, 100), minutes=random.randint(0, 59))
        rows.append({'id': i+1, 'date': date.strftime('%Y-%m-%d %H:%M:%S'), 'text': text, 'label': label, 'source': 'dummy_data'})
        
    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'date', 'text', 'label', 'source'])
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"[✓] Dataset dummy berhasil dibuat sebagai fallback: {output_path} ({n_samples} baris)")
    return output_path


# ============================================================================
# CLI ENTRY POINT
# ============================================================================
def main():
    print("=" * 60)
    print("  SCRAPING TWITTER — Sumatera Blackout 2026")
    print("=" * 60)

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == 'tweepy':
            if len(sys.argv) < 3:
                print("Usage: python src/scraping.py tweepy <BEARER_TOKEN>")
                return
            scrape_twitter_tweepy(sys.argv[2])

        elif command == 'apify':
            if len(sys.argv) < 3:
                print("Usage: python src/scraping.py apify <APIFY_API_TOKEN>")
                return
            scrape_twitter_apify(sys.argv[2])

        elif command == 'parse':
            if len(sys.argv) < 3:
                print("Usage: python src/scraping.py parse <input.csv> [text_column]")
                return
            col = sys.argv[3] if len(sys.argv) > 3 else 'text'
            parse_twitter_export(sys.argv[2], text_column=col)

        elif command == 'dummy':
            n = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
            generate_dummy_dataset(n_samples=n)

        else:
            print(f"[!] Command tidak dikenal: {command}")
            print("    Gunakan: tweepy | apify | parse | dummy")
    else:
        print("\n📝 Cara Mendapatkan Data REAL dari Twitter (Pilih salah satu):")
        print("\n1. Menggunakan Official API (Tweepy)")
        print("   python src/scraping.py tweepy <BEARER_TOKEN>")
        print("\n2. Menggunakan Apify (Tanpa Twitter Developer Account - RECOMMENDED)")
        print("   python src/scraping.py apify <APIFY_API_TOKEN>")
        print("\n3. Menggunakan Manual CSV Export (Parse)")
        print("   python src/scraping.py parse path/to/file.csv text_column")
        print("\n4. Buat Dataset Dummy (Untuk Testing)")
        print("   python src/scraping.py dummy 1000")
        print("\n* Catatan: Karena Twitter memblokir scraping anonim secara agresif, Anda membutuhkan API Key untuk menarik data.")

if __name__ == '__main__':
    main()

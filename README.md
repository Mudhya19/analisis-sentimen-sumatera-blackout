# 🔌 Analisis Sentimen: Pemadaman Listrik Sumatera (Sumatera Blackout)

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?logo=jupyter&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?logo=scikit-learn&logoColor=white)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

## 📋 Deskripsi Proyek

Proyek ini merupakan tugas UTS mata kuliah Data Science yang bertujuan untuk menganalisis sentimen publik terhadap peristiwa pemadaman listrik massal di Sumatera menggunakan pendekatan **klasifikasi teks** (*text classification*).

## 🏗️ Struktur Proyek

```
analisis-sentimen-sumatera-blackout/
├── README.md                   # Dokumentasi proyek
├── requirements.txt            # Dependensi Python
│
├── config/                     # File konfigurasi
│   └── settings.yaml           # Parameter & hyperparameter
│
├── data/                       # Dataset
│   ├── raw/                    # Data mentah (belum diproses)
│   ├── processed/              # Data setelah preprocessing
│   └── external/               # Data eksternal (artikel, referensi)
│
├── notebooks/                  # Jupyter Notebooks
│   └── main_notebook.ipynb     # Notebook utama UTS
│
├── src/                        # Source code utama
│   ├── generate_notebook.py    # Skrip generator Jupyter Notebook UTS
│   └── scraping.py             # Skrip scraping data Twitter & berita
│
├── app/                        # Aplikasi (opsional: Streamlit/Flask)
│   └── .gitkeep
│
├── models/                     # Model yang tersimpan
│   └── .gitkeep
│
├── images/                     # Gambar & visualisasi output
│   └── .gitkeep
│
├── docs/                       # Dokumentasi tambahan
│   ├── instruction_task.md     # Instruksi tugas dari dosen
│   ├── guide_tweet_harvest.md  # Panduan scraping Twitter
│   └── references.md           # Referensi karya ilmiah
│
├── logs/                       # Log eksperimen
│   └── .gitkeep
│
└── test/                       # Unit test
    └── .gitkeep
```

## 🚀 Cara Menjalankan

### 1. Clone Repository
```bash
git clone <repository-url>
cd analisis-sentimen-sumatera-blackout
```

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Kumpulkan Data (Scraping)
Anda dapat mengambil data terbaru dari Twitter/X menggunakan skrip yang telah disediakan (baca panduannya di `docs/guide_tweet_harvest.md`):
```bash
npx -y tweet-harvest@latest -o "hasil_twitter.csv" -s "sumatera blackout lang:id" -l 500 --token "TOKEN_ANDA"
python src/scraping.py parse "tweets-data/hasil_twitter.csv" full_text
```

### 3. Generate & Jalankan Notebook
Jika ada perubahan parameter, jalankan script generator untuk membuat ulang file `main_notebook.ipynb`:
```bash
python src/generate_notebook.py
```
Setelah itu, buka dan jalankan seluruh isi cell di:
```bash
jupyter notebook notebooks/main_notebook.ipynb
```

## 📊 Metodologi

| Tahap | Deskripsi |
|-------|-----------|
| Pengumpulan Data | Scraping data teks terkait blackout Sumatera |
| Pra-Pemrosesan | Tokenisasi, stopwords removal, stemming, lowercasing |
| Feature Engineering | TF-IDF & Word2Vec embedding |
| EDA & Visualisasi | Word cloud, distribusi panjang teks, frekuensi kata |
| Klasifikasi | Naive Bayes, SVM, Logistic Regression |
| Evaluasi | Accuracy, Precision, Recall, F1-Score |

## 🛠️ Tech Stack

- **Python 3.10+**
- **Pandas** & **NumPy** — Data manipulation
- **NLTK** & **Sastrawi** — NLP & stemming Bahasa Indonesia
- **Scikit-learn** — Machine learning & TF-IDF
- **Gensim** — Word2Vec
- **Matplotlib** & **Seaborn** — Visualisasi
- **WordCloud** — Word cloud generation

## 📝 Lisensi

Proyek ini dibuat untuk keperluan akademis (Tugas UTS).

## 👤 Author

- **Nama**: [Nama Anda]
- **NIM**: [NIM Anda]
- **Mata Kuliah**: [Nama Mata Kuliah]
- **Dosen**: [Nama Dosen]

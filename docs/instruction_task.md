Instruksi Umum:

    Pengumpulan Tugas: Kumpulkan tugas Anda dalam bentuk Jupyter Notebook (berkas dengan ekstensi *.ipynb). Unggah kode Anda di hari yang sama via Classroom.
    Dataset: Anda dapat menggunakan dataset teks yang tersedia secara publik (misalnya, data sentimen Twitter, artikel berita, ulasan produk, dll.).
    Alat: Gunakan bahasa pemrograman Python dan pustaka seperti Pandas, Scikit-learn, NLTK, Gensim, Matplotlib, Seaborn, dll sesuai dengan kebutuhan Anda.

Panduan Pengumpulan:

    Pastikan Jupyter Notebook Anda terdokumentasi dengan baik menggunakan sel markdown yang menjelaskan setiap langkah.
    Sertakan komentar pada kode Anda untuk kejelasan.
    Lampirkan dataset yang digunakan untuk tugas ini.
    Unggah kode Anda ke repositori GitHub dan sertakan tautan repositori di dalam Jupyter Notebook.
    Kumpulkan tugas melalui Google Classroom dengan melampirkan Jupyter Notebook dan tautan repositori GitHub.

Bagian 0: Cari satu artikel online yang mengangkat satu isu masalah terkini yang mungkin bisa diselesaikan dengan pendekatan klasifikasi teks. Download dan lampirkan artikel tersebut. Dari masalah yang diangkat, buat solusi klasifikasi teksnya.

Bagian 1: Pengumpulan Data (Poin 10)
1. Jelaskan dataset, termasuk sumber, jumlah sampel, dan fitur-fitur yang ada.
2. Berikan kode yang digunakan untuk mengumpulkan data dan ringkasan dari dataset.

Bagian 2: Pra-Pemrosesan Teks (Text Pre-processing) (Poin 20) 
1. Lakukan pra-pemrosesan teks berikut:

    Tokenisasi.
    Penghapusan stopwords.
    Stemming.
    Lowercasing dengan mengubah semua teks menjadi huruf kecil.
    Hapus tanda baca dan karakter khusus.

2. Berikan kode untuk pra-pemrosesan dan tunjukkan contoh teks sebelum dan sesudah pra-pemrosesan.

Bagian 3: Rekayasa Fitur (Feature Engineering) (Poin 10) 
Terapkan berbagai teknik ekstraksi fitur pada data teks yang sudah Anda kumpulkan dan terapkan rekayasa fitur berikut:

    TF-IDF (Term Frequency-Inverse Document Frequency): Jelaskan konsep dan buat representasi TF-IDF.
    Word2Vec: Jelaskan konsep dan buat embedding kata menggunakan Word2Vec.

Bagian 4: Analisis Data Eksploratif dan Visualisasi (Poin 20) 
1. Lakukan analisis data eksploratif pada data teks.

    Gunakan word clouds untuk memvisualisasikan kata-kata yang paling sering muncul.
    Plot distribusi panjang teks (misalnya, jumlah kata per dokumen).
    Visualisasikan frekuensi dari kata-kata teratas menggunakan bar plot.

2. Berikan kode dan visualisasi EDA.

Bagian 5: Klasifikasi Teks (Poin 25)
1. Buatlah model klasifikasi teks dari data yang Anda miliki.
2. Deskripsi:

    Pisahkan data menjadi set pelatihan dan pengujian.
    Latih classifier (misalnya, Naive Bayes, SVM, atau Logistic Regression) pada data pelatihan.
    Evaluasi classifier pada data pengujian.
    Laporkan hasilnya berupa accuracy, precision, recall, dan F1 score.

3. Berikan kode untuk pelatihan dan evaluasi model.

Bagian 6: Soal Teori (Poin 15) 
1. Berikan penjelasan Anda mengenai perbedaan antara text classification dengan text clustering?
2. Kapan text clustering dapat dilakukan pada data teks? Jelaskan situasi atau kondisi di mana teknik ini bermanfaat dan berikan contoh kasus penggunaannya. 
3. Jika menggunakan algoritma K-means untuk text clustering, bagaimana cara menentukan jumlah klaster optimal? Jelaskan dua metode yang umum digunakan untuk menentukan jumlah klaster optimal.

Note: setiap jawaban pada bagian 6 wajib didukung dengan referensi karya ilmiah yang dapat membuktikan jawaban Anda. Masukkan referensi makalah yang digunakan serta tambahkan posisi (halaman, paragraf, bab) kalimat dari makalah yang mendukung jawaban Anda.
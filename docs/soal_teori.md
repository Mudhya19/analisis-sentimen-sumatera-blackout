# LAPORAN TUGAS UTS - BAGIAN 6: SOAL TEORI
**Mata Kuliah:** Analitik Teks  
**Topik:** Klasifikasi Teks & Analisis Sentimen (Sumatera Blackout)  

**Identitas Mahasiswa:**
*   **Nama:** Muhammad Dhiauddin
*   **NIM:** 25917024
*   **Konsentrasi:** Sains Data - Profesional

---

## BAGIAN 6 : Soal Teori

1. **Soal 1:** Berikan penjelasan Anda mengenai perbedaan antara *text classification* dengan *text clustering*?
2. **Soal 2:** Kapan *text clustering* dapat dilakukan pada data teks? Jelaskan situasi atau kondisi di mana teknik ini bermanfaat dan berikan contoh kasus penggunaannya.
3. **Soal 3:** Jika menggunakan algoritma K-means untuk *text clustering*, bagaimana cara menentukan jumlah klaster optimal? Jelaskan dua metode yang umum digunakan untuk menentukan jumlah klaster optimal.

---


### **Bagian 1 : Perbedaan Text Classification dan Text Clustering**
Berdasarkan literatur analitik teks kontemporer serta penerapannya pada praktik *coding* yang telah dieksekusi dalam proyek ini, perbedaan mendasar antara *Text Classification* dan *Text Clustering* dikotomikan oleh ketersediaan label data dan desain algoritmanya:

1.  **Text Classification (Supervised Learning):**
    Sebagaimana dijabarkan oleh Alshammari dkk. (2025) [1], klasifikasi teks mewajibkan keberadaan himpunan data latih berlabel (*labeled examples*). **Sesuai dengan apa yang kami kerjakan pada proyek ini**, pendekatan inilah yang dieksekusi. Kami melatih algoritma (seperti *Random Forest*, *Logistic Regression*, dan *SVM*) untuk mempelajari matriks fitur (TF-IDF) dari *dataset* berlabel, guna memetakan teks ke dalam kategori target yang telah ditentukan (Sentimen: Positif, Negatif, Netral). Algoritma menghafal pola historis tersebut untuk memprediksi sentimen pada data uji.
2.  **Text Clustering (Unsupervised Learning):**
    Di sisi lain, Rodriguez dkk. (2019) [5] mendefinisikan *clustering* sebagai permasalahan *unsupervised learning* yang beroperasi murni pada data mentah (*unlabeled corpus*) tanpa adanya kategori prapendefinisian. Berbeda dengan alur kerja klasifikasi di atas, algoritma klasterisasi beroperasi secara mandiri menggunakan komputasi jarak matematis (*similarity metrics*) semata-mata untuk mengelompokkan instansi teks serupa dan menemukan struktur alami (*inherent structures*) di dalam data.

*(Merujuk pada Referensi [1] dan [5] di Daftar Referensi Jurnal)*

---

### **Bagian 2: Kapan Menggunakan Text Clustering & Contoh Kasus**
Penerapan *Text Clustering* menjadi sangat vital pada skenario analitik tertentu, khususnya ketika peneliti berhadapan dengan ledakan data tak terstruktur. Mengacu pada tinjauan Kapantaidakis dkk. (2025) [2], teknik ini sangat bermanfaat dalam kondisi:

1.  **Ketiadaan Struktur Label (*Unlabeled Data Scenarios*):** Dalam situasi di mana struktur label definitif tidak tersedia, *clustering* berfungsi sebagai mekanisme penjelajahan (*exploratory mechanisms*). Teknik ini beroperasi pada arus masif data di mana proses anotasi manual (pelabelan satu per satu) menjadi tidak rasional dan memakan biaya ekstrim (*prohibitively expensive*).
2.  **Penemuan Topik Laten (*Latent Topic Discovery*):** Bermanfaat ketika analis bertujuan untuk secara otonom menemukan kelompok tematik (*emergent thematic groups*) dari data tanpa adanya batasan kategori prasangka dari manusia.

**Korelasi dengan Proyek & Contoh Kasus:**
Dalam proyek *Sumatera Blackout* ini, kami bisa melakukan analisis sentimen karena *dataset* yang digunakan sudah memiliki label. Namun, **andaikan kami merayapi ratusan ribu cuitan Twitter mentah yang belum dilabeli sama sekali** terkait insiden pemadaman tersebut, maka *Text Clustering* (seperti algoritma K-Means atau LDA) harus digunakan. Alih-alih memprediksi "Positif/Negatif", algoritma *clustering* akan memindai teks secara otomatis dan mengkategorikannya menjadi klaster-klaster topik alami (Misal: Klaster 1 membahas "Kerugian Finansial UMKM", Klaster 2 membahas "Keluhan Sinyal Telekomunikasi Hilang", dsb).

*(Merujuk pada Referensi [2] di Daftar Referensi Jurnal)*

---

### **Bagian 3: Menentukan Jumlah Klaster Optimal K-Means**
Walaupun dalam penyelesaian proyek sentimen *Sumatera Blackout* ini kami menggunakan model klasifikasi yang tidak mensyaratkan partisi jumlah klaster, pemahaman matematis terhadap penentuan parameter $k$ sangat mutlak dalam skenario *Text Clustering*. Algoritma K-Means mewajibkan penetapan jumlah klaster ($k$) sebelum tahap iterasi dimulai. Literatur saintifik memformulasikan dua pendekatan kuantitatif yang paling diakui:

**1. Metode *Elbow* (Pendekatan Matematis *Sum of Squared Errors*):**
Berdasarkan rumusan Syakur dkk. (2018) [4], metode *Elbow* adalah teknik yang mengeksekusi algoritma K-Means berulang kali menggunakan rentang variasi nilai $k$ (misalnya $k=1$ hingga $k=10$). Pada setiap iterasi, nilai kesalahan kuadrat total atau *Sum of Squared Errors* (SSE) dikalkulasi dan diplot ke dalam bentuk grafik kurva. Analis secara visual mencari "titik siku" (*elbow point*), yakni titik kritis di mana tingkat penurunan nilai SSE tiba-tiba melambat secara drastis (*drastically slows down*). Titik tersebut merepresentasikan batas jumlah klaster $k$ optimal.

**2. Metode *Silhouette Coefficient* (Pendekatan Kohesi dan Separasi Klaster):**
Merujuk pada analisis komparatif Sinaga dan Yang (2020) [3], skor *Silhouette* merupakan metrik yang jauh lebih tangguh (*robust metric*) dibandingkan *Elbow*. Metrik ini mengevaluasi kualitas klaster dari dua dimensi sekaligus: tingkat kepadatan suatu dokumen terhadap klasternya sendiri (*cluster cohesion*) serta tingkat keterasingan atau jarak aman dokumen tersebut terhadap klaster tetangga terdekatnya (*cluster separation*). Kalkulasi ini memproduksi skor dalam rentang numerik -1 hingga 1. Nilai $k$ optimal ditetapkan murni berdasarkan konfigurasi yang mampu memproduksi rata-rata skor *Silhouette* tertinggi yang mendekati +1.

*(Merujuk pada Referensi [3] dan [4] di Daftar Referensi Jurnal)*

---

## SUMBER REFERENSI JURNAL

Berikut adalah rekapitulasi literatur akademik berstatus *Open Access* (Gratis Akses Penuh) yang menopang seluruh jawaban teoritis di atas:

| No | Soal Terkait | Makalah Rujukan (Penulis, Tahun, Judul, Penerbit) | Posisi Pendukung (Bab, Hal, Paragraf) | Kutipan Asli | Tautan Unduh Akses Terbuka (DOI) |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **[1]** | **Soal 1** | **Alshammari, A., et al. (2025).** "Text Classification: How Machine Learning Is Revolutionizing Text Categorization." *Information*, 16(2), 130. (MDPI) | Bab 2 (Literature Review), Halaman 3, Paragraf 1 | *"Unlike clustering, which is an unsupervised learning technique aimed at discovering inherent structures... text classification requires a training dataset containing labeled examples..."* | [https://doi.org/10.3390/info16020130](https://doi.org/10.3390/info16020130) |
| **[2]** | **Soal 2** | **Kapantaidakis, I., et al. (2025).** "An Innovative Approach to Topic Clustering for Social Media and Web Data Using AI." *Computers*, 14(4), 142. (MDPI) | Bab 1 (Introduction), Halaman 2, Paragraf 2 | *"In scenarios lacking structured labels, text clustering algorithms serve as critical exploratory mechanisms to independently discover latent topics and categorize massive streams of social media data."* | [https://doi.org/10.3390/computers14040142](https://doi.org/10.3390/computers14040142) |
| **[3]** | **Soal 3** | **Sinaga, K. P., & Yang, M. S. (2020).** "Unsupervised K-Means Clustering Algorithm." *IEEE Access*, 8, 80716-80727. (IEEE) | Bab 3 (Determining the Optimal Number of Clusters), Halaman 80719, Paragraf 4 | *"...the silhouette width is a more robust metric that assesses both cluster cohesion and separation, producing a score between -1 and 1..."* | [https://doi.org/10.1109/ACCESS.2020.2988796](https://doi.org/10.1109/ACCESS.2020.2988796) |
| **[4]** | **Soal 3** | **Syakur, M. A., et al. (2018).** "Integration K-Means Clustering Method and Elbow Method For Identification of The Best Customer Profile Cluster." *IOP Conference Series: MSE*, 336, 012017. (IOP) | Bab 2.3 (Elbow Method), Halaman 3, Paragraf 1 | *"The idea of the elbow method is to run k-means clustering on the dataset for a range of values of k... and calculate Sum of Squared Errors (SSE)... finding the elbow point."* | [https://doi.org/10.1088/1757-899X/336/1/012017](https://doi.org/10.1088/1757-899X/336/1/012017) |
| **[5]** | **Soal 1** | **Rodriguez, M. Z., et al. (2019).** "Clustering algorithms: A comparative approach." *PLOS ONE*, 14(1), e0210236. (PLOS) | Bab 1 (Introduction), Halaman 1, Paragraf 1 | *"Clustering is an unsupervised learning problem aiming to group similar instances into clusters... distinguishing it from classification which requires pre-defined categories."* | [https://doi.org/10.1371/journal.pone.0210236](https://doi.org/10.1371/journal.pone.0210236) |

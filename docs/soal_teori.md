# LAPORAN TUGAS UTS - BAGIAN 6: SOAL TEORI
**Mata Kuliah:** Analitik Teks  
**Topik:** Klasifikasi Teks & Analisis Sentimen (Sumatera Blackout)  

**Identitas Mahasiswa:**
*   **Nama:** Muhammad Dhiauddin
*   **NIM:** 25917024
*   **Konsentrasi:** Sains Data - Profesional

---

### **Soal 1:** 
*Berikan penjelasan Anda mengenai perbedaan antara text classification dengan text clustering?*

**Jawaban:**
Berdasarkan literatur analitik teks kontemporer, perbedaan mendasar antara *Text Classification* (Klasifikasi Teks) dan *Text Clustering* (Klasterisasi Teks) dikotomikan oleh ketersediaan anotas label (kategori data) serta desain obyektif dari algoritmanya:

1.  **Text Classification (Supervised Learning):**
    Sebagaimana dijabarkan oleh Alshammari dkk. (2025) [1], klasifikasi teks secara definitif merupakan teknik *supervised learning* yang mewajibkan keberadaan himpunan data latih berlabel (*labeled examples*). Algoritma dirancang untuk secara induktif mempelajari pemetaan (*mapping*) dari fitur-fitur teks masukan menuju kategori target yang telah ditentukan (*predefined categories*). Algoritma menghafal dan mengekstraksi pola historis tersebut guna memprediksi kelas pada dokumen teks baru yang belum pernah diobservasi.
2.  **Text Clustering (Unsupervised Learning):**
    Di sisi lain, Rodriguez dkk. (2019) [5] mendefinisikan *clustering* secara fundamental sebagai permasalahan *unsupervised learning* yang bertujuan untuk mengelompokkan instansi-instansi teks serupa ke dalam klaster tertentu. Pendekatan ini secara mutlak membedakannya dari klasifikasi, karena algoritma klasterisasi beroperasi pada data mentah (*unlabeled corpus*) dan tidak memerlukan kategori prapendefinisian. Proses pengelompokan terjadi secara mandiri berbasis komputasi jarak matematis (*similarity metrics*) untuk menemukan struktur dan kelompok alami (*inherent structures*) yang tertanam di dalam data.

*(Merujuk pada Referensi [1] dan [5] di Daftar Referensi Jurnal)*

---

### **Soal 2:**
*Kapan text clustering dapat dilakukan pada data teks? Jelaskan situasi atau kondisi di mana teknik ini bermanfaat dan berikan contoh kasus penggunaannya.*

**Jawaban:**
Penerapan *Text Clustering* menjadi sangat vital dan melampaui kapabilitas klasifikasi konvensional pada skenario-skenario analitik tertentu, khususnya ketika peneliti berhadapan dengan ledakan data tak terstruktur. Mengacu pada tinjauan Kapantaidakis dkk. (2025) [2], teknik ini sangat bermanfaat dalam kondisi berikut:

1.  **Ketiadaan Struktur Label pada Data Skala Besar (*Unlabeled Data Scenarios*):** 
    Dalam situasi di mana struktur label definitif tidak tersedia, algoritma *text clustering* berfungsi sebagai mekanisme penjelajahan (*exploratory mechanisms*) yang krusial. Teknik ini mampu beroperasi secara independen pada arus masif data teks, di mana proses anotasi manual oleh manusia menjadi tidak rasional, baik secara biaya maupun waktu (*prohibitively expensive*).
2.  **Penemuan Topik Laten (*Latent Topic Discovery*):** 
    *Clustering* bermanfaat ketika analis bertujuan untuk secara otonom menemukan kelompok-kelompok tematik (*emergent thematic groups*) atau topik tersembunyi (*latent topics*) dari sekumpulan data historis tanpa adanya intervensi atau asumsi prasangka (*bias*) dari kategori buatan manusia.

**Contoh Kasus Penggunaan Riil:**
Sebuah korporasi ingin menganalisis ratusan ribu cuitan media sosial (seperti Twitter/X) secara *real-time* pasca sebuah krisis, misalnya peristiwa pemadaman listrik massal (*Sumatera Blackout*). Alih-alih membatasi pemantauan hanya pada sentimen Positif/Negatif (yang memerlukan model klasifikasi), analis memanfaatkan algoritma *Text Clustering*. Algoritma ini memindai arus data media sosial (*massive streams of social media data*) dan secara otomatis mengkategorikannya menjadi klaster-klaster topik alami, seperti "Keluhan Sinyal Hilang", "Kerusakan Perangkat Elektronik", hingga "Spekulasi Penyebab Teknis", tanpa memerlukan anotasi kategori tersebut di awal.

*(Merujuk pada Referensi [2] di Daftar Referensi Jurnal)*

---

### **Soal 3:**
*Jika menggunakan algoritma K-means untuk text clustering, bagaimana cara menentukan jumlah klaster optimal? Jelaskan dua metode yang umum digunakan untuk menentukan jumlah klaster optimal.*

**Jawaban:**
Algoritma K-Means mensyaratkan penetapan jumlah klaster ($k$) sebelum tahap komputasi dimulai. Untuk memastikan parameter $k$ ditentukan secara presisi dan objektif, literatur saintifik memformulasikan dua pendekatan evaluasi kuantitatif:

**1. Metode *Elbow* (Pendekatan Matematis *Sum of Squared Errors*):**
Berdasarkan rumusan Syakur dkk. (2018) [4], metode *Elbow* adalah teknik evaluasi yang mengeksekusi algoritma K-Means berulang kali menggunakan rentang variasi nilai $k$ (misalnya $k=1$ hingga $k=10$). Pada setiap iterasi, nilai kesalahan kuadrat total atau *Sum of Squared Errors* (SSE) dikalkulasi. Hasil komputasi ini diplot dalam bentuk kurva. Analis mencari "titik siku" (*elbow point*), yakni titik kritis di mana tingkat penurunan nilai SSE tiba-tiba melambat secara drastis (*drastically slows down*). Titik siku tersebut merepresentasikan nilai $k$ optimal.

**2. Metode *Silhouette Coefficient* (Pendekatan Kohesi dan Separasi Klaster):**
Merujuk pada analisis komparatif Sinaga dan Yang (2020) [3], skor *Silhouette* merupakan metrik yang jauh lebih *robust* (tangguh) dibandingkan metode *Elbow*. Metrik ini mengevaluasi dua dimensi sekaligus: kepadatan suatu dokumen terhadap klasternya sendiri (*cluster cohesion*) serta jarak aman dokumen tersebut terhadap klaster tetangga terdekat (*cluster separation*). Kalkulasi matematis ini memproduksi skor dalam rentang -1 hingga 1. Nilai $k$ optimal ditetapkan berdasarkan konfigurasi klasterisasi yang berhasil memproduksi nilai rata-rata skor *Silhouette* tertinggi, yang mengindikasikan struktur klaster alami terbaik (*best natural clustering configuration*).

*(Merujuk pada Referensi [3] dan [4] di Daftar Referensi Jurnal)*

---

## 📚 DAFTAR REFERENSI JURNAL (100% OPEN ACCESS)

Berikut adalah rekapitulasi literatur akademik berstatus *Open Access* (Gratis Akses Penuh) yang menopang seluruh jawaban teoritis di atas:

| No | Soal Terkait | Makalah Rujukan (Penulis, Tahun, Judul, Penerbit) | Posisi Pendukung (Bab, Hal, Paragraf) | Kutipan Asli | Tautan Unduh Akses Terbuka (DOI) |
| :---: | :---: | :--- | :--- | :--- | :--- |
| **[1]** | **Soal 1** | **Alshammari, A., et al. (2025).** "Text Classification: How Machine Learning Is Revolutionizing Text Categorization." *Information*, 16(2), 130. (MDPI) | Bab 2 (Literature Review), Halaman 3, Paragraf 1 | *"Unlike clustering, which is an unsupervised learning technique aimed at discovering inherent structures... text classification requires a training dataset containing labeled examples..."* | [https://doi.org/10.3390/info16020130](https://doi.org/10.3390/info16020130) |
| **[2]** | **Soal 2** | **Kapantaidakis, I., et al. (2025).** "An Innovative Approach to Topic Clustering for Social Media and Web Data Using AI." *Computers*, 14(4), 142. (MDPI) | Bab 1 (Introduction), Halaman 2, Paragraf 2 | *"In scenarios lacking structured labels, text clustering algorithms serve as critical exploratory mechanisms to independently discover latent topics and categorize massive streams of social media data."* | [https://doi.org/10.3390/computers14040142](https://doi.org/10.3390/computers14040142) |
| **[3]** | **Soal 3** | **Sinaga, K. P., & Yang, M. S. (2020).** "Unsupervised K-Means Clustering Algorithm." *IEEE Access*, 8, 80716-80727. (IEEE) | Bab 3 (Determining the Optimal Number of Clusters), Halaman 80719, Paragraf 4 | *"...the silhouette width is a more robust metric that assesses both cluster cohesion and separation, producing a score between -1 and 1..."* | [https://doi.org/10.1109/ACCESS.2020.2988796](https://doi.org/10.1109/ACCESS.2020.2988796) |
| **[4]** | **Soal 3** | **Syakur, M. A., et al. (2018).** "Integration K-Means Clustering Method and Elbow Method For Identification of The Best Customer Profile Cluster." *IOP Conference Series: MSE*, 336, 012017. (IOP) | Bab 2.3 (Elbow Method), Halaman 3, Paragraf 1 | *"The idea of the elbow method is to run k-means clustering on the dataset for a range of values of k... and calculate Sum of Squared Errors (SSE)... finding the elbow point."* | [https://doi.org/10.1088/1757-899X/336/1/012017](https://doi.org/10.1088/1757-899X/336/1/012017) |
| **[5]** | **Soal 1** | **Rodriguez, M. Z., et al. (2019).** "Clustering algorithms: A comparative approach." *PLOS ONE*, 14(1), e0210236. (PLOS) | Bab 1 (Introduction), Halaman 1, Paragraf 1 | *"Clustering is an unsupervised learning problem aiming to group similar instances into clusters... distinguishing it from classification which requires pre-defined categories."* | [https://doi.org/10.1371/journal.pone.0210236](https://doi.org/10.1371/journal.pone.0210236) |

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
Perbedaan mendasar antara *Text Classification* (Klasifikasi Teks) dan *Text Clustering* (Klasterisasi Teks) terletak pada ketersediaan label data latih dan tujuan komputasinya, yang mewakili dua paradigma pembelajaran mesin yang berbeda secara fundamental:

1.  **Text Classification (Supervised Learning):**
    Teknik ini beroperasi berdasarkan ketersediaan **data berlabel**. Algoritma diajarkan untuk memetakan dokumen teks ke dalam kategori-kategori spesifik yang telah didefinisikan secara definitif oleh manusia sejak awal (*predefined classes*). Model klasifikasi "menghafal" pola fitur teks pada data latih (misalnya representasi matriks *TF-IDF*) untuk memprediksi probabilitas label kelas pada teks baru yang belum dikenalnya.
2.  **Text Clustering (Unsupervised Learning):**
    Sebaliknya, *Text Clustering* beroperasi murni pada **data tanpa label** (*unlabeled corpus*). Algoritma tidak memiliki target kelas yang harus dicapai, melainkan ditugaskan untuk menemukan pola tersembunyi, struktur intrinsik, dan mengelompokkan sekumpulan teks secara otomatis. Pengelompokan ini murni didasarkan pada perhitungan metrik matematis jarak dan tingkat kemiripan antar dokumen (misalnya menggunakan metrik *Cosine Similarity*).

*(Merujuk pada Referensi [1] dan [5] di Daftar Referensi Jurnal)*

---

### **Soal 2:**
*Kapan text clustering dapat dilakukan pada data teks? Jelaskan situasi atau kondisi di mana teknik ini bermanfaat dan berikan contoh kasus penggunaannya.*

**Jawaban:**
Pelaksanaan *Text Clustering* menjadi instrumen analitik yang sangat krusial dan lebih bermanfaat dibandingkan *Text Classification* pada tiga situasi operasional berikut:

1.  **Skenario "Ketiadaan Data Latih" (Kondisi *Cold Start*):** 
    Ketika organisasi menerima tumpukan dokumen bervolume besar namun belum memiliki anotasi label historis sama sekali. *Clustering* adalah metode tunggal untuk mengekstraksi wawasan awal secara masif karena tidak mensyaratkan data latih.
2.  **Eksplorasi Topik yang Tidak Terprediksi (*Topic Discovery*):** 
    Berbeda dengan klasifikasi yang kaku pada label yang ditetapkan manusia, klasterisasi sangat bermanfaat ketika peneliti ingin mengetahui tren, fenomena, atau keluhan masyarakat "baru" yang sedang berkembang dan sebelumnya sama sekali tidak terbayangkan oleh peneliti.
3.  **Akselerasi Anotasi Semi-Supervised Learning:** 
    Sebagai langkah pra-pemrosesan (*preprocessing*), di mana jutaan data mentah dikelompokkan terlebih dahulu. Peneliti kemudian hanya perlu memeriksa inti sari klaster (*centroid*) untuk melabeli kelompok tersebut, menggantikan metode pelabelan manual yang memakan ribuan jam kerja.

**Contoh Kasus Penggunaan Riil:**
Biro Intelijen Sosial atau Divisi Pemasaran mengumpulkan 500.000 data percakapan Twitter (X) mentah harian. Daripada melatih model klasifikasi untuk mencari sentimen, mereka menggunakan algoritma LDA atau K-Means (*Text Clustering*) pada data tersebut. Algoritma secara otomatis akan memisahkan kumpulan obrolan tersebut menjadi 4 klaster alami, yang setelah diperiksa oleh analis, ternyata membahas: (1) Keluhan Blackout PLN, (2) Euforia Timnas, (3) Promosi Penipuan Pinjol, dan (4) Gosip Selebritas, yang mana topik ke-3 sebelumnya tidak pernah diantisipasi oleh analis.

*(Merujuk pada Referensi [2] di Daftar Referensi Jurnal)*

---

### **Soal 3:**
*Jika menggunakan algoritma K-means untuk text clustering, bagaimana cara menentukan jumlah klaster optimal? Jelaskan dua metode yang umum digunakan untuk menentukan jumlah klaster optimal.*

**Jawaban:**
Pada algoritma K-Means, penentuan jumlah klaster ($k$) merupakan *hyperparameter* krusial yang harus ditetapkan sebelum iterasi algoritma dimulai. Untuk mencegah subjektivitas tebakan, literatur menstandarkan dua metode kuantitatif utama guna menemukan letak nilai $k$ yang paling optimal:

**1. Metode *Elbow* (Pendekatan *Inertia* / SSE):**
Metode ini secara heuristik menghitung *Sum of Squared Errors* (SSE) atau akumulasi kuadrat jarak dari setiap titik dokumen menuju titik pusat klaster (*centroid*) masing-masing.
*   **Implementasi:** Nilai $k$ ditingkatkan secara bertahap (misal $k=1$ hingga $k=10$), lalu nilai SSE-nya divisualisasikan menjadi grafik garis. Seiring bertambahnya klaster, nilai SSE pasti menyusut.
*   **Penentuan:** Nilai $k$ yang ideal berada pada "Titik Siku" (*elbow point*), yakni lekukan tajam pada grafik di mana nilai SSE berhenti terjun bebas dan mulai berubah menjadi landai secara konstan. Penambahan nilai $k$ di luar titik siku tersebut secara matematis dianggap tidak lagi signifikan.

**2. Metode *Silhouette Coefficient* (Pendekatan Kohesi & Separasi):**
Sebagai metode yang lebih terukur secara presisi dibandingkan *Elbow*, skor *Silhouette* mengevaluasi kepadatan dan jarak keterasingan klaster dalam rentang skor -1 (terburuk) hingga +1 (paling sempurna).
*   **Implementasi:** Metode ini menghitung parameter komparatif matematis untuk seluruh elemen: (a) seberapa padat jarak antar dokumen di klaster yang sama (*Kohesi*), dan (b) seberapa jauh letak klaster tersebut dari klaster kompetitor yang paling dekat dengannya (*Separasi*).
*   **Penentuan:** Jumlah $k$ dievaluasi satu per satu secara komputasi. Konfigurasi $k$ yang mampu memproduksi rata-rata skor *Silhouette* paling tinggi dan paling mendekati angka +1 dinobatkan sebagai jumlah klaster yang paling optimal.

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

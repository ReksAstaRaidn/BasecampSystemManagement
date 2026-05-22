# Sistem Manajemen Basecamp Pendakian

Sistem Manajemen Basecamp Pendakian adalah aplikasi berbasis CLI (Command Line Interface) yang dirancang untuk membantu petugas basecamp dalam mengelola pendaftaran pendaki, mengatur antrian keberangkatan, serta memvisualisasikan jalur pendakian. 

Proyek ini dibuat untuk mengimplementasikan tiga Struktur Data utama secara efisien: **Hash Table**, **Queue (Antrian)**, dan **Graph**.

---

## Fitur Utama

Aplikasi ini menyediakan berbagai fitur manajemen basecamp, antara lain:

* **Peta Jalur Pendakian (Graph):** Merepresentasikan pos-pos pendakian beserta jarak antar pos dalam satuan MDPL (Meter Di atas Permukaan Laut). Jalur dapat ditampilkan dalam format teks biasa atau **Visualisasi Grafis** interaktif.
* **Registrasi Pendaki Tanpa Duplikasi (Hash Table):** Menyimpan data pendaki (ID Tiket, Nama, Kontak Darurat) menggunakan algoritma Hashing. Mencegah pendaftaran ganda secara instan.
* **Manajemen Keberangkatan (Queue):** Mengatur antrian pendaki yang siap diberangkatkan ke jalur pendakian berdasarkan prinsip FIFO (*First In, First Out*).
* **Pencarian Cepat Identitas:** Melakukan verifikasi data pendaki menggunakan ID Tiket dalam waktu singkat berkat efisiensi *Hash Table*.

---

## Struktur Struktur Data & File

Proyek ini dibagi menjadi beberapa modul berbasis objek (OOP) untuk mempermudah pemeliharaan kode:

1.  **`HashDataPendaki.py` (`Class Hash`)**: Menangani penyimpanan data pendaki secara aman menggunakan metode *Separate Chaining* untuk menangani kolisi indeks.
2.  **`QueueAntrianPendaki.py` (`Class Queue`)**: Mengelola antrian masuk dan keluar pendaki di basecamp.
3.  **`GraphJalur.py` (`Class Graph`)**: Memetakan koordinat pos pendakian dan merender visualisasi peta menggunakan bantuan library grafis dengan tambahan kompas penunjuk arah.
4.  **`main.py`**: Berperan sebagai kontroler utama yang menyatukan seluruh modul dan menyediakan antarmuka menu untuk pengguna (petugas).

---

## Prasyarat Sistem

Sebelum menjalankan program, pastikan perangkat Anda telah memenuhi spesifikasi berikut:

* **Python**: Versi 3.x atau yang lebih baru.
* **Library Python**: `graphviz` dan `matplotlib`.

### ⚠️ Catatan Penting Mengenai Graphviz
Agar fitur **Visualisasi Grafis** berjalan dengan lancar, Anda tidak hanya membutuhkan library Python-nya, tetapi juga perangkat lunak (software) Graphviz yang terpasang di sistem operasi Anda.
1. Unduh installer Graphviz dari situs resminya: [Graphviz Downloads](https://graphviz.org/download/).
2. **PENTING:** Saat proses instalasi, pastikan Anda mencentang pilihan **"Add Graphviz to the system PATH"** agar executable Graphviz dapat dikenali oleh Python.

---

## Cara Instalasi & Menjalankan Program

Ikuti langkah-langkah di bawah ini untuk menjalankan program di komputer Anda:

### 1. Clone Repositori
`
git clone 
`

### 2. Masuk ke VSCode dan langsung jalankan Program main nya, atau jalankan di terminal di direktori program nya diletakkan
`
python main.py
`




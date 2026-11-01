# Proyek Akhir Algoritma & Pemrograman - Kalkulator Geometri

Aplikasi berbasis terminal (console) menggunakan Python yang dirancang untuk menghitung luas dan keliling bangun datar secara otomatis serta menyimpan riwayat perhitungannya ke dalam berkas teks.

**Nama:** Rijal munawarudin
**NIM:** 2225250151 
**Kelas:** 3F

---

## 1. Deskripsi Program
Program Kalkulator Geometri Bangun Datar merupakan aplikasi sederhana berbasis CLI (*Command Line Interface*) yang dibuat untuk membantu siswa dan guru sekolah dalam memvalidasi hasil perhitungan matematis bangun datar secara cepat, akurat, dan konsisten.

## 2. Fitur Utama (Kebutuhan Fungsional)
* **F01:** Menghitung Luas dan Keliling Bangun Datar secara instan (Persegi dan Segitiga).
* **F02:** Validasi Input Berlapis (Mencegah input bernilai negatif, nol, atau karakter huruf).
* **F03:** Penyimpanan Otomatis (Menuliskan setiap hasil kalkulasi sukses ke dalam file riwayat teks).

## 3. Spesifikasi Input, Proses, dan Output (IPO)
* **Input:** Pilihan opsi menu utama, nilai dimensi bangun datar (panjang sisi/alas/tinggi).
* **Proses:** Memvalidasi tipe data angka $\rightarrow$ Memproses rumus matematika geometri $\rightarrow$ Memformat hasil keluaran menjadi string terstruktur.
* **Output:** Cetakan hasil kalkulasi waktu nyata (*real-time*) di terminal console dan rekaman data permanen di file `output/riwayat_hitung.txt`.

## 4. Struktur Arsitektur Berkas
Proyek dibangun dengan pendekatan modular terpisah untuk memudahkan perawatan kode:
* `src/main.py` - Mengatur jalannya menu utama dan logika alur aplikasi.
* `src/analisis.py` - Menyimpan fungsi rumus matematika kalkulasi luas & keliling.
* `src/utilitas.py` - Menyimpan fungsi validasi keabsahan data angka.
* `src/data_io.py` - Menangani manajemen tulis dan rekam berkas eksternal.

## 5. Cara Menjalankan Program (Fase Implementasi Pertemuan 15)
1. Buka aplikasi **VS Code** dan jalankan terminal terintegrasi (`Ctrl + ~`).
2. Pastikan interpreter Python 3 Anda sudah aktif.
3. Jalankan aplikasi dengan mengetikkan perintah berikut:
   ```bash
   python src/main.py
   ```
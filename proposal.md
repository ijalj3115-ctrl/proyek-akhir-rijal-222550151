# Proposal Proyek Akhir: Kalkulator Geometri Bangun Datar Berbasis Console
**Mata Kuliah:** Algoritma dan Pemrograman (Pertemuan 14)  
**Program Studi:** S1 Pendidikan Matematika   
**Tahun Ajaran:** 2026/2027 Ganjil  

---

## 1. Judul dan Latar Belakang Masalah
* **Judul:** Kalkulator Geometri Bangun Datar Berbasis Console
* **Latar Belakang:** Siswa seringkali mengalami kesulitan atau ketidaktelitian saat menghitung luas dan keliling bangun datar secara manual. Di sisi lain, guru membutuhkan alat bantu periksa yang cepat. Oleh karena itu, diperlukan sebuah program kalkulator geometri berbasis terminal (console) yang dapat menghitung ukuran bangun datar secara instan, memvalidasi input agar tidak bernilai negatif, dan menyimpan riwayat perhitungan ke dalam file teks.

## 2. Pengguna dan Tujuan
* **Pengguna Utama:** Siswa sekolah dan Guru Matematika.
* **Tujuan:** Membantu memvalidasi hasil perhitungan luas dan keliling bangun datar secara cepat, konsisten, dan akurat.

## 3. Ruang Lingkup & Kebutuhan Proyek
Program ini dibuat menggunakan Python berbasis terminal/console dengan batasan fitur:
* **F01 (Wajib):** Menghitung Luas dan Keliling Bangun Datar (Persegi dan Segitiga).
* **F02 (Wajib):** Memvalidasi input pengguna (panjang sisi tidak boleh <= 0 atau berupa huruf).
* **F03 (Wajib):** Menyimpan riwayat hasil perhitungan ke dalam file teks laporan (`output/riwayat_hitung.txt`).

## 4. Spesifikasi Input, Proses, dan Output (IPO)
* **Input:** Pilihan menu bangun datar, nilai dimensi (panjang sisi/alas/tinggi).
* **Proses:** Validasi nilai input -> Perhitungan rumus geometri -> Pemformatan string teks hasil hitung.
* **Output:** Tampilan hasil perhitungan di layar terminal console dan catatan riwayat di file teks.

## 5. Algoritma (Pseudocode Alur Utama)
```text
MULAI
  Tampilkan menu utama (1. Persegi, 2. Segitiga, 3. Keluar)
  BACA pilihan_menu
  JIKA pilihan_menu == 1 MAKA:
    BACA sisi
    JIKA sisi <= 0 atau bukan angka MAKA:
      Tampilkan "Input tidak valid! Angka harus lebih besar dari 0."
    MELAINKAN:
      luas = sisi * sisi
      keliling = 4 * sisi
      Tampilkan luas dan keliling ke layar terminal
      SIMPAN teks hasil hitung ke 'output/riwayat_hitung.txt'
  SELESAI
```

## 6. Struktur Program dan Modularisasi
Program dibagi menjadi beberapa modul berdasarkan tanggung jawabnya:
* `src/main.py`: Mengatur alur menu utama dan jalannya program.
* `src/data_io.py`: Menangani fungsi pembacaan/penulisan file riwayat.
* `src/analisis.py`: Menghitung rumus matematika geometri (luas dan keliling).
* `src/utilitas.py`: Berisi fungsi validasi input angka.

## 7. Struktur Data yang Digunakan
* **List:** Menyimpan urutan riwayat perhitungan sementara sebelum dituliskan ke file teks.
* **String:** Digunakan untuk memformat teks laporan agar rapi saat disimpan di file.
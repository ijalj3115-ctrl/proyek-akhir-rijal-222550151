# Tabel Test Case Awal - Kalkulator Geometri

| ID | Kategori | Input / Kondisi | Expected Result (Hasil yang Diharapkan) |
|---|---|---|---|
| TC01 | Normal | Menghitung persegi dengan nilai sisi = 5 | Program menampilkan Luas = 25, Keliling = 20 |
| TC02 | Batas | Input dimensi bernilai 0 | Sistem menolak input dengan memunculkan pesan validasi salah |
| TC03 | Invalid | Input dimensi bernilai negatif (misal: -5) | Sistem mendeteksi nilai tidak valid dan meminta input ulang |
| TC04 | Invalid | Input dimensi berupa huruf/teks (misal: "lima") | Mengantisipasi ValueError agar program tidak langsung crash |
| TC05 | Normal | File `riwayat_hitung.txt` belum ada di folder output | Sistem otomatis membuat file teks baru tanpa terjadi error |
from analisis import hitung_luas_persegi, hitung_keliling_persegi
from utilitas import validasi_angka
from data_io import simpan_laporan

def main():
    print("=== KALKULATOR GEOMETRI BANGUN DATAR ===")
    print("1. Hitung Persegi")
    print("2. Keluar")
    
    pilihan = input("Pilih menu (1/2): ")
    
    if pilihan == "1":
        sisi_input = input("Masukkan panjang sisi persegi: ")
        is_valid, hasil_cek = validasi_angka(sisi_input)
        
        if is_valid:
            sisi = hasil_cek
            luas = hitung_luas_persegi(sisi)
            keliling = hitung_keliling_persegi(sisi)
            
            output_teks = f"Persegi [Sisi={sisi}] -> Luas: {luas}, Keliling: {keliling}"
            print(output_teks)
            
            # Simpan ke file teks
            simpan_laporan(output_teks)
        else:
            print(f"Error: {hasil_cek}")
            
    elif pilihan == "2":
        print("Terima kasih!")
    else:
        print("Pilihan menu tidak tersedia.")

if __name__ == "__main__":
    main()
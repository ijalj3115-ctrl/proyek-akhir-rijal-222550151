import os

def simpan_laporan(teks_hasil, path_file="output/riwayat_hitung.txt"):
    """Menulis hasil kalkulasi ke dalam file teks laporan"""
    try:
        # Memastikan folder output tersedia
        os.makedirs(os.path.dirname(path_file), exist_ok=True)
        with open(path_file, "a") as file:
            file.write(teks_hasil + "\n")
        return True
    except Exception as e:
        print(f"Gagal menyimpan laporan: {e}")
        return False
def validasi_angka(nilai_input):
    """Memeriksa apakah input berupa angka valid dan lebih besar dari nol"""
    try:
        angka = float(nilai_input)
        if angka > 0:
            return True, angka
        else:
            return False, "Nilai harus lebih besar dari 0!"
    except ValueError:
        return False, "Input harus berupa angka/bilangan!"
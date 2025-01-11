# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator angka romawi

print('-'*40)
print("\tKALKULATOR ANGKA ROMAWI ")
print('-'*40)

def angka_ke_romawi(angka):
    romawi = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"),
        (1, "I")
    ]
    
    hasil = ""

    for nilai, simbol in romawi:
        while angka >= nilai:
            hasil += simbol
            angka -= nilai
    
    return hasil

def romawi_ke_angka(romawi):
    peta_romawi = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
        "D": 500, "M": 1000
    }
    
    angka = 0
    prev_value = 0

    for simbol in reversed(romawi):
        nilai = peta_romawi[simbol]
        if nilai < prev_value:
            angka -= nilai 
        else:
            angka += nilai
        prev_value = nilai
    
    return angka

def kalkulator_romawi():
    print("=== Kalkulator Angka Romawi ===")
    print("1. Angka ke Romawi")
    print("2. Romawi ke Angka")
    
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1': 
        angka = int(input("Masukkan angka untuk dikonversi: "))
        if angka <= 0:
            print("Angka harus lebih besar dari 0.")
        else:
            hasil = angka_ke_romawi(angka)
            print(f"{angka} dalam angka Romawi adalah {hasil}")
    
    elif pilihan == '2': 
        romawi = input("Masukkan angka Romawi untuk dikonversi: ").upper()
        try:
            hasil = romawi_ke_angka(romawi)
            print(f"{romawi} dalam angka adalah {hasil}")
        except KeyError:
            print("Input Romawi tidak valid.")
    
    else:
        print("Pilihan tidak valid!")

kalkulator_romawi()
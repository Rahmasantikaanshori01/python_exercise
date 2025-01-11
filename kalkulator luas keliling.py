# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator luas-keliling

print('-'*40)
print("\tKALKULATOR LUAS-KELILING ")
print('-'*40)

import math

def kalkulator_luas_keliling():
    print("Pilih bentuk geometri:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Lingkaran")
    print("4. Segitiga")
    
    pilihan = input("Masukkan pilihan (1/2/3/4): ")

    if pilihan == '1':
        sisi = float(input("Masukkan panjang sisi persegi: "))
        luas = sisi ** 2
        keliling = 4 * sisi
        print(f"Luas Persegi: {luas:.2f}")
        print(f"Keliling Persegi: {keliling:.2f}")

    elif pilihan == '2':
        panjang = float(input("Masukkan panjang persegi panjang: "))
        lebar = float(input("Masukkan lebar persegi panjang: "))
        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)
        print(f"Luas Persegi Panjang: {luas:.2f}")
        print(f"Keliling Persegi Panjang: {keliling:.2f}")

    elif pilihan == '3':
        radius = float(input("Masukkan jari-jari lingkaran: "))
        luas = math.pi * radius ** 2
        keliling = 2 * math.pi * radius
        print(f"Luas Lingkaran: {luas:.2f}")
        print(f"Keliling Lingkaran: {keliling:.2f}")

    elif pilihan == '4': 
        alas = float(input("Masukkan panjang alas segitiga: "))
        tinggi = float(input("Masukkan tinggi segitiga: "))
        sisi1 = float(input("Masukkan panjang sisi 1 segitiga: "))
        sisi2 = float(input("Masukkan panjang sisi 2 segitiga: "))
        sisi3 = float(input("Masukkan panjang sisi 3 segitiga: "))
        luas = 0.5 * alas * tinggi
        keliling = sisi1 + sisi2 + sisi3
        print(f"Luas Segitiga: {luas:.2f}")
        print(f"Keliling Segitiga: {keliling:.2f}")

    else:
        print("Pilihan tidak valid!")

kalkulator_luas_keliling()
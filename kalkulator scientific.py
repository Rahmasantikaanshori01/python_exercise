# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator scientific

print('-'*40)
print("\tKALKULATOR SCIENTIFIC")
print('-'*40)

import math

def kalkulator_scientific():
    print("=== Kalkulator Scientific ===")
    print("Operasi yang tersedia:")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pangkat (^)")
    print("6. Akar Kuadrat (sqrt)")
    print("7. Logaritma (log)")
    print("8. Sinus (sin)")
    print("9. Cosinus (cos)")
    print("10. Tangen (tan)")
    print("0. Keluar")
    
    while True:
        pilihan = input("\nPilih operasi (0-10): ")
        
        if pilihan == "0":
            print("Terima kasih telah menggunakan Kalkulator Scientific!")
            break
        
        if pilihan in ["1", "2", "3", "4", "5"]:
            try:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))
                
                if pilihan == "1":
                    print(f"Hasil: {angka1} + {angka2} = {angka1 + angka2}")
                elif pilihan == "2":
                    print(f"Hasil: {angka1} - {angka2} = {angka1 - angka2}")
                elif pilihan == "3":
                    print(f"Hasil: {angka1} * {angka2} = {angka1 * angka2}")
                elif pilihan == "4":
                    if angka2 != 0:
                        print(f"Hasil: {angka1} / {angka2} = {angka1 / angka2}")
                    else:
                        print("Error: Pembagian dengan nol!")
                elif pilihan == "5":
                    print(f"Hasil: {angka1} ^ {angka2} = {angka1 ** angka2}")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        
        elif pilihan == "6":
            try:
                angka = float(input("Masukkan angka: "))
                if angka >= 0:
                    print(f"Hasil: √{angka} = {math.sqrt(angka)}")
                else:
                    print("Error: Tidak dapat menghitung akar kuadrat dari bilangan negatif!")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        
        elif pilihan == "7":
            try:
                angka = float(input("Masukkan angka (lebih besar dari 0): "))
                if angka > 0:
                    print(f"Hasil: log({angka}) = {math.log(angka)}")
                else:
                    print("Error: Masukkan angka lebih besar dari 0!")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        
        elif pilihan in ["8", "9", "10"]:
            try:
                sudut = float(input("Masukkan sudut (dalam derajat): "))
                radian = math.radians(sudut)
                
                if pilihan == "8":
                    print(f"Hasil: sin({sudut}°) = {math.sin(radian)}")
                elif pilihan == "9":
                    print(f"Hasil: cos({sudut}°) = {math.cos(radian)}")
                elif pilihan == "10":
                    print(f"Hasil: tan({sudut}°) = {math.tan(radian)}")
            except ValueError:
                print("Error: Masukkan angka yang valid!")
        
        else:
            print("Pilihan tidak valid, silakan pilih kembali.")

kalkulator_scientific()
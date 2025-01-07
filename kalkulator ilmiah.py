# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program kalkulator ilmiah

import math

def tampilkan_menu():
    print("Kalkulator Ilmiah")
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Pangkat")
    print("6. Akar Kuadrat")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Logaritma (log base 10)")
    print("11. Sinus Invers (asin)")
    print("12. Cosinus Invers (acos)")
    print("13. Keluar")

def kalkulator():
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Masukkan pilihan: "))
            
            if pilihan == 13:
                print("Terima kasih! Keluar dari program.")
                break

            if pilihan in [1, 2, 3, 4, 5]:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua: "))

                if pilihan == 1:
                    print(f"Hasil: {angka1 + angka2}")
                elif pilihan == 2:
                    print(f"Hasil: {angka1 - angka2}")
                elif pilihan == 3:
                    print(f"Hasil: {angka1 * angka2}")
                elif pilihan == 4:
                    if angka2 != 0:
                        print(f"Hasil: {angka1 / angka2}")
                    else:
                        print("Error: Pembagian dengan 0 tidak diperbolehkan.")
                elif pilihan == 5:
                    print(f"Hasil: {angka1 ** angka2}")
            
            elif pilihan == 6:
                angka = float(input("Masukkan angka untuk akar kuadrat: "))
                if angka < 0:
                    print("Error: Tidak dapat mengambil akar kuadrat dari angka negatif.")
                else:
                    print(f"Hasil: {math.sqrt(angka)}")
            
            elif pilihan == 7:
                angka = float(input("Masukkan sudut dalam derajat untuk sin: "))
                print(f"Hasil: {math.sin(math.radians(angka))}")
            
            elif pilihan == 8:
                angka = float(input("Masukkan sudut dalam derajat untuk cos: "))
                print(f"Hasil: {math.cos(math.radians(angka))}")
            
            elif pilihan == 9:
                angka = float(input("Masukkan sudut dalam derajat untuk tan: "))
                print(f"Hasil: {math.tan(math.radians(angka))}")
            
            elif pilihan == 10:
                angka = float(input("Masukkan angka untuk logaritma (base 10): "))
                if angka <= 0:
                    print("Error: Logaritma hanya dapat dihitung untuk angka positif.")
                else:
                    print(f"Hasil: {math.log10(angka)}")
            
            elif pilihan == 11:
                angka = float(input("Masukkan nilai untuk sinus invers (asin): "))
                if -1 <= angka <= 1:
                    print(f"Hasil: {math.degrees(math.asin(angka))} derajat")
                else:
                    print("Error: Nilai harus berada di antara -1 dan 1.")
            
            elif pilihan == 12:
                angka = float(input("Masukkan nilai untuk cosinus invers (acos): "))
                if -1 <= angka <= 1:
                    print(f"Hasil: {math.degrees(math.acos(angka))} derajat")
                else:
                    print("Error: Nilai harus berada di antara -1 dan 1.")
            else:
                print("Pilihan tidak valid. Coba lagi.")
        
        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")
kalkulator()
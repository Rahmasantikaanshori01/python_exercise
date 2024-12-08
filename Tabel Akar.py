# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program tabel akar

import math

def tabel_akar():
    print('-' * 40)
    print("\tProgram Tabel Akar")
    print('-' * 40)
    # Input dari pengguna
    try:
        max_number = int(input("Masukkan angka maksimum: "))
        if max_number < 1:
            print("Harap masukkan angka lebih besar dari 0.")
            return
        
        # Membuat tabel
        print("\nTabel Akar:")
        print(f"{'Angka':<10}{'Akar Kuadrat':<15}{'Akar Pangkat Tiga':<15}")
        print("-" * 40)
        
        for i in range(1, max_number + 1):
            akar_kuadrat = math.sqrt(i)
            akar_pangkat_tiga = i ** (1/3)
            print(f"{i:<10}{akar_kuadrat:<15.6f}{akar_pangkat_tiga:<15.6f}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")

# Menjalankan fungsi
tabel_akar()
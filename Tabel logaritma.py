# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program tabel logaritma

import math

def tabel_logaritma():
    print('*'*40)
    print("\tTabel Logaritma")
    print('*'*40)
    
    try:
        # Meminta input angka maksimum dari pengguna
        max_number = int(input("Masukkan angka maksimum: "))
        
        if max_number < 1:
            print("Harap masukkan angka lebih besar dari 0.")
            return

        # Membuat tabel
        print("\nTabel Logaritma:")
        print(f"{'Angka':<10}{'Logaritma (basis 10)':<20}{'Logaritma (basis e)':<20}")
        print("-" * 50)
        
        for i in range(1, max_number + 1):
            log_basis_10 = math.log10(i)
            log_basis_e = math.log(i)
            print(f"{i:<10}{log_basis_10:<20.6f}{log_basis_e:<20.6f}")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")

# Menjalankan fungsi
tabel_logaritma()
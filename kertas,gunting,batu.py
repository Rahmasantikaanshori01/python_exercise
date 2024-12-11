# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 Desember 2024
# program game kertas gunting batu

print('*' * 20)
print('\tGAME')
print('*' * 20)

import random

def permainan_batu_gunting_kertas():
    pilihan = ['Batu', 'Gunting', 'Kertas']
    
    while True:
        pemain = input("Pilih Batu, Gunting, atau Kertas: ").capitalize()  # Mengubah input menjadi format huruf kapital
        
        if pemain not in pilihan:  # Memeriksa apakah input valid
            print("Input tidak valid. Silakan pilih Batu, Gunting, atau Kertas.")
            continue  # Minta input lagi jika tidak valid
        
        komputer = random.choice(pilihan)
        
        if pemain == komputer:
            print(f"Seri! Anda dan komputer sama-sama memilih {pemain}.")
        elif (pemain == 'Batu' and komputer == 'Gunting') or (pemain == 'Gunting' and komputer == 'Kertas') or (pemain == 'Kertas' and komputer == 'Batu'):
            print(f"Anda menang! Anda memilih {pemain}, komputer memilih {komputer}.")
        else:
            print(f"Anda kalah! Komputer memilih {komputer}, Anda memilih {pemain}.")
        break  # Keluar dari loop setelah permainan selesai

permainan_batu_gunting_kertas()
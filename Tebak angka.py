# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program tebak angka

import random

def tebak_angka():
    print('*'*40)
    print("\tGame Tebak Angka")
    print('*'*40)
    print("Saya sudah memilih angka antara 1 sampai 100. Coba tebak!")
    
    # Menghasilkan angka acak
    angka_rahasia = random.randint(1, 100)
    percobaan = 0

    while True:
        try:
            tebakan = input("Masukkan tebakan Anda (atau ketik 'q' untuk keluar): ")
            
            # Keluar dari permainan
            if tebakan.lower() == 'q':
                print(f"Anda menyerah! Angka rahasia adalah {angka_rahasia}.")
                break

            tebakan = int(tebakan)
            percobaan += 1

            # Memeriksa tebakan
            if tebakan < angka_rahasia:
                print("Terlalu kecil!")
            elif tebakan > angka_rahasia:
                print("Terlalu besar!")
            else:
                print(f"Selamat! Anda menebak angka {angka_rahasia} dengan benar dalam {percobaan} percobaan.")
                break
        except ValueError:
            print("Harap masukkan angka yang valid atau 'q' untuk keluar.")

# Menjalankan game
tebak_angka()
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 Desember 2024
# program gulung dadu

print('*' * 30)
print('\tGULUNG DADU')
print('*' * 30)
import random

def gulung_dadu():
    print("=== Simulasi Menggulung Dadu ===")

    while True:
        input("Tekan Enter untuk menggulung dadu...")
        hasil = random.randint(1, 6)
        print(f"Anda mendapatkan angka: {hasil}")

        lagi = input("Ingin menggulung lagi? (y/n): ").lower()
        if lagi != 'y':
            print("Terima kasih telah bermain!")
            break

gulung_dadu()
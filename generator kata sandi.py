# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program generator kata sandi

import random
import string

def generate_password(length=12):
    """Fungsi untuk membuat kata sandi acak."""
   
    characters = string.ascii_letters + string.digits + string.punctuation
   
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Selamat datang di Generator Kata Sandi!")
    while True:
        try:
            
            length = int(input("Masukkan panjang kata sandi yang diinginkan (minimal 8): "))
            if length < 8:
                print("Panjang kata sandi harus minimal 8 karakter.")
                continue
            
            password = generate_password(length)
            print(f"Kata sandi Anda: {password}")
            
            ulang = input("Ingin membuat kata sandi lain? (y/n): ").lower()
            if ulang != 'y':
                print("Terima kasih telah menggunakan Generator Kata Sandi!")
                break
        except ValueError:
            print("Masukkan angka yang valid.")

main()
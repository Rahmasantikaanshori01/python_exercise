# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program generator password

print('-'*40)
print("\tGENERATOR PASSWORD")
print('-'*40)

import random
import string

panjang = int(input("Masukkan panjang password: "))
password = ''.join(random.choices(string.ascii_letters + string.digits, k=panjang))
print(f"Password Anda: {password}")
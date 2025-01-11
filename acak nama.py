# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program acak nama

print('-'*40)
print("\tACAK NAMA")
print('-'*40)

import random

nama_depan = ["Callisa", "Cantika", "Citra", "Dewi", "alvi", "Renata"]
nama_belakang = ["Saputri", "Khori", "Jayana", "Putri", "Harika", "Adrian"]

nama = random.choice(nama_depan) + " " + random.choice(nama_belakang)
print(f"Nama acak:{nama}")
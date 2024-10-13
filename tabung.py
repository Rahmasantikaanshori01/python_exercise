# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 10 oktober 2024
# program tabung

print('=' * 40)
print('RUMUS TABUNG')
print('=' * 40)

r = int(input("masukkan jari2 (r): "))
t = int(input("massukan tinggi tabung (t): "))

volume = r ** 2 * t
luas_permukaan = 2 * r * (r + t)

print("Volume tabung: ", volume, "m3")
print("Luas permukaan tabung: ", luas_permukaan, "m2")
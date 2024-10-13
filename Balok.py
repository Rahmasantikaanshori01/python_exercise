# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 13 oktober 2024
# program balok

print('=' * 40)
print('RUMUS BALOK')
print('=' * 40)

panjang = int(input("masukkan panjang (p): "))
lebar = int(input("masukkan lebar (l): "))
tinggi = int(input("masukkan tinggi (t): "))

luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
volume = panjang * lebar * tinggi

print("Luas permukaan balok: ", luas_permukaan, "m2")
print("Volume: ", volume, "m3")
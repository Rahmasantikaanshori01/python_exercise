# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 oktober 2024
# program kerucut

print('=' * 40)
print('PROGRAM KERUCUT')
print('=' * 40)

r = int(input("masukkan jari2 (r): "))
t = int(input("massukan tinggi kerucut (t): "))

volume = (1/3)
s = (r**2 + t**2)

luas_permukaan = r * (r + s)

print("Volume kerucut: ", volume, "m3")
print("Luas permukaan kerucut: ", luas_permukaan, "m2")
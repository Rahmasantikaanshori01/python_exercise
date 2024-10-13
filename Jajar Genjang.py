# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 oktober 2024
# program jajar genjang

print('=' * 40)
print('RUMUS JAJAR GENJANG')
print('=' * 40)

alas = int(input("masukkan alas (a): "))
tinggi = int(input("masukkan tinggi (t): "))
sisi_miring = int(input("masukkan sisi miring (s): "))

luas = alas * tinggi
keliling = 2 * (alas + sisi_miring)

print("Luas jaja genjang: ", luas, "m2")
print("Keliling jajar genjang: ", keliling, "m")
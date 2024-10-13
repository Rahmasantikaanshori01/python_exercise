# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 12 oktober 2024
# program trapesium

print('=' * 40)
print('RUMUS TRAPESIUM')
print('=' * 40)

sisi_atas = int(input("masukkan sisi atas (a): "))
sisi_bawah = int(input("masukkan sisi bawah (b): "))
tinggi = int(input("masukkan tinggi (t): "))
sisi_miring = int(input("masukkan sisi miring (s): "))

luas = 0,5 * (sisi_atas + sisi_bawah) * tinggi
keliling = sisi_atas + sisi_bawah + 2 * sisi_miring

print("Luas trapesium: ", luas, "m2")
print("Keliling trapesium: ", keliling, "m")
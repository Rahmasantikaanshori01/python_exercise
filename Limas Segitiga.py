# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 13 oktober 2024
# program limas segitiga

print('=' * 40)
print('RUMUS LIMAS SEGITIGA')
print('=' * 40)

alas = int(input("masukkan panjang alas segitiga (a): "))
tinggi_segitiga = int(input("masukkan tinggi segitiga (t): "))
tinggi_limas = int(input("masukkan tinggi limas (T): "))

luas_alas = 0.5 * alas * tinggi_segitiga
volume = (1/3) * luas_alas * tinggi_limas

print("Luas alas segitiga: ", luas_alas, "m2")
print("Volume limas segitiga: ", volume, "m3")
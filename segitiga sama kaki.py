# Dibuat oleh : Rahma Santika Al Anshori
# Tanggal pengerjaan : 7 November 2024
# Program segitiga sama kaki

print('-' * 40)
print("RUMUS SEGITIGA SAMA KAKI")
print('-' * 40)

alas = int(input('alas: '))
sisi_sama = int(input('sisi sama: '))

tinggi = (sisi_sama*2 - (alas / 2)*2)
luas = (alas * tinggi) / 2
keliling = alas + 2 * sisi_sama

print('Luas =', luas, "m2")
print('Keliling =',keliling,"m")
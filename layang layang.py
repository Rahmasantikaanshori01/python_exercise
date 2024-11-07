# Dibuat oleh : Rahma Santika Al Anshori
# Tanggal pengerjaan : 7 November 2024
# Program layang layang

print('-' * 40)
print("RUMUS LAYANG LAYANG")
print('-' * 40)

diagonal1 = int(input('Diagonal 1: '))
diagonal2 = int(input('Diagonal 2: '))
sisi1 = int(input('Sisi 1: '))
sisi2 = int(input('Sisi 2: '))

luas = (diagonal1 * diagonal2) / 2
keliling = 2 * (sisi1 + sisi2)

print('Luas =', luas, "m2")
print('Keliling =', keliling, "m")
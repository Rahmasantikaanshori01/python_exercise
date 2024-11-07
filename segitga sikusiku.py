# Dibuat oleh : Rahma Santika Al Anshori
# Tanggal pengerjaan : 7 November 2024
# Program segitiga siku-siku

print('-' * 40)
print("RUMUS SEGITIGA SIKU-SIKU")
print('-' * 40)

alas = int(input('alas: '))
tinggi = int(input('tinggi: '))
sisi_miring = (alas*2 + tinggi*2)  
luas = (alas * tinggi) / 2
keliling = alas + tinggi + sisi_miring

print('Luas =', luas, "m2")
print('Keliling =',keliling,"m")
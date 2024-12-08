# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program segitiga bintang terbalik

print('=' * 40)
print('\tSEGITIGA TERBALIK')
print('=' * 40)

def segitiga_terbalik():
    tinggi = int(input("Masukkan tinggi segitiga terbalik: "))
    
    for i in range(tinggi, 0, -1):
        print('*' * i)

segitiga_terbalik()
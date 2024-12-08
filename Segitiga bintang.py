# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program segitiga bintang

print('-' * 40)
print("\tKonversi Suhu")
print('-' * 40)

def segitiga_bintang():
  
    tinggi = int(input("Masukkan tinggi segitiga: "))
    
    for i in range(1, tinggi + 1):
      
        print('*' * i)

segitiga_bintang()
# dibuat oleh : Rahma Santika Al Anshori
# tanggal di buat : 08 Desember 2024
# program tabel pembagian

print('-' * 40)
print("\tTABEL PEMBAGIAN")
print('-' * 40)

def tabel_pembagian(angka):
    for i in range(1, 11):
        print(f"{angka} ÷ {i} = {angka / i}")

# Input dan output
angka = int(input("Masukkan angka untuk tabel pembagian: "))
tabel_pembagian(angka)
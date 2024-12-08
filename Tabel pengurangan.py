# dibuat oleh : Rahma Santika Al Anshori
# tanggal di buat : 08 Desember 2024
# program tabel pengurangan

print('-' * 40)
print("\tTABEL PENGURANGAN")
print('-' * 40)

def tabel_pengurangan(angka):
    for i in range(1, 11):
        print(f"{angka} - {i} = {angka - i}")

angka = int(input("Masukkan angka untuk tabel pengurangan: "))
tabel_pengurangan(angka)
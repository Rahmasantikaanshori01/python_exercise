# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program konversi mata uang

print('=' * 40)
print('\tKONVERSI MATA UANG')
print('=' * 40)

def konversi_mata_uang():
    rupiah = float(input("Masukkan jumlah uang dalam Rupiah: "))
    kurs = 0.067  # 1 Rupiah = 0.067 Dolar AS
    dolar = rupiah * kurs
    print(f"{rupiah} Rupiah = {dolar:.2f} Dolar AS")

# Menjalankan program konversi mata uang
konversi_mata_uang()

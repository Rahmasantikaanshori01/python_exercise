# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program pembalik kata

print('=' * 40)
print('\tPEMBALIK KATA')
print('=' * 40)

def balik_kata():
    kata = input("Masukkan kata untuk dibalik: ")
    print(f"Kata setelah dibalik: {kata[::-1]}")

balik_kata()
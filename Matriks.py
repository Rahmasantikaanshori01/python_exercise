# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program martiks

print('=' * 40)
print('\tPROGRAM MARTIKS')
print('=' * 40)

def matriks_identitas(n):
    for i in range(n):
        for j in range(n):
            print(1 if i == j else 0, end=" ")
        print()

# Input dan output
n = int(input("Masukkan ukuran matriks: "))
matriks_identitas(n)
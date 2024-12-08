# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program fibonacci

print('=' * 40)
print('\tPROGRAM FIBONACCI')
print('=' * 40)

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Input dan output
n = int(input("Masukkan jumlah bilangan Fibonacci yang ingin ditampilkan: "))
fibonacci(n)
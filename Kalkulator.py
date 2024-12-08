# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program kalkulator

def kalkulator():
    print('*'*40)
    print("\tKalkulator Sederhana")
    print('*'*40)
    try:
        a = float(input("Masukkan angka pertama: "))
        b = float(input("Masukkan angka kedua: "))
        operasi = input("Pilih operasi (+, -, *, /): ")
        
        if operasi == '+':
            print(f"Hasil: {a + b}")
        elif operasi == '-':
            print(f"Hasil: {a - b}")
        elif operasi == '*':
            print(f"Hasil: {a * b}")
        elif operasi == '/':
            if b != 0:
                print(f"Hasil: {a / b}")
            else:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
        else:
            print("Operasi tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

kalkulator()
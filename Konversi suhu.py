# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program konversi suhu

def konversi_suhu():
    print('-' * 40)
    print("\tKonversi Suhu")
    print('-' * 40)
    try:
        celsius = float(input("Masukkan suhu dalam Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Suhu dalam Fahrenheit: {fahrenheit:.2f}°F")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

konversi_suhu()

# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator kecepatan

print('-'*40)
print("\tKALKULATOR KECEPATAN ")
print('-'*40)

def kalkulator_kecepatan():
    print("Pilih satuan untuk jarak dan waktu:")
    print("1. Meter dan Detik")
    print("2. Kilometer dan Jam")
    
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1':
        jarak = float(input("Masukkan jarak (dalam meter): "))
        waktu = float(input("Masukkan waktu (dalam detik): "))
        kecepatan = jarak / waktu
        print(f"Kecepatan: {kecepatan:.2f} meter/detik")
    
    elif pilihan == '2':
        jarak = float(input("Masukkan jarak (dalam kilometer): "))
        waktu = float(input("Masukkan waktu (dalam jam): "))
        kecepatan = jarak / waktu
        print(f"Kecepatan: {kecepatan:.2f} kilometer/jam")
    
    else:
        print("Pilihan tidak valid!")

kalkulator_kecepatan()
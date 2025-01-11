# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator jarak

print('-'*40)
print("\tKALKULATOR JARAK")
print('-'*40)

def kalkulator_jarak():
    print("Pilih satuan untuk kecepatan dan waktu:")
    print("1. Meter per detik dan Detik")
    print("2. Kilometer per jam dan Jam")
    
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == '1': 
        kecepatan = float(input("Masukkan kecepatan (dalam meter per detik): "))
        waktu = float(input("Masukkan waktu (dalam detik): "))
        jarak = kecepatan * waktu
        print(f"Jarak: {jarak:.2f} meter")
    
    elif pilihan == '2': 
        kecepatan = float(input("Masukkan kecepatan (dalam kilometer per jam): "))
        waktu = float(input("Masukkan waktu (dalam jam): "))
        jarak = kecepatan * waktu
        print(f"Jarak: {jarak:.2f} kilometer")
    
    else:
        print("Pilihan tidak valid!")

kalkulator_jarak()
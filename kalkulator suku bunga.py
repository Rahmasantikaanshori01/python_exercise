# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator suku bunga

print('-'*40)
print("\tKALKULATOR SUKU BUNGA")
print('-'*40)

def bunga_sederhana(principal, suku_bunga, waktu):
    return principal * suku_bunga * waktu / 100

def bunga_majemuk(principal, suku_bunga, waktu, frekuensi):
    return principal * (1 + suku_bunga / (100 * frekuensi)) ** (frekuensi * waktu) - principal

def kalkulator_suku_bunga():
    print("=== Kalkulator Suku Bunga ===")
    print("1. Bunga Sederhana")
    print("2. Bunga Majemuk")
    pilihan = input("Pilih tipe bunga (1/2): ")

    if pilihan == "1":
        principal = float(input("Masukkan jumlah pokok (Principal): "))
        suku_bunga = float(input("Masukkan suku bunga tahunan (%): "))
        waktu = float(input("Masukkan waktu (tahun): "))
        
        bunga = bunga_sederhana(principal, suku_bunga, waktu)
        total = principal + bunga
        
        print(f"\nBunga Sederhana: {bunga}")
        print(f"Total uang setelah {waktu} tahun: {total}")
    
    elif pilihan == "2":
        principal = float(input("Masukkan jumlah pokok (Principal): "))
        suku_bunga = float(input("Masukkan suku bunga tahunan (%): "))
        waktu = float(input("Masukkan waktu (tahun): "))
        frekuensi = float(input("Masukkan frekuensi per tahun (contoh: 4 untuk kuartalan): "))
        
        bunga = bunga_majemuk(principal, suku_bunga, waktu, frekuensi)
        total = principal + bunga
        
        print(f"\nBunga Majemuk: {bunga}")
        print(f"Total uang setelah {waktu} tahun: {total}")
    
    else:
        print("Pilihan tidak valid. Program selesai.")

kalkulator_suku_bunga()
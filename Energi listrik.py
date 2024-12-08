# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program menghitung energi listrik

def hitung_energi_listrik():
    print('-' * 40)
    print("\tMenghitung Energi Listrik")
    print('-' * 40)
    
    # Input daya listrik (P) dan waktu (t)
    daya = float(input("Masukkan daya listrik (dalam watt): "))
    waktu = float(input("Masukkan waktu penggunaan (dalam jam): "))
    
    # Menghitung energi listrik
    energi = daya * waktu
    
    # Menampilkan hasil
    print(f"\nEnergi listrik yang digunakan: {energi} watt-jam")
    print(f"Atau setara dengan: {energi / 1000} kWh (kilowatt-jam)")

# Memanggil fungsi
hitung_energi_listrik()
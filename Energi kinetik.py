# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program menghitung energi kinetik

def hitung_energi_kinetik():
    print('-' * 40)
    print("\tMenghitung Energi Kinetik")
    print('-' * 40)
    
    # Input massa (m) dan kecepatan (v)
    massa = float(input("Masukkan massa benda (dalam kilogram): "))
    kecepatan = float(input("Masukkan kecepatan benda (dalam meter per detik): "))
    
    # Menghitung energi kinetik
    energi_kinetik = 0.5 * massa * kecepatan**2
    
    # Menampilkan hasil
    print(f"\nEnergi kinetik benda: {energi_kinetik:.2f} joule")

hitung_energi_kinetik()

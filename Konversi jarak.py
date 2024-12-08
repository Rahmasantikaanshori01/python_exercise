# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program konversi jarak

def konversi_jarak():
    print('-' * 40)
    print("\tProgram Konversi Jarak")
    print('-' * 40)
    
    try:
        # Meminta input jarak dalam kilometer
        kilometer = float(input("Masukkan jarak dalam kilometer: "))
        
        if kilometer < 0:
            print("Harap masukkan nilai positif.")
            return

        # Menghitung konversi
        meter = kilometer * 1000
        mil = kilometer * 0.621371
        yard = kilometer * 1093.61

        # Menampilkan hasil konversi
        print(f"\nHasil Konversi:")
        print(f"{kilometer} kilometer = {meter:.2f} meter")
        print(f"{kilometer} kilometer = {mil:.2f} mil")
        print(f"{kilometer} kilometer = {yard:.2f} yard")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# Menjalankan fungsi
konversi_jarak()
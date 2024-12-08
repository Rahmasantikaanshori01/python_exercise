# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program konversi waktu

def konversi_waktu():
    print('-' * 40)
    print("\tProgram Konversi Waktu")
    print('-' * 40)
    
    try:
        # Input jumlah detik dari pengguna
        total_detik = int(input("Masukkan jumlah detik: "))
        
        if total_detik < 0:
            print("Harap masukkan angka positif.")
            return

        # Menghitung jam, menit, dan detik
        jam = total_detik // 3600
        sisa_detik = total_detik % 3600
        menit = sisa_detik // 60
        detik = sisa_detik % 60

        # Menampilkan hasil konversi
        print(f"\nHasil Konversi:")
        print(f"{total_detik} detik = {jam} jam, {menit} menit, dan {detik} detik.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka bulat.")

# Menjalankan fungsi
konversi_waktu()
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program penjadwalan

def jadwal_tugas():
    # Menyusun daftar hari dalam seminggu
    hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
    
    # Membuat dictionary untuk menyimpan tugas per hari
    jadwal = {}

    print('-' * 40)
    print("\tProgram Penjadwalan Tugas")
    print('-' * 40)

    # Meminta input tugas untuk setiap hari dalam minggu
    for h in hari:
        tugas = input(f"Tugas untuk {h}: ")
        jadwal[h] = tugas
    
    # Menampilkan jadwal yang telah dimasukkan
    print("\nJadwal Tugas Anda:")
    for h in hari:
        print(f"{h}: {jadwal[h]}")

# Menjalankan fungsi
jadwal_tugas()
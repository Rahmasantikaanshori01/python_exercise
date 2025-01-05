# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 05 januari 2025
# program pencatat keuangan

import os
import datetime

# Nama file untuk menyimpan data keuangan
file_name = "data_keuangan.txt"

def tambah_catatan():
    """Menambahkan catatan pemasukan atau pengeluaran."""
    print("\n=== Tambah Catatan Pemasukan/Pengeluaran ===")
    jenis = input("Masukkan jenis (pemasukan/pengeluaran): ").lower()
    if jenis not in ['pemasukan', 'pengeluaran']:
        print("Jenis tidak valid! Masukkan 'pemasukan' atau 'pengeluaran'.")
        return
    
    try:
        jumlah = float(input("Masukkan jumlah uang: Rp "))
    except ValueError:
        print("Masukkan jumlah uang yang valid!")
        return

    # Mendapatkan tanggal hari ini
    tanggal = datetime.date.today().strftime("%Y-%m-%d")

    # Menyimpan data ke file
    with open(file_name, "a") as file:
        file.write(f"{tanggal} - {jenis} - Rp {jumlah:.2f}\n")
    
    print(f"Catatan {jenis} berhasil ditambahkan.")

def hitung_saldo():
    """Menghitung saldo akhir berdasarkan pemasukan dan pengeluaran."""
    saldo = 0
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(" - ")
                jenis = data[1]
                jumlah = float(data[2][3:])  # Mengambil nilai uang setelah 'Rp'
                if jenis == "pemasukan":
                    saldo += jumlah
                else:
                    saldo -= jumlah
    return saldo

def tampilkan_laporan_bulanan():
    """Menampilkan laporan pemasukan dan pengeluaran bulanan."""
    bulan_ini = datetime.date.today().strftime("%Y-%m")
    laporan_pemasukan = 0
    laporan_pengeluaran = 0

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split(" - ")
                tanggal = data[0]
                jenis = data[1]
                jumlah = float(data[2][3:])
                if tanggal.startswith(bulan_ini):
                    if jenis == "pemasukan":
                        laporan_pemasukan += jumlah
                    elif jenis == "pengeluaran":
                        laporan_pengeluaran += jumlah

    print(f"\n=== Laporan Keuangan Bulan {bulan_ini} ===")
    print(f"Pemasukan Bulanan: Rp {laporan_pemasukan:.2f}")
    print(f"Pengeluaran Bulanan: Rp {laporan_pengeluaran:.2f}")
    print(f"Saldo Akhir Bulan: Rp {laporan_pemasukan - laporan_pengeluaran:.2f}")

def menu():
    """Menampilkan menu utama aplikasi."""
    while True:
        print("\n=== Aplikasi Pencatat Keuangan Sederhana ===")
        print("1. Tambah Catatan Pemasukan/Pengeluaran")
        print("2. Hitung Saldo Akhir")
        print("3. Tampilkan Laporan Bulanan")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == "1":
            tambah_catatan()
        elif pilihan == "2":
            saldo = hitung_saldo()
            print(f"Saldo Akhir: Rp {saldo:.2f}")
        elif pilihan == "3":
            tampilkan_laporan_bulanan()
        elif pilihan == "4":
            print("Terima kasih telah menggunakan Aplikasi Pencatat Keuangan!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()
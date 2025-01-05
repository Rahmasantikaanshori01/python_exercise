# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 05 januari 2025
# program catatan harian

import os

# Nama file untuk menyimpan catatan
file_name = "catatan_harian.txt"

def tambah_catatan():
    """Menambahkan catatan baru ke file."""
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    isi_catatan = input("Masukkan isi catatan: ")

    with open(file_name, "a") as file:
        file.write(f"{tanggal} - {isi_catatan}\n")
    print("Catatan berhasil disimpan.")

def tampilkan_catatan():
    """Menampilkan semua catatan yang tersimpan."""
    if not os.path.exists(file_name):
        print("Belum ada catatan yang tersimpan.")
        return

    print("\n=== Semua Catatan ===")
    with open(file_name, "r") as file:
        catatan = file.readlines()
        if not catatan:
            print("Belum ada catatan yang tersimpan.")
        else:
            for idx, entry in enumerate(catatan, 1):
                print(f"{idx}. {entry.strip()}")

def menu():
    """Menampilkan menu utama aplikasi."""
    while True:
        print("\n=== Aplikasi Catatan Harian ===")
        print("1. Tambah Catatan Baru")
        print("2. Tampilkan Semua Catatan")
        print("3. Keluar")
        
        pilihan = input("Pilih opsi (1/2/3): ")
        
        if pilihan == "1":
            tambah_catatan()
        elif pilihan == "2":
            tampilkan_catatan()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan aplikasi Catatan Harian!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")

menu()
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalender pengingat

print('-'*40)
print("\tKALENDER PENGINGAT")
print('-'*40)

import calendar
import json
from datetime import date

FILE_PENGINGAT = "pengingat.json"

def muat_pengingat():
    try:
        with open(FILE_PENGINGAT, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def simpan_pengingat(pengingat):
    with open(FILE_PENGINGAT, "w") as file:
        json.dump(pengingat, file)

def tampilkan_kalender(tahun, bulan):
    print("\n" + calendar.month(tahun, bulan))

def tambah_pengingat(pengingat):
    tanggal = input("Masukkan tanggal pengingat (YYYY-MM-DD): ")
    pesan = input("Masukkan pesan pengingat: ")
    if tanggal in pengingat:
        pengingat[tanggal].append(pesan)
    else:
        pengingat[tanggal] = [pesan]
    simpan_pengingat(pengingat)
    print(f"Pengingat ditambahkan untuk {tanggal}.")

def lihat_pengingat(pengingat):
    tanggal = input("Masukkan tanggal untuk melihat pengingat (YYYY-MM-DD): ")
    if tanggal in pengingat:
        print(f"Pengingat untuk {tanggal}:")
        for i, pesan in enumerate(pengingat[tanggal], start=1):
            print(f"{i}. {pesan}")
    else:
        print("Tidak ada pengingat untuk tanggal ini.")

def kalender_dengan_pengingat():
    pengingat = muat_pengingat()
    print("=== Kalender dengan Pengingat ===")
    while True:
        print("\nMenu:")
        print("1. Tampilkan kalender")
        print("2. Tambah pengingat")
        print("3. Lihat pengingat")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == "1":
            tahun = int(input("Masukkan tahun: "))
            bulan = int(input("Masukkan bulan (1-12): "))
            tampilkan_kalender(tahun, bulan)
        elif pilihan == "2":
            tambah_pengingat(pengingat)
        elif pilihan == "3":
            lihat_pengingat(pengingat)
        elif pilihan == "4":
            print("Terima kasih telah menggunakan kalender pengingat!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

kalender_dengan_pengingat()
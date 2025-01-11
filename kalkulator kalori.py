# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator kalori

print('-'*40)
print("\tKALKULATOR KALORI")
print('-'*40)

def tambah_makanan(makanan, kalori, daftar_kalori):
    daftar_kalori[makanan] = kalori
    print(f"{makanan} dengan {kalori} kalori telah ditambahkan.")

def hitung_total_kalori(daftar_kalori):
    return sum(daftar_kalori.values())

def tampilkan_makanan(daftar_kalori):
    if not daftar_kalori:
        print("Belum ada makanan yang dimasukkan.")
    else:
        print("\nDaftar Makanan:")
        for makanan, kalori in daftar_kalori.items():
            print(f"- {makanan}: {kalori} kalori")
        print(f"Total Kalori: {hitung_total_kalori(daftar_kalori)} kalori")

def kalkulator_kalori():
    daftar_kalori = {}
    print("=== Kalkulator Kalori ===")
    while True:
        print("\nMenu:")
        print("1. Tambah makanan")
        print("2. Tampilkan daftar makanan")
        print("3. Hitung total kalori")
        print("4. Keluar")
        pilihan = input("Pilih opsi (1-4): ")

        if pilihan == "1":
            makanan = input("Masukkan nama makanan: ")
            try:
                kalori = int(input("Masukkan jumlah kalori: "))
                tambah_makanan(makanan, kalori, daftar_kalori)
            except ValueError:
                print("Masukkan jumlah kalori dalam angka.")
        elif pilihan == "2":
            tampilkan_makanan(daftar_kalori)
        elif pilihan == "3":
            total = hitung_total_kalori(daftar_kalori)
            print(f"Total kalori saat ini: {total} kalori")
        elif pilihan == "4":
            print("Terima kasih telah menggunakan kalkulator kalori!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

kalkulator_kalori()
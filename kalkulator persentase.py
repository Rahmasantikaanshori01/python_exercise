# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program kalkulator persentase

def hitung_persentase(nilai, persentase):
    """Menghitung persentase dari suatu nilai."""
    return (nilai * persentase) / 100

def hitung_angka_dari_persentase(nilai, persentase):
    """Menghitung angka berdasarkan persentase tertentu dari nilai."""
    return nilai * (1 + persentase / 100)

def hitung_selisih_persentase(nilai_awal, nilai_akhir):
    """Menghitung selisih persentase antara dua nilai."""
    return ((nilai_akhir - nilai_awal) / nilai_awal) * 100

def tampilkan_menu():
    """Menampilkan menu pilihan kalkulator persentase."""
    print("Kalkulator Persentase")
    print("1. Hitung Persentase dari Suatu Nilai")
    print("2. Hitung Nilai Berdasarkan Persentase")
    print("3. Hitung Selisih Persentase antara Dua Nilai")
    print("4. Keluar")

def kalkulator_persentase():
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Masukkan pilihan (1-4): "))
            
            if pilihan == 4:
                print("Terima kasih! Keluar dari program.")
                break
            
            if pilihan == 1:
                nilai = float(input("Masukkan nilai: "))
                persentase = float(input("Masukkan persentase: "))
                hasil = hitung_persentase(nilai, persentase)
                print(f"{persentase}% dari {nilai} adalah: {hasil}")

            elif pilihan == 2:
                nilai = float(input("Masukkan nilai: "))
                persentase = float(input("Masukkan persentase: "))
                hasil = hitung_angka_dari_persentase(nilai, persentase)
                print(f"Nilai setelah {persentase}% ditambahkan pada {nilai} adalah: {hasil}")

            elif pilihan == 3:
                nilai_awal = float(input("Masukkan nilai awal: "))
                nilai_akhir = float(input("Masukkan nilai akhir: "))
                hasil = hitung_selisih_persentase(nilai_awal, nilai_akhir)
                print(f"Selisih persentase antara {nilai_awal} dan {nilai_akhir} adalah: {hasil}%")

            else:
                print("Pilihan tidak valid. Coba lagi.")

        except ValueError:
            print("Input tidak valid. Masukkan angka yang benar.")
kalkulator_persentase()
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program penghitung usia

from datetime import datetime

def penghitung_usia():
    print('-' * 40)
    print("\tPenghitung Usia")
    print('-' * 40)
    
    # Meminta input tanggal lahir dari pengguna
    try:
        tanggal_lahir = input("Masukkan tanggal lahir Anda (format: YYYY-MM-DD): ")
        tanggal_lahir = datetime.strptime(tanggal_lahir, "%Y-%m-%d")
        
        # Mendapatkan tanggal hari ini
        hari_ini = datetime.now()
        
        # Menghitung usia
        usia_tahun = hari_ini.year - tanggal_lahir.year
        usia_bulan = hari_ini.month - tanggal_lahir.month
        usia_hari = hari_ini.day - tanggal_lahir.day

        # Penyesuaian jika bulan atau hari negatif
        if usia_hari < 0:
            usia_bulan -= 1
            usia_hari += (tanggal_lahir.replace(month=tanggal_lahir.month + 1, day=1) - tanggal_lahir).days
        if usia_bulan < 0:
            usia_tahun -= 1
            usia_bulan += 12

        print("\nHasil Penghitungan Usia:")
        print(f"Usia Anda: {usia_tahun} tahun, {usia_bulan} bulan, dan {usia_hari} hari.")
    except ValueError:
        print("Format tanggal tidak valid. Harap masukkan tanggal dalam format YYYY-MM-DD.")

# Menjalankan fungsi
penghitung_usia()
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program penghitung waktu mundur

import time

def penghitung_mundur(jam, menit, detik):
    """Menghitung mundur waktu dan menampilkannya setiap detik."""
    total_detik = jam * 3600 + menit * 60 + detik  
    while total_detik > 0:
        jam_sisa = total_detik // 3600
        menit_sisa = (total_detik % 3600) // 60
        detik_sisa = total_detik % 60
        
        
        print(f"{jam_sisa:02}:{menit_sisa:02}:{detik_sisa:02}", end='\r')
        time.sleep(1)  
        total_detik -= 1
    
    print("Waktu habis!")

def main():
    print("Penghitung Waktu Mundur")
    try:
        jam = int(input("Masukkan jam (0-23): "))
        menit = int(input("Masukkan menit (0-59): "))
        detik = int(input("Masukkan detik (0-59): "))
              
        penghitung_mundur(jam, menit, detik)
    except ValueError:
        print("Input tidak valid. Masukkan angka yang benar.")
main()
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program stopwatch mundur

print('-'*40)
print("\tSTOPWATCH MUNDUR")
print('-'*40)

import time

def stopwatch_mundur(detik):
    while detik >= 0:
        menit, sisa_detik = divmod(detik, 60)
        jam, menit = divmod(menit, 60)
        print(f"{jam:02}:{menit:02}:{sisa_detik:02}", end="\r")
        time.sleep(1)
        detik -= 1
    print("Waktu habis!")

durasi = int(input("Masukkan durasi stopwatch (detik): "))
stopwatch_mundur(durasi)
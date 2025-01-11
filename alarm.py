# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program alarm

print('-'*40)
print("\tALARM")
print('-'*40)

import time

alarm = input("Set waktu alarm (HH:MM): ")
while True:
    waktu_sekarang = time.strftime("%H:%M")
    if waktu_sekarang == alarm:
        print("Alarm berbunyi!")
        break
time.sleep(1)
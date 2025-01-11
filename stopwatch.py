# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program stopwatch

print('-'*40)
print("\tSTOPWATCH")
print('-'*40)

import time

input("Tekan Enter untuk mulai...")
start = time.time()
input("Tekan Enter untuk berhenti...")
end = time.time()
print(f"Waktu berlalu: {end - start:.2f}detik")
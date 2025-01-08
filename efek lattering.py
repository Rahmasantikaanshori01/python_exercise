# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program efek lattering

print('-'*40)
print("\t EFEK LATTERING")
print('-'*40)

import sys
import time

def tampilkan_tulisan(tulisan, jeda=0.1):
    """Menampilkan tulisan dengan efek lettering."""
    for huruf in tulisan:
        sys.stdout.write(huruf)
        sys.stdout.flush() 
        time.sleep(jeda)  
    print()  

teks = input("Masukkan teks yang ingin ditampilkan: ")
tampilkan_tulisan(teks)
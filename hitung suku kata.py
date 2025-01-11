# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program hitung suku kata

print('-'*40)
print("\tHITUNG SUKU KATA")
print('-'*40)

import re

def hitung_suku_kata(teks):
    teks = re.sub(r'[^\w\s]', '', teks)

    suku_kata = len(re.findall(r'[aiueoAIUEO]+', teks))
    
    return suku_kata

kalimat = input("Masukkan kata atau kalimat: ")

jumlah_suku_kata = hitung_suku_kata(kalimat)

print(f"Jumlah suku kata dalam kalimat: {jumlah_suku_kata}")

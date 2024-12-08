# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 Desember 2024
# program kuis matematika

import random

def kuis_matematika():
    print("Kuis Matematika")
    print("===================")
    print("Jawab soal matematika berikut. Ketik 'q' untuk keluar.\n")
    
    skor = 0  # Inisialisasi skor
    total_soal = 0

    while True:
        # Membuat bilangan dan operator acak
        angka1 = random.randint(1, 20)
        angka2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
        
        # Menentukan jawaban yang benar
        if operator == '+':
            jawaban_benar = angka1 + angka2
        elif operator == '-':
            jawaban_benar = angka1 - angka2
        elif operator == '*':
            jawaban_benar = angka1 * angka2

        # Memberikan soal kepada pengguna
        soal = f"{angka1} {operator} {angka2} = ? "
        jawaban = input(soal)
        
        # Keluar dari kuis
        if jawaban.lower() == 'q':
            print("\nAnda keluar dari kuis.")
            break

        # Memeriksa jawaban
        try:
            if int(jawaban) == jawaban_benar:
                print("Benar!")
                skor += 1
            else:
                print(f"Salah! Jawaban yang benar adalah {jawaban_benar}.")
            total_soal += 1
        except ValueError:
            print("Masukkan angka yang valid atau 'q' untuk keluar.")

    # Menampilkan skor akhir
    print("\nHasil Kuis:")
    print(f"Total Soal Dijawab: {total_soal}")
    print(f"Skor Anda: {skor}/{total_soal}")

# Menjalankan kuis
kuis_matematika()
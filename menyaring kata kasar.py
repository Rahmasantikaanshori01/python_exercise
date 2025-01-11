# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program menyaring kata kasar

print('-'*40)
print("\tMENYARING KATA KASAR")
print('-'*40)

def saring_kata_kasar(teks, kata_kasar):
    # Mengganti kata kasar dengan simbol '*'
    kata_teks = teks.split()
    for i, kata in enumerate(kata_teks):
        if kata.lower() in kata_kasar:
            kata_teks[i] = '*' * len(kata)
    return ' '.join(kata_teks)

kata_kasar = {"bodoh", "jelek",  "dungu", "bangsat"}

print("=== Penyaring Kata Kasar ===")
teks = input("Masukkan teks: ")
hasil = saring_kata_kasar(teks, kata_kasar)

print("\nHasil Penyaringan:")
print(hasil)
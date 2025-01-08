# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program pencari huruf kapital

print('-'*40)
print("\t PENCARI HURUF KAPITAL")
print('-'*40)

def hitung_huruf_kapital(teks):
    jumlah_kapital = 0
    huruf_kapital = []

    for huruf in teks:
        if huruf.isupper():  
            jumlah_kapital += 1
            huruf_kapital.append(huruf)

    return jumlah_kapital, huruf_kapital

teks = input("Masukkan kata atau kalimat: ")

jumlah, kapital_ditemukan = hitung_huruf_kapital(teks)

print(f"Teks yang dimasukkan: {teks}")
print(f"Jumlah huruf kapital: {jumlah}")
print(f"Huruf kapital yang ditemukan: {', '.join(kapital_ditemukan)}")
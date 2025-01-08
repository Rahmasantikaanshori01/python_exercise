# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program pencari huruf vocal

print('-'*40)
print("\t PENCARI HURUF VOCAL")
print('-'*40)

def hitung_vokal(teks):
    vokal = "aiueoAIUEO"
    jumlah_vokal = 0
    huruf_vokal = []

    for huruf in teks:
        if huruf in vokal:
            jumlah_vokal += 1
            huruf_vokal.append(huruf)

    return jumlah_vokal, huruf_vokal

teks = input("Masukkan kata atau kalimat: ")

jumlah, vokal_ditemukan = hitung_vokal(teks)

print(f"Teks yang dimasukkan: {teks}")
print(f"Jumlah huruf vokal: {jumlah}")
print(f"Huruf vokal yang ditemukan: {', '.join(vokal_ditemukan)}")
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program deteksi huruf konsonan

print('-'*40)
print("\tDETEKSI HURUF KONSONAN")
print('-'*40)

def deteksi_konsonan(teks):
    vokal = "aiueoAIUEO"
    konsonan = []
    for huruf in teks:
        if huruf.isalpha() and huruf not in vokal:
            konsonan.append(huruf)
    return konsonan

print("=== Deteksi Huruf Konsonan ===")
teks = input("Masukkan teks: ")

hasil_konsonan = deteksi_konsonan(teks)

print("\nHasil Deteksi:")
print(f"Jumlah huruf konsonan: {len(hasil_konsonan)}")
print(f"Konsonan yang ditemukan: {', '.join(hasil_konsonan)}")
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program penghitung teks

print('-'*40)
print("\tPENGHITUNG TEKS")
print('-'*40)

def hitung_teks(teks):
    vokal = "aiueoAIUEO"
    jumlah_kata = len(teks.split())
    jumlah_vokal = sum(1 for huruf in teks if huruf in vokal)
    jumlah_konsonan = sum(1 for huruf in teks if huruf.isalpha() and huruf not in vokal)
    jumlah_kalimat = teks.count('.') + teks.count('!') + teks.count('?')

    return jumlah_kata, jumlah_vokal, jumlah_konsonan, jumlah_kalimat

print("=== Penghitung Kata dalam Teks ===")
teks = input("Masukkan teks: ")

jumlah_kata, jumlah_vokal, jumlah_konsonan, jumlah_kalimat = hitung_teks(teks)

print("\nHasil Penghitungan:")
print(f"Jumlah kata: {jumlah_kata}")
print(f"Jumlah huruf vokal: {jumlah_vokal}")
print(f"Jumlah huruf konsonan: {jumlah_konsonan}")
print(f"Jumlah kalimat: {jumlah_kalimat}")
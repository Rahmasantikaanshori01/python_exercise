# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator waktu

print('-'*40)
print("\tKALKULATOR WAKTU")
print('-'*40)

total_detik = int(input("Masukkan total detik: "))
jam = total_detik // 3600
menit = (total_detik % 3600) // 60
detik = total_detik % 60
print(f"{jam} jam, {menit} menit,{detik}detik")
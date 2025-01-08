# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program tabel penjualan

print('-'*40)
print("\t TABEL PENJUALAN")
print('-'*40)

tabel_penjualan = [
    ["001", "Laptop", 1500, 10, 15000],
    ["002", "Smartphone", 800, 20, 16000],
    ["003", "Tablet", 600, 15, 9000],
    ["004", "Headphones", 100, 50, 5000],
    ["005", "Monitor", 200, 8, 1600],
]

header = ["Kode", "Produk", "Harga (USD)", "Jumlah", "Total Penjualan (USD)"]

def tampilkan_tabel_penjualan(data, header):
    print(f"{header[0]:<10} {header[1]:<12} {header[2]:<15} {header[3]:<10} {header[4]:<20}")
    print("-" * 70) 
    for baris in data:
        print(f"{baris[0]:<10} {baris[1]:<12} {baris[2]:<15} {baris[3]:<10} {baris[4]:<20}")

tampilkan_tabel_penjualan(tabel_penjualan,header)
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program catat pengeluaran

print('-'*40)
print("\tCATAT PENGELUARAN")
print('-'*40)

def catat_pengeluaran():
    pengeluaran = []
    while True:
        print("\n=== Kalkulator Pengeluaran ===")
        try:
            kategori = input("Masukkan kategori pengeluaran (contoh: Makanan, Transportasi, dll) atau 'selesai' untuk berhenti: ")
            if kategori.lower() == 'selesai':
                break

            jumlah = float(input(f"Masukkan jumlah pengeluaran untuk kategori '{kategori}': Rp "))
            pengeluaran.append((kategori, jumlah)) 

        except ValueError:
            print("Masukkan jumlah pengeluaran yang valid (angka).")
    
    return pengeluaran

def hitung_total_pengeluaran(pengeluaran):
    total = sum([jumlah for kategori, jumlah in pengeluaran])
    return total

def tampilkan_pengeluaran(pengeluaran, total):
    for kategori, jumlah in pengeluaran:
        print(f"{kategori}: Rp {jumlah:,.2f}")
    print(f"\nTotal Pengeluaran: Rp {total:,.2f}")

pengeluaran = catat_pengeluaran()  
total = hitung_total_pengeluaran(pengeluaran)  
tampilkan_pengeluaran(pengeluaran, total)  
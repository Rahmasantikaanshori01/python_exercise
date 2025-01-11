# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator diskon

print('-'*40)
print("\tKALKULATOR DISKON")
print('-'*40)

def hitung_diskon(harga_awal, diskon_persen):
    """Fungsi untuk menghitung harga setelah diskon."""
    diskon = harga_awal * (diskon_persen / 100)
    harga_setelah_diskon = harga_awal - diskon
    return diskon, harga_setelah_diskon

def kalkulator_diskon():
    print("=== Kalkulator Diskon ===")
    
    try:
        harga_awal = float(input("Masukkan harga awal barang: Rp "))
        diskon_persen = float(input("Masukkan persentase diskon: "))
        
        diskon, harga_setelah_diskon = hitung_diskon(harga_awal, diskon_persen)
        
        print(f"\nDiskon yang diberikan: Rp {diskon:,.2f}")
        print(f"Harga setelah diskon: Rp {harga_setelah_diskon:,.2f}")
    
    except ValueError:
        print("Masukkan nilai yang valid (harus berupa angka).")

kalkulator_diskon()
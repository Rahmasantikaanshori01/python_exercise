# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator pajak

print('-'*40)
print("\tKALKULATOR PAJAK")
print('-'*40)

def hitung_pajak(penghasilan, tarif_pajak):
    """Fungsi untuk menghitung pajak berdasarkan penghasilan dan tarif pajak."""
    pajak = penghasilan * (tarif_pajak / 100)
    return pajak

def kalkulator_pajak():
    print("=== Kalkulator Pajak Penghasilan ===")
    
    try:
        penghasilan = float(input("Masukkan penghasilan tahunan Anda: Rp "))
        tarif_pajak = float(input("Masukkan tarif pajak (misalnya 10, 20, 30): "))
        
        pajak = hitung_pajak(penghasilan, tarif_pajak)
        total_setelah_pajak = penghasilan - pajak
        
        print(f"\nPajak yang harus dibayar: Rp {pajak:,.2f}")
        print(f"Total penghasilan setelah dipotong pajak: Rp {total_setelah_pajak:,.2f}")
    
    except ValueError:
        print("Masukkan nilai yang valid (harus berupa angka).")

kalkulator_pajak()
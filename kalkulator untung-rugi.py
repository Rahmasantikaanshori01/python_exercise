# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator untung-rugi

print('-'*40)
print("\tKALKULATOR UNTUNG-RUGI")
print('-'*40)

def hitung_keuntungan_kerugian(harga_beli, harga_jual):
    """Fungsi untuk menghitung keuntungan atau kerugian."""
    if harga_jual > harga_beli:
        keuntungan = harga_jual - harga_beli
        return keuntungan, "Keuntungan"
    elif harga_jual < harga_beli:
        kerugian = harga_beli - harga_jual
        return kerugian, "Kerugian"
    else:
        return 0, "Tidak ada keuntungan atau kerugian"

def kalkulator_keuntungan_kerugian():
    try:
        harga_beli = float(input("Masukkan harga beli barang: Rp "))
        harga_jual = float(input("Masukkan harga jual barang: Rp "))
        
        hasil, status = hitung_keuntungan_kerugian(harga_beli, harga_jual)
        
        if status == "Keuntungan":
            print(f"\nKeuntungan yang didapat: Rp {hasil:,.2f}")
        elif status == "Kerugian":
            print(f"\nKerugian yang dialami: Rp {hasil:,.2f}")
        else:
            print(f"\n{status}")
    
    except ValueError:
        print("Masukkan nilai yang valid (harus berupa angka).")

kalkulator_keuntungan_kerugian()
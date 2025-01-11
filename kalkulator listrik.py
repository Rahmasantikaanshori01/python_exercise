# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kalkulator listrik

print('-'*40)
print("\tKALKULATOR LISTRIK ")
print('-'*40)

def kalkulator_listrik():
    try:
        daya_peralatan = float(input("Masukkan daya peralatan listrik (dalam watt): "))
        waktu_pemakaian = float(input("Masukkan waktu pemakaian (dalam jam): "))
        tarif_per_kwh = float(input("Masukkan tarif listrik per kWh (dalam Rp): "))

        konsumsi_kwh = (daya_peralatan * waktu_pemakaian) / 1000 

        estimasi_biaya = konsumsi_kwh * tarif_per_kwh

        print(f"\nKonsumsi energi: {konsumsi_kwh:.2f} kWh")
        print(f"Estimasi biaya listrik: Rp {estimasi_biaya:,.2f}")

    except ValueError:
        print("Masukkan nilai yang valid (harus berupa angka).")

kalkulator_listrik()
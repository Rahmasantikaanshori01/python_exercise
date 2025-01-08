# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program deteksi bilangan prima

print('-'*40)
print("\tDETEKSI BILANGAN PRIMA")
print('-'*40)

def cek_prima(angka):
    """Fungsi untuk memeriksa apakah sebuah angka adalah bilangan prima."""
    if angka <= 1:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

def main():
    print("Program Deteksi Bilangan Prima")
    while True:
        try:
            angka = int(input("\nMasukkan angka (atau ketik -1 untuk keluar): "))
            if angka == -1:
                print("Terima kasih telah menggunakan program ini!")
                break
            if cek_prima(angka):
                print(f"{angka} adalah bilangan prima.")
            else:
                print(f"{angka} bukan bilangan prima.")
        except ValueError:
            print("Masukkan angka yang valid!")

main()
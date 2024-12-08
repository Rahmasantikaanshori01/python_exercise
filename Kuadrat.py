# dibuat oleh : Rahma Santika Al Anshori
# tanggal di buat : 08 Desember 2024
# program kuadrat

print('-' * 40)
print("\tNILAI KUADRAT")
print('-' * 40)

def kuadrat(angka):
    return angka**2

angka = int(input("Masukkan angka untuk dihitung kuadratnya: "))
print(f"Kuadrat dari {angka} adalah {kuadrat(angka)}")
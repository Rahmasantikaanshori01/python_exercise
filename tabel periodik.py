# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program tabel periodik

print('-'*40)
print("\t TABEL PERIODIK")
print('-'*40)

tabel_periodik = [
    ["1", "H", "Hydrogen", "1.008"],
    ["2", "He", "Helium", "4.0026"],
    ["3", "Li", "Lithium", "6.94"],
    ["4", "Be", "Beryllium", "9.0122"],
    ["5", "B", "Boron", "10.81"],
    ["6", "C", "Carbon", "12.011"],
    ["7", "N", "Nitrogen", "14.007"],
    ["8", "O", "Oxygen", "15.999"],
    ["9", "F", "Fluorine", "18.998"],
    ["10", "Ne", "Neon", "20.180"],
]

header = ["No.", "Simbol", "Nama", "Massa Atom (g/mol)"]

def tampilkan_tabel(data, header):
    print(f"{header[0]:<5} {header[1]:<6} {header[2]:<10} {header[3]:<20}")
    print("-" * 40) 

    for baris in data:
        print(f"{baris[0]:<5} {baris[1]:<6} {baris[2]:<10} {baris[3]:<20}")

tampilkan_tabel(tabel_periodik,header)
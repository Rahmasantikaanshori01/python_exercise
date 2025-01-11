# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kosakata sunda

print('-'*40)
print("\tKOSAKATA SUNDA")
print('-'*40)

def buat_tabel_sunda(kosakata):
    header = f"{'No.':<5} {'Bahasa Indonesia':<30} {'Bahasa Sunda':<30}"
    garis = "-" * 50
    print(header)
    print(garis)

    for i, (indonesia, sunda) in enumerate(kosakata.items(), start=1):
        print(f"{i:<5} {indonesia:<30} {sunda:<30}")

kosakata = {
    "Makan": "Tuang",
    "Minum": "Inum",
    "Tidur": "Saré",
    "Pergi": "Angkat",
    "Datang": "Sumping",
    "Ayah": "Bapa",
    "Ibu": "Indung",
    "Adik": "Adi",
    "Kakak": "Akang/Teteh",
    "Rumah": "Imah",
    "Sekolah": "Sakola",
    "Buku": "Buku",
    "Teman": "Réréncangan",
    "Cinta": "Deudeuh",
    "Cantik": "Geulis",
    "Ganteng": "Kasep",
    "Apa": "Naon",
    "Kenapa": "Kunaon",
    "Siapa": "Saha",
    "Bagaimana": "Kumaha",
    "Kapan": "Iraha",
    "Kemana": "Kamana",
    "Darimana": "Timana",
    "Berapa": "Sabaraha",
    "Terima Kasih": "Hatur Nuhun"
}

buat_tabel_sunda(kosakata)
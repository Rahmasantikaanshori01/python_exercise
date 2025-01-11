# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 11 januari 2025
# program kosakata arab

print('-'*40)
print("\tKOSAKATA ARAB")
print('-'*40)

def buat_tabel_arab(kosakata):
    header = f"{'No.':<5} {'Bahasa Indonesia':<20} {'Bahasa Arab':<20}"
    garis = "-" * 50
    print(header)
    print(garis)
    
    for i, (indonesia, arab) in enumerate(kosakata.items(), start=1):
        print(f"{i:<5} {indonesia:<20} {arab:<20}")

kosakata = {
    "Makan": "أكل (Akala)",
    "Minum": "شرب (Shariba)",
    "Tidur": "نوم (Naum)",
    "Pergi": "ذهب (Dhahaba)",
    "Datang": "جاء (Ja'a)",
    "Ayah": "أب (Abun)",
    "Ibu": "أم (Ummun)",
    "Adik": "أخ/أخت (Akh/Ukht)",
    "Kakak": "أخ/أخت (Akh/Ukht)",
    "Rumah": "بيت (Bayt)",
    "Sekolah": "مدرسة (Madrasa)",
    "Buku": "كتاب (Kitab)",
    "Teman": "صديق (Sadiq)",
    "Cinta": "حب (Hubb)",
    "Cantik": "جميلة (Jamilah)"
}

buat_tabel_arab(kosakata)
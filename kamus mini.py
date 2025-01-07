# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program kamus mini

kamus = {"python": "Bahasa pemograman yang populer dan mudah dipelajari.", 
"komputer": "Mesin elektronik yang dirancang untuk mengolah data.", 
"program": "Kumpulan instruksi yang diberikan kepada komputer untuk menjalankan tugas tertentu",
"data": "Informasi yang dapat di proses oleh komputer. ",
"algoritma": "Langkah-langkah atau prosedur yang terstruktur untuk menyelesaikan masalah"}

def cari_kata():
    print("selamat datang di kamus mini!")
    while True:
        kata = input("\nMasukkan kata yang ingin dicari (atau ketik 'keluar' untuk selesai): ").lower()
        if kata == "keluar":
            print ("Terima kasih telah menggunakan kamus mini!")
            break
        elif kata in kamus:
            print(f"{kata.capitalize()}:{kamus[kata]}")
        else:
            print(f"Maaf, kata '{kata}' tidak ditemukan dalam kamus.")   

cari_kata()             
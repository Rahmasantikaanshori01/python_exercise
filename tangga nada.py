# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program tangga nada

print('-'*40)
print("\t TANGGA NADA")
print('-'*40)

def buat_tangga_nada(nada_dasar, jenis_tangga):
    # Notasi dasar (C = Do, D = Re, dst.)
    notasi_musik = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    tangga_nada = {
        'mayor': [2, 2, 1, 2, 2, 2, 1],
        'minor': [2, 1, 2, 2, 1, 2, 2]
    }

    if nada_dasar not in notasi_musik:
        return f"Error: Nada dasar '{nada_dasar}' tidak valid."
    if jenis_tangga not in tangga_nada:
        return f"Error: Jenis tangga nada '{jenis_tangga}' tidak valid."

    pola = tangga_nada[jenis_tangga]
    index_awal = notasi_musik.index(nada_dasar)
    hasil_tangga = [nada_dasar]

    for interval in pola:
        index_awal = (index_awal + interval) % len(notasi_musik)
        hasil_tangga.append(notasi_musik[index_awal])

    return hasil_tangga

nada_dasar = input("Masukkan nada dasar (misal: C, D, E, dll.): ").upper()
jenis_tangga = input("Masukkan jenis tangga nada (mayor/minor): ").lower()

hasil = buat_tangga_nada(nada_dasar, jenis_tangga)

if isinstance(hasil, list):
    print(f"Tangga nada {jenis_tangga} dari {nada_dasar}: {', '.join(hasil)}")
else:
     print(hasil)
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program limas segiempat

print('-'*40)
print("\t LIMAS SEGIEMPAT")
print('-'*40)

def luas_alas(s):
    return s ** 2

def volume_limas(luas_alas, tinggi_limas):
    return (1 / 3) * luas_alas * tinggi_limas

def luas_segitiga(s, tinggi_segitiga):
    return 0.5 * s * tinggi_segitiga

def luas_permukaan_limas(luas_alas, luas_segitiga, jumlah_segitiga):
    return luas_alas + jumlah_segitiga * luas_segitiga

s = 4  
tinggi_limas = 6  # cm
tinggi_segitiga = 5  # cm

luas_alas = luas_alas(s)

volume = volume_limas(luas_alas, tinggi_limas)

luas_segitiga_samping = luas_segitiga(s, tinggi_segitiga)

luas_permukaan = luas_permukaan_limas(luas_alas, luas_segitiga_samping, 4)

print(f"Volume limas segi empat: {volume} cm^3")
print(f"Luas permukaan limas segi empat: {luas_permukaan}cm^2")
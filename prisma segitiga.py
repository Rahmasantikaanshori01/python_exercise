# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program prisma segitiga

print('-'*40)
print("\t PRISMA SEGITIGA")
print('-'*40)

def luas_alas_segitiga(alas, tinggi_segitiga):
    return 0.5 * alas * tinggi_segitiga

def volume_prisma(luas_alas, tinggi_prisma):
    return luas_alas * tinggi_prisma

def keliling_segitiga(sisi1, sisi2, sisi3):
    return sisi1 + sisi2 + sisi3

def luas_permukaan_prisma(luas_alas, keliling_alas, tinggi_prisma):
    return 2 * luas_alas + keliling_alas * tinggi_prisma

alas = 6  # cm
tinggi_segitiga = 4  # cm
tinggi_prisma = 10  # cm
sisi1 = 6  # cm
sisi2 = 5  # cm
sisi3 = 7  # cm

luas_alas = luas_alas_segitiga(alas, tinggi_segitiga)

volume = volume_prisma(luas_alas, tinggi_prisma)

keliling_alas = keliling_segitiga(sisi1, sisi2, sisi3)

luas_permukaan = luas_permukaan_prisma(luas_alas, keliling_alas, tinggi_prisma)

print(f"Volume Prisma Segitiga: {volume} cm^3")
print(f"Luas Permukaan Prisma Segitiga: {luas_permukaan} cm^2")
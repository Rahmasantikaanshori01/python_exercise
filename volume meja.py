# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program volume meja

print('-'*40)
print("\t VOLUME MEJA")
print('-'*40)

def volume_meja(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

panjang = 1.5  # M
lebar = 0.75  # M
tinggi = 0.8  # M

volume = volume_meja(panjang, lebar, tinggi)

print(f"Volume meja adalah:{volume}m^3")
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 10 januari 2025
# program volume balok

print('-'*40)
print("\t VOLUME BALOK")
print('-'*40)

def volume_Balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


panjang = 5 # cM
lebar = 3  # cM
tinggi = 4 # cM

volume = volume_Balok(panjang, lebar, tinggi)

print(f"Volume balok adalah:{volume}m^3")
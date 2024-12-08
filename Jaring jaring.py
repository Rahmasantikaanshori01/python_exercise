# dibuat oleh : Rahma Santika Al Anshori
# tanggal di buat : 08 Desember 2024
# program jaring jaring

print('-' * 40)
print("RUMUS JARING JARING")
print('-' * 40)

r = int(input('masukan jari jari : '))
s = int(input('masukan sisi miring : '))
t = int(input('masukan tinggi : '))

ls = 3.14 * r * s
lp = (3.14 * r * s) + (3.14 * r * r)
v = 1/3 * 3.14 * r * r * t

print(f'jadi luas selimutnya adalah {ls} luas permukaannya adalah {lp} dan volumenya adalah {v}')
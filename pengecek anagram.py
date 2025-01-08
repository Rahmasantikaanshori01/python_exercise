# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 08 januari 2025
# program pengecek anagram

print('-'*40)
print("\t PENGECEK ANAGRAM")
print('-'*40)

def is_anagram(word1, word2):
    
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    
    return sorted(word1) == sorted(word2)

kata1 = input("Masukkan kata atau kalimat pertama: ")
kata2 = input("Masukkan kata atau kalimat kedua: ")

if is_anagram(kata1, kata2):
    print(f'"{kata1}" dan "{kata2}" adalah anagram.')
else:
    print(f'"{kata1}" dan "{kata2}" bukan anagram.')
# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 06 januari 2025
# program menentukan polindrom


kata = input("Masukkan kata: ").lower()
if kata == kata[::-1]:
    print(f"{kata} adalah palindrom.")
else:
    print(f"{kata} bukan palindrom.")
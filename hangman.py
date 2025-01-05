# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 05 januari 2025
# program permainan hangman

import random

# Daftar kata rahasia
words = ["python", "programming", "hangman", "developer", "algorithm"]

# Memilih kata rahasia secara acak
secret_word = random.choice(words)
guessed_word = ["_"] * len(secret_word)  
attempts = 6  # Jumlah nyawa

print("=== Selamat Datang di Permainan Hangman ===")
print(f"Kata rahasia memiliki {len(secret_word)} huruf.")

while attempts > 0 and "_" in guessed_word:
    print("\nKata saat ini: " + " ".join(guessed_word))
    print(f"Nyawa tersisa: {attempts}")
    
    guess = input("Tebak sebuah huruf: ").lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Masukkan satu huruf saja!")
        continue

    if guess in guessed_word:
        print("Anda sudah menebak huruf ini!")
        continue

    if guess in secret_word:
        print(f"Benar! Huruf '{guess}' ada dalam kata rahasia.")
        for idx, letter in enumerate(secret_word):
            if letter == guess:
                guessed_word[idx] = guess
    else:
        print(f"Salah! Huruf '{guess}' tidak ada dalam kata rahasia.")
        attempts -= 1

if "_" not in guessed_word:
    print("\nSelamat! Anda berhasil menebak kata rahasia:", "".join(guessed_word))
else:
    print("\nAnda kehabisan nyawa! Kata rahasia adalah:", secret_word)

print("=== Terima kasih telah bermain! ===")
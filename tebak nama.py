# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 05 januari 2025
# program tebak nama

import random

# Daftar karakter
characters = [
    {"name": "Zorg", "alien": True},
    {"name": "John", "alien": False},
    {"name": "Xander", "alien": True},
    {"name": "Sarah", "alien": False},
    {"name": "Klaatu", "alien": True},
]

def game_tebak_alien():
    print("Selamat datang di Game Tebak Alien!")
    print("Tebak apakah karakter ini adalah alien atau bukan.\n")

    score = 0
    for i in range(5): 
        character = random.choice(characters)
        print(f"Karakter yang muncul: {character['name']}")
        guess = input("Apakah ini alien? (ya/tidak): ").lower()

        if (guess == "ya" and character["alien"]) or (guess == "tidak" and not character["alien"]):
            print("Tebakan Anda benar!")
            score += 1
        else:
            print("Tebakan Anda salah.")
        
        print(f"Score Anda: {score}\n")

    print(f"Permainan selesai. Skor akhir Anda: {score}")

game_tebak_alien()
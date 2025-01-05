# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 05 januari 2025
# program game zombie

import random
import time

player_health = 100
player_resources = 0
zombie_health = 50
game_over = False

def display_status():
    print(f"\nKesehatan Pemain: {player_health}")
    print(f"Sumber Daya: {player_resources}")
    print(f"Kesehatan Zombie: {zombie_health}")

def collect_resources():
    global player_resources
    collected = random.choice([True, False])
    if collected:
        resources_found = random.randint(1, 5)
        player_resources += resources_found
        print(f"Anda berhasil mengumpulkan {resources_found} sumber daya!")
    else:
        print("Tidak ada sumber daya yang ditemukan di sekitar Anda.")

def attack_zombie():
    global zombie_health
    damage = random.randint(10, 30)
    zombie_health -= damage
    print(f"Anda menyerang zombie dan memberikan {damage} kerusakan!")

def zombie_attack():
    global player_health
    damage = random.randint(5, 15)
    player_health -= damage
    print(f"Zombie menyerang Anda dan memberikan {damage} kerusakan!")

def build_defense():
    global player_resources
    if player_resources >= 10:
        player_resources -= 10
        print("Anda berhasil membangun perlindungan!")
        return True
    else:
        print("Anda tidak memiliki cukup sumber daya untuk membangun perlindungan.")
        return False

def game_loop():
    global player_health, zombie_health, game_over
    print("Selamat datang di Zombie Survival Game!\n")
    while not game_over:
        
        display_status()

       
        print("\nPilih tindakan:")
        print("1. Mengumpulkan sumber daya")
        print("2. Menyerang zombie")
        print("3. Membangun perlindungan")
        print("4. Menunggu (Zombie akan menyerang)")
        choice = input("\nApa yang ingin Anda lakukan? (1/2/3/4): ")

        if choice == "1":
            collect_resources()
        elif choice == "2":
            attack_zombie()
        elif choice == "3":
            if build_defense():
                zombie_health -= 20  
        elif choice == "4":
            print("Anda menunggu...\nZombie menyerang!")
        else:
            print("Pilihan tidak valid. Cobalah lagi.")
            continue
            
        if zombie_health > 0:
            zombie_attack()

        if player_health <= 0:
            print("\nGame Over! Anda telah mati.")
            game_over = True
        elif zombie_health <= 0:
            print("\nSelamat! Anda berhasil mengalahkan zombie!")
            game_over = True

        time.sleep(1)

game_loop()
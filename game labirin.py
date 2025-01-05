# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 05 januari 2025
# program game labirin

# Labirin 5x5 sebagai array 2D
maze = [
    ["S", ".", ".", ".", "."],
    [".", "#", ".", "#", "."],
    [".", "#", ".", ".", "."],
    [".", ".", ".", "#", "."],
    [".", ".", ".", ".", "E"]
]

def print_maze():
    for row in maze:
        print(" ".join(row))

def game_labirin():
    player_position = [0, 0]  # Mulai di posisi (0, 0) yang ditandai dengan "S"
    print("Selamat datang di Game Labirin!")
    print("Anda harus menuju ke titik 'E' untuk menang.")
    
    while True:
        print_maze()
        move = input("Pilih pergerakan (atas, bawah, kiri, kanan): ").lower()

        # Update posisi pemain
        if move == "atas" and player_position[0] > 0 and maze[player_position[0] - 1][player_position[1]] != "#":
            player_position[0] -= 1
        elif move == "bawah" and player_position[0] < 4 and maze[player_position[0] + 1][player_position[1]] != "#":
            player_position[0] += 1
        elif move == "kiri" and player_position[1] > 0 and maze[player_position[0]][player_position[1] - 1] != "#":
            player_position[1] -= 1
        elif move == "kanan" and player_position[1] < 4 and maze[player_position[0]][player_position[1] + 1] != "#":
            player_position[1] += 1
        else:
            print("Gerakan tidak valid atau dinding! Coba lagi.")
            continue

        # Cek apakah pemain sampai ke tujuan
        if maze[player_position[0]][player_position[1]] == "E":
            print("Selamat! Anda berhasil keluar dari labirin!")
            break

game_labirin()
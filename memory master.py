# Dibuat oleh : Rahma Santika Al anshori
# Tanggal pengerjaan : 05 januari 2025
# program memory master

import random

# Kartu yang harus dicocokkan
cards = ["A", "B", "C", "D", "E", "F", "A", "B", "C", "D", "E", "F"]
random.shuffle(cards)  # Mengacak kartu

def print_board(board):
    for row in board:
        print(" ".join(row))

def game_memory():
    board = [["*" for _ in range(4)] for _ in range(3)]  # 3x4 papan
    revealed = set()  # Set untuk melacak kartu yang dibuka

    print("Selamat datang di Game Memory!")
    turns = 0

    while len(revealed) < len(cards):
        print_board(board)
        print("Pilih dua kartu untuk dibuka.")
        

        try:
            first_choice = tuple(map(int, input("Masukkan posisi kartu pertama (baris kolom): ").split()))
            second_choice = tuple(map(int, input("Masukkan posisi kartu kedua (baris kolom): ").split()))

            if first_choice == second_choice or first_choice not in [(i, j) for i in range(3) for j in range(4)] or second_choice not in [(i, j) for i in range(3) for j in range(4)]:
                print("Posisi kartu tidak valid! Coba lagi.")
                continue
        except ValueError:
            print("Masukkan posisi kartu dengan format yang benar (misal: 0 0).")
            continue

        # Tampilkan kartu yang dibuka
        first_row, first_col = first_choice
        second_row, second_col = second_choice
        board[first_row][first_col] = cards[first_row * 4 + first_col]
        board[second_row][second_col] = cards[second_row * 4 + second_col]

        print_board(board)

        if cards[first_row * 4 + first_col] == cards[second_row * 4 + second_col]:
            print("Kartu cocok!")
            revealed.add(cards[first_row * 4 + first_col])
        else:
            print("Kartu tidak cocok!")
            board[first_row][first_col] = "*"
            board[second_row][second_col] = "*"

        turns += 1


    print(f"Selamat! Anda berhasil mencocokkan semua kartu dalam {turns} putaran.")

game_memory()
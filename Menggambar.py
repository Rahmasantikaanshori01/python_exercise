# dibuat oleh : Rahma Santika Al Anshori
# tanggal di buat : 08 Desember 2024
# program menggambar bunga

print('-' * 40)
print("\tMENGGAMBAR BUNGA")
print('-' * 40)

import turtle

# Setup layar dan turtle
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(10)

# Fungsi untuk menggambar petal bunga
def petal():
    t.color("red")
    t.begin_fill()
    t.circle(100, 60)  # Menggambar setengah lingkaran
    t.left(120)
    t.circle(100, 60)  # Menggambar setengah lingkaran kedua
    t.left(120)
    t.end_fill()

# Menggambar bunga dengan beberapa kelopak
for _ in range(6):
    petal()
    t.left(60)  # Putar untuk menggambar kelopak berikutnya

# Menggambar bagian tengah bunga (stigma)
t.penup()
t.goto(0, -20)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(20)  # Lingkaran kecil untuk bagian tengah bunga
t.end_fill()

# Selesai menggambar
t.hideturtle()
turtle.done()
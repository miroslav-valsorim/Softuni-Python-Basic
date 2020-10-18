import sys

painted_eggs = int(input())

red = 0
orange = 0
blue = 0
green = 0
max_color = -sys.maxsize

while True:
    egg_color = input()

    if egg_color == "red":
        red += 1
    elif egg_color == "orange":
        orange += 1
    elif egg_color == "blue":
        blue += 1
    elif egg_color == "green":
        green += 1
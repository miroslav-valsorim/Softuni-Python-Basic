#На първия ред е широчината на кораба - реално число в интервала [1.00... 10.00]
# На втория ред е дължината на кораба - реално число в интервала [1.00…10.00]
#На третия ред е височината на кораба - реално число в интервала [1.00…20.00]
# На четвъртия ред е средната височина на астронавтите - реално число в интервала [1.50 … 1.90]
from math import floor
width_of_spaceship = float(input())
length_of_spaceship = float(input())
height_of_spaceship = float(input())
middle_height_of_people = float(input())

volume = width_of_spaceship * length_of_spaceship * height_of_spaceship
room_volume = (middle_height_of_people + 0.40) * 2 * 2
place_for_people = floor(volume / room_volume)

if 3 <= place_for_people <= 10:
    print(f"The spacecraft holds {place_for_people} astronauts.")
elif place_for_people < 3:
    print(f"The spacecraft is too small.")
elif place_for_people > 10:
    print(f"The spacecraft is too big.")
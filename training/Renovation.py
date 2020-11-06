from math import ceil
wall_height = int(input())
wall_width = int(input())
wall_percentage = int(input())

paint_needed = wall_width * wall_height * 4
total_paint = paint_needed - paint_needed * wall_percentage / 100
paints = total_paint

command = input()
while command != "Tired!":
    paint_liters = int(command)

    paints -= paint_liters
    if paints == 0:
        print(f"All walls are painted! Great job, Pesho!")
        break
    if paints < 0:
        print(f"All walls are painted and you have {ceil(abs(paints))} l paint left!")
        break
    command = input()

if command == "Tired!":
    print(f"{ceil(paints)} quadratic m left.")
stadium_capacity = int(input())
all_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
capacity_percentage = 0

for fans in range(1, all_fans + 1):
    stadium_part = input()
    if stadium_part == "A":
        sector_a += 1
    elif stadium_part == "B":
        sector_b += 1
    elif stadium_part == "V":
        sector_v += 1
    elif stadium_part == "G":
        sector_g += 1

print(f"{(sector_a / all_fans * 100):.2f}%")
print(f"{(sector_b/ all_fans * 100):.2f}%")
print(f"{(sector_v / all_fans * 100):.2f}%")
print(f"{(sector_g / all_fans * 100):.2f}%")
print(f"{(all_fans / stadium_capacity * 100):.2f}%")
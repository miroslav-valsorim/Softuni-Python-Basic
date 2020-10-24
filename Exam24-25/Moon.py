from math import ceil
middle_speed = float(input())
liters_for_hundred_km = float(input())

total_distance = 384400 * 2
total_time = ceil(total_distance / middle_speed)

plus_time_on_moon = total_time + 3

fuel = (liters_for_hundred_km * total_distance) / 100

print(plus_time_on_moon)
print(int(fuel))
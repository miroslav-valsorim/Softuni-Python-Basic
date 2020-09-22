lenght = float(input())
wide = float(input())
height = float(input())
volume = float(input())
tank_volume_dcm = lenght * wide * height
tank_volume_liters = tank_volume_dcm / 1000
volume_per_cent = volume / 100
water = tank_volume_liters * (1-volume_per_cent)
print(water)
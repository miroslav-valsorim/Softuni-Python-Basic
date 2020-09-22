x = float(input())
y = float(input())
h = float(input())
green = 3.4
red = 4.3

door = 1.2*2
front_wall = x * x - door
back_wall = x * x
window = 1.5 * 1.5
side_wall = (x * y - window) * 2
house_area = side_wall + front_wall + back_wall
green_paint = house_area / green
print(f'{green_paint:.2f}')

#s = ( x + x + x ) / 2
#area = (s* (s-x) * (s-x) * (s-x)) ** 0.5
area = x * h / 2
roof_scat = x * y
roof_area = roof_scat * 2 + area * 2
red_paint = roof_area / red
print(f'{red_paint:.2f}')






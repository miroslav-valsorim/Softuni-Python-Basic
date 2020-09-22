import math

type = input()



if type == "square":
    side = float(input())
    square_area = math.pow(side, 2)
    print(f'{square_area:.3f} ')
elif type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    rectangle_area = side_a * side_b
    print(f'{rectangle_area:.3f}')
elif type == "circle":
    r = float(input())
    circle_area = math.pi * math.pow(r, 2)
    print(f'{circle_area:.3f}')
elif type == "triangle":
    a = float(input())
    h = float(input())
    triangle_area = a * h / 2
    print(f'{triangle_area:.3f}')
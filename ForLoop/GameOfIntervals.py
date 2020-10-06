how_many_numbers = int(input())

sum_of_numbers = 0
int_one = 0
int_two = 0
int_three = 0
int_four = 0
int_five = 0
int_six = 0
bonus = 0

for numbers in range(1, how_many_numbers + 1):
    n = int(input())

    if 0 <= n <= 9:
        int_one += 1
        bonus = n - n * 80 / 100
        sum_of_numbers += bonus
    elif 10 <= n <= 19:
        int_two += 1
        bonus = n - n * 70 / 100
        sum_of_numbers += bonus
    elif 20 <= n <= 29:
        int_three += 1
        bonus = n - n * 60 / 100
        sum_of_numbers += bonus
    elif 30 <= n <= 39:
        int_four += 1
        bonus += 50
        sum_of_numbers += bonus
    elif 40 <= n <= 50:
        int_five += 1
        bonus += 100
        sum_of_numbers += bonus
    else:
        int_six += 1
        sum_of_numbers /= 2

print(f"{sum_of_numbers:.2f}")
print(f"From 0 to 9: {(int_one / how_many_numbers * 100):.2f}%")
print(f"From 10 to 19: {(int_two / how_many_numbers * 100):.2f}%")
print(f"From 20 to 29: {(int_three / how_many_numbers * 100):.2f}%")
print(f"From 30 to 39: {(int_four / how_many_numbers * 100):.2f}%")
print(f"From 40 to 50: {(int_five / how_many_numbers * 100):.2f}%")
print(f"Invalid numbers: {(int_six / how_many_numbers * 100):.2f}%")


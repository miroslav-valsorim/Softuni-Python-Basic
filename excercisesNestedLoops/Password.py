number_one = int(input())
number_two = int(input())
number_three = int(input())

for one in range(2, number_one + 1, 2):
    for two in range(2, number_two + 1):
        for three in range(2, number_three + 1, 2):
            if two == 2 or two == 3 or two == 5 or two == 7:
                print(f"{one} {two} {three}")
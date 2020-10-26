number_one = int(input())
number_two = int(input())
number_three = int(input())

for one in range(1, number_one + 1):
    if one % 2 == 0:
        if 2 <= number_two <= 7:
            for two in range(1, number_two + 1):
                for three in range(1, number_three):
                    if three % 2 == 0:
                        print(f"{one}{two}{three}")
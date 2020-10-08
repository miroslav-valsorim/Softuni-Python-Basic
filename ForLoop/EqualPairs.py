n = int(input())
is_all_equal = True
current_sum = 0
previous_sum = 0
biggest_difference_between_two_couples = 0
for numbers in range(1, 2 * n + 1):
    number = int(input())
    if numbers % 2 == 0:
        current_sum += number
        if numbers == 2:
            previous_sum = current_sum
        else:
            if current_sum != previous_sum:
                is_all_equal = False
        difference_between_last_two_couples = abs(current_sum - previous_sum)
        if difference_between_last_two_couples > biggest_difference_between_two_couples:
            biggest_difference_between_two_couples = abs(
                difference_between_last_two_couples)
        previous_sum = current_sum
        current_sum = 0
    else:
        current_sum += number
if is_all_equal:
    print(f"Yes, value={previous_sum}")
else:
    print(f"No, maxdiff={biggest_difference_between_two_couples}")
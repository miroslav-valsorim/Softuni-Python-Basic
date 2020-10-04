import sys

n = int(input())

sum_of_all_numbers = 0
max_element = -sys.maxsize

for number in range(1, n + 1):
    num = int(input())
    sum_of_all_numbers += num
    if num > max_element:
        max_element = num
if max_element == sum_of_all_numbers - max_element:
    print("Yes")
    print(f"Sum = {max_element}")
else:
    print("No")
    print(f"Diff = {abs(max_element - (sum_of_all_numbers - max_element))}")
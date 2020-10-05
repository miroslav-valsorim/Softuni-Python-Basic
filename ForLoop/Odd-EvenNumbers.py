import sys

n = int(input())

odd_sum = 0
odd_max = -sys.maxsize
odd_min = sys.maxsize

even_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize

for number in range(1, n + 1):
    new_number = float(input())
    if number % 2 == 0:
        even_sum += new_number
        if new_number > even_max:
            even_max = new_number
        if new_number < even_min:
            even_min = new_number
    else:
        odd_sum += new_number
        if new_number > odd_max:
            odd_max = new_number
        if new_number < odd_min:
            odd_min = new_number

print(f"OddSum={odd_sum:.2f},")

if odd_min == sys.maxsize:
    print(f"OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -sys.maxsize:
    print(f"OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")

if even_min == sys.maxsize:
    print(f"EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -sys.maxsize:
    print(f"EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")

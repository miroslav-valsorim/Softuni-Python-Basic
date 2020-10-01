number_one = int(input())
number_two = int(input())
symbol = str(input())

if symbol == "+":
    result = number_one + number_two

    if result % 2 == 0:
        print(f"{number_one} + {number_two} = {result} - even")
    else:
        print(f"{number_one} + {number_two} = {result} - odd")
elif symbol == "-":
    result = number_one - number_two

    if result % 2 == 0:
        print(f"{number_one} - {number_two} = {result} - even")
    else:
        print(f"{number_one} - {number_two} = {result} - odd")
elif symbol == "*":
    result = number_one * number_two
    if result % 2 == 0:
        print(f"{number_one} * {number_two} = {result} - even")
    else:
        print(f"{number_one} * {number_two} = {result} - odd")
elif symbol == "/":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one / number_two
        print(f"{number_one} / {number_two} = {result:.2f}")
elif symbol == "%":
    if number_two == 0:
        print(f"Cannot divide {number_one} by zero")
    else:
        result = number_one % number_two
        print(f"{number_one} % {number_two} = {result}")

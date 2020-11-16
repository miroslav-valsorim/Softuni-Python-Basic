MILL = 1 * 10 ** 6
ZERO = 0
ONE = 1

a = float(input())

if a < ZERO:
    print("negative")
elif a > ZERO:
    print("positive")
else:
    print("zero")

if abs(a) < ONE:
    print("small")
elif abs(a) > MILL:
    print("large")
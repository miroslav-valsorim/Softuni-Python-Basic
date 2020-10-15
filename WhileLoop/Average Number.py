n = int(input())

sum = 0
how_many = 0

while True:
    numbers = int(input())
    sum += numbers
    how_many += 1
    if how_many == n :
        sum /= how_many
        print(f"{sum:.2f}")
        break
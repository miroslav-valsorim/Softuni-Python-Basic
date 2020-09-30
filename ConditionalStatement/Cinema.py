type_cinema = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns

if type_cinema == "Premiere":
    income = cinema_capacity * 12.00
elif type_cinema == "Normal":
    income = cinema_capacity * 7.50
elif type_cinema == "Discount":
    income = cinema_capacity * 5.00
print(f"{income:.2f} leva")
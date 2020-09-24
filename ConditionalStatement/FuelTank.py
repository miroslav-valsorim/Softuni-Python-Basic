type_fuel = str(input())
how_much_fuel = float(input())

if type_fuel == "Diesel":
    if how_much_fuel >= 25:
        print(f"You have enough diesel.")
    elif how_much_fuel < 25:
        print(f"Fill your tank with diesel!")
elif type_fuel == "Gasoline":
    if how_much_fuel >= 25:
        print(f"You have enough gasoline.")
    elif how_much_fuel < 25:
        print(f"Fill your tank with gasoline!")
elif type_fuel == "Gas":
    if how_much_fuel >= 25:
        print(f"You have enough gas.")
    elif how_much_fuel < 25:
        print(f"Fill your tank with gas!")
else:
    print(f"Invalid fuel!")
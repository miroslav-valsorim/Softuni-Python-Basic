type_of_fuel = input()
quantity_of_fuel = float(input())
club_card = input()
gas_price = 0.93
gasoline_price = 2.22
diesel_price = 2.33
total_sum = 0
if club_card == "Yes":
    gas_price -= 0.08
    gasoline_price -= 0.18
    diesel_price -= 0.12
if type_of_fuel == "Gas":
    total_sum = gas_price * quantity_of_fuel
elif type_of_fuel == "Gasoline":
    total_sum = gasoline_price * quantity_of_fuel
elif type_of_fuel == "Diesel":
    total_sum = diesel_price * quantity_of_fuel
if 20 < quantity_of_fuel <= 25:
    total_sum *= 0.92
elif quantity_of_fuel > 25:
    total_sum *= 0.9
print(f"{total_sum:.2f} lv.")
number_of_cargo = int(input())

all_cargo = 0
cargo_price = 0
bus_price = 0
truck_price = 0
train_price = 0
cargo_bus = 0
cargo_truck = 0
cargo_train = 0

for cargo in range(1, number_of_cargo + 1):
    ton = int(input())
    all_cargo += ton

    if ton <= 3:
        cargo_price += ton * 200
        bus_price += ton * 200
        cargo_bus += ton
    elif 4 <= ton <= 11:
        cargo_price += ton * 175
        truck_price += ton * 175
        cargo_truck += ton
    elif ton >= 12:
        cargo_price += ton * 120
        train_price += ton * 120
        cargo_train += ton

cargo_price /= all_cargo

print(f"{cargo_price:.2f}")
print(f"{(cargo_bus / all_cargo * 100):.2f}%")
print(f"{(cargo_truck / all_cargo * 100):.2f}%")
print(f"{(cargo_train / all_cargo * 100):.2f}%")

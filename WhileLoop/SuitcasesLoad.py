boot_capacity = float(input())

entries = 0
capacity = 0
suitcases_inside = 0

command = input()
while command != "End":
    suitcases = float(command)
    entries += 1
    suitcases_inside += 1

    command = input()

    if entries % 3 == 0:
        capacity += suitcases + suitcases * 10 / 100
        if capacity > boot_capacity:
            print(f"No more space!")
            print(f"Statistic: {suitcases_inside - 1} suitcases loaded.")
            break
    else:
        capacity += suitcases
        if capacity > boot_capacity:
            print(f"No more space!")
            print(f"Statistic: {suitcases_inside - 1} suitcases loaded.")
            break

    if command == "End":
        print(f"Congratulations! All suitcases are loaded!")
        print(f"Statistic: {suitcases_inside} suitcases loaded.")
        break



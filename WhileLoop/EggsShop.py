egg_count = int(input())
command = ""
eggs_sold = 0
while command != "Close":
    command = input()
    if command == "Close":
        print(f'Store is closed!')
        print(f'{eggs_sold} eggs sold.')
        break
    order = int(input())
    if command == "Buy":
        if egg_count >= order:
            egg_count -= order
            eggs_sold += order
        else:
            print(f'Not enough eggs in store!')
            print(f'You can buy only {egg_count}.')
            break
    elif command == "Fill":
        egg_count += order
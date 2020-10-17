eggs_in_store = int(input())

sold = 0

while True:

    command = input()
    eggs = int(input())

    if command == "Fill":
        eggs_in_store += eggs
    elif command == "Buy":
        eggs_in_store -= eggs
        sold += eggs
        if eggs_in_store < 0:
            print(f"Not enough eggs in store!")
            print(f"You can buy only {eggs_in_store}")
            break

    if command == "Close":
        print(f"Store is closed!")
        print(f"{sold} eggs sold.")
        break
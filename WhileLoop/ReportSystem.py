money_expected = int(input())

entries = 0
cash = 0
card = 0
total = 0
people_cash = 0
people_card = 0

command = input()
while command != "End":
    money_entered = int(command)
    entries += 1

    if entries % 2 == 0:
        if money_entered < 10:
            print(f"Error in transaction!")
        else:
            card += money_entered
            total += money_entered
            people_card += 1
            print(f"Product sold!")
            if total >= money_expected:
                print(f"Average CS: {(cash / people_cash):.2f}")
                print(f"Average CC: {(card / people_card):.2f}")
                break

    else:
        if money_entered > 100:
            print(f"Error in transaction!")
        else:
            cash += money_entered
            total += money_entered
            people_cash += 1
            print(f"Product sold!")
            if total >= money_expected:
                print(f"Average CS: {(cash / people_cash):.2f}")
                print(f"Average CC: {(card / people_card):.2f}")
                break

    command = input()

if command == "End":
    print(f"Failed to collect required money for charity.")
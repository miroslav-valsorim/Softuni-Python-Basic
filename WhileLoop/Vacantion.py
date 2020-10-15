needed_money = float(input())
owned_money = float(input())

days_counted = 0
spending_days_counted = 0

while owned_money < needed_money and spending_days_counted < 5:
    command = input()
    money = float(input())
    days_counted += 1

    if command == "save":
        owned_money += money
        spending_days_counted = 0
    elif command == "spend":
        owned_money -= money
        spending_days_counted += 1
        if owned_money < 0:
            owned_money = 0

if spending_days_counted == 5:
    print(f"You can't save the money.")
    print(days_counted)

if owned_money >= needed_money:
    print(f"You saved the money for {days_counted} days.")

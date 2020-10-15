money = input()

total = 0

while money != "NoMoreMoney":
    increase = float(money)
    if increase > 0:
        print(f"Increase: {increase:.2f}")
    if increase < 0:
        print("Invalid operation!")
        break
    total += increase
    money = input()

print(f"Total: {total:.2f}")

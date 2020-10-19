day = int(input())
hours = int(input())

park_tax = 0
total_for_all_days = 0

for days in range(1, day + 1):
    total = 0
    for hours in range(1, hours + 1):
        if days % 2 == 0 and hours % 2 != 0:
            park_tax = 2.50
            total += 2.50
            total_for_all_days += 2.50
        elif days % 2 != 0 and hours % 2 == 0:
            park_tax = 1.25
            total += 1.25
            total_for_all_days += 1.25
        else:
            park_tax = 1
            total +=1
            total_for_all_days += 1
    print(f"Day: {days} - {total:.2f} leva")
print(f"Total: {total_for_all_days:.2f} leva")

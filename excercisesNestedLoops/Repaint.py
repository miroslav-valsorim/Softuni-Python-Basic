nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

total = (nylon + 2) * 1.50 + (paint + 0.10 * paint) * 14.50 + thinner * 5 + 0.40

pay_per_hour = total * 0.30
total_pay = hours * pay_per_hour

grand_total = total + total_pay

print(f"Total expenses: {grand_total:.2f} lv.")
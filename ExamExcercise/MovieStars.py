budget = float(input())

pay_slip = budget
payment = 0
noBudget = False

command = input()
while command != "ACTION":
    actor_name = command
    if len(actor_name) > 15:
        pay_slip -= pay_slip * 20 / 100
        command = input()
        continue

    payment = float(input())

    if pay_slip < payment:
        noBudget = True
        break
    elif pay_slip >= payment:
        pay_slip -= payment

    command = input()

if noBudget:
    diff = payment - pay_slip
    print(f"We need {abs(diff):.2f} leva for our actors.")
if command == "ACTION":
    print(f"We are left with {pay_slip:.2f} leva.")
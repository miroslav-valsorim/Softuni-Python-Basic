persons_age = float(input())
persons_gender = input()

if persons_gender == "m":
    if persons_age >= 16:
        print("Mr.")
    else:
        print("Master")
elif persons_gender == "f":
    if persons_age >= 16:
        print("Ms.")
    else:
        print("Miss")

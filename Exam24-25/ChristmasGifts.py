command = input()

kids = 0
adults = 0

while command != "Christmas":
    peoples_age = int(command)

    if peoples_age <= 16:
        kids += 1
    elif peoples_age > 16:
        adults += 1
    command = input()

if command == "Christmas":
    total_toys_price = kids * 5
    total_sweater_price = adults * 15
    print(f"Number of adults: {adults}")
    print(f"Number of kids: {kids}")
    print(f"Money for toys: {total_toys_price}")
    print(f"Money for sweaters: {total_sweater_price}")
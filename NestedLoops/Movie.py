movie = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
all_tickets = 0

while movie != "Finish":
    total_spots = int(input())

    ticket = input()
    while ticket != "End":
        all_tickets += 1
        if ticket == "student":
            student_tickets += 1
        elif ticket == "standard":
            standard_tickets += 1
        elif ticket == "kid":
            kid_tickets += 1

        ticket = input()
    else:
        print(f"{movie}-{((all_tickets / total_spots)*100):.2f}% full.")

    movie = input()
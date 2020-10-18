movie = input()

student_tickets = 0
standard_tickets = 0
kid_tickets = 0
all_tickets = 0
people_in_the_hall = 0

while movie != "Finish":
    total_spots = int(input())
    ticket = input()
    while ticket != "End":
        people_in_the_hall += 1
        all_tickets += 1
        if ticket == "student":
            student_tickets += 1
        elif ticket == "standard":
            standard_tickets += 1
        elif ticket == "kid":
            kid_tickets += 1
        if total_spots == people_in_the_hall:
            break

        ticket = input()
    print(f"{movie} - {(people_in_the_hall / total_spots * 100):.2f}% full.")
    people_in_the_hall = 0
    film = input()
print(f"Total tickets: {all_tickets}")
print(f"{(student_tickets / all_tickets * 100):.2f}% student tickets.")
print(f"{(standard_tickets / all_tickets * 100):.2f}% standard tickets.")
print(F"{(kid_tickets / all_tickets * 100):.2f}% kids tickets.")
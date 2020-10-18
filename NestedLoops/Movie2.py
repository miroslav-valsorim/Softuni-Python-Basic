film = input()
people_in_the_hall = 0
student = 0
standard = 0
kid = 0
all_people = 0
while film != "Finish":
    hall_capacity = int(input())
    watcher = input()
    while watcher != "End":
        people_in_the_hall += 1
        all_people += 1
        if watcher == "kid":
            kid += 1
        elif watcher == "student":
            student += 1
        elif watcher == "standard":
            standard += 1
        if hall_capacity == people_in_the_hall:
            break
        watcher = input()
    print(f"{film} - {(people_in_the_hall / hall_capacity * 100):.2f}% full.")
    people_in_the_hall = 0
    film = input()
print(f"Total tickets: {all_people}")
print(f"{(student / all_people * 100):.2f}% student tickets.")
print(f"{(standard / all_people * 100):.2f}% standard tickets.")
print(F"{(kid / all_people * 100):.2f}% kids tickets.")
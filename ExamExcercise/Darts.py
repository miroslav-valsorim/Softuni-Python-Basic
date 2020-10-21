name = input()

total_points = 301
points_for_current_shot = 0
successful_shots = 0
unsuccessful_shots = 0

word_input = input()
while word_input != "Retire":
    command = word_input
    points = int(input())

    if command == "Single":
        points_for_current_shot = points
    elif command == "Double":
        points_for_current_shot = points * 2
    elif command == "Triple":
        points_for_current_shot = points * 3

    if points_for_current_shot <= total_points:
        successful_shots +=1
        total_points -= points_for_current_shot

    elif total_points < points_for_current_shot:
        unsuccessful_shots += 1

    if total_points == 0:
        print(f"{name} won the leg with {successful_shots} shots.")
        break

    word_input = input()
if word_input == "Retire":
    print(f"{name} retired after {unsuccessful_shots} unsuccessful shots.")
number_of_people_in_gym = int(input())

back = 0
chest = 0
legs = 0
abs = 0
protein_shake = 0
protein_bar = 0

people_training = 0
people_on_bar = 0

for people in range(1, number_of_people_in_gym + 1):
    service = input()

    if service == "Back":
        back += 1
        people_training += 1
    elif service == "Chest":
        chest += 1
        people_training += 1
    elif service == "Legs":
        legs += 1
        people_training += 1
    elif service == "Abs":
        abs += 1
        people_training += 1
    elif service == "Protein shake":
        protein_shake += 1
        people_on_bar += 1
    elif service == "Protein bar":
        protein_bar += 1
        people_on_bar += 1

print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(people_training / number_of_people_in_gym) * 100 :.2f}% - work out")
print(f"{(people_on_bar / number_of_people_in_gym) * 100 :.2f}% - protein")

name = input()

class_school = 1
sum_of_grades = 0
ejected = False
failed = 0

while True:
    grade = float(input())
    if grade >= 4.00:
        sum_of_grades += grade
        if class_school == 12:
            break
        class_school += 1
    else:
        failed += 1
        if failed == 2:
            ejected = True
            break

if ejected:
    print(f"{name} has been excluded at {class_school} grade")
else:
    average = sum_of_grades / class_school
    print(f"{name} graduated. Average grade: {average:.2f}")


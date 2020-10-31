number_of_students = int(input())

top_student = 0
btw_four = 0
btw_three = 0
fail = 0
total = 0

for students in range(1, number_of_students + 1):
    grade = float(input())

    total += grade

    if grade >= 5:
        top_student += 1
    elif 4 <= grade <= 4.99:
        btw_four += 1
    elif 3 <= grade <= 3.99:
        btw_three += 1
    else:
        fail += 1

print(f"Top students: {((top_student / number_of_students) * 100):.2f}%")
print(f"Between 4.00 and 4.99: {((btw_four / number_of_students) * 100):.2f}%")
print(f"Between 3.00 and 3.99: {((btw_three / number_of_students) * 100):.2f}%")
print(f"Fail: {((fail / number_of_students) * 100):.2f}%")
print(f"Average: {(total / number_of_students):.2f}")
number_of_students = int(input())

total_grade = 0
top_stud = 0
btw_three = 0
btw_four = 0
failed = 0

for students in range(1, number_of_students + 1):
    grade = float(input())

    if 2 <= grade <= 2.99:
        total_grade += grade
        failed += 1
    elif 3 <= grade <= 3.99:
        total_grade += grade
        btw_three += 1
    elif 4 <= grade <= 4.99:
        total_grade += grade
        btw_four += 1
    elif grade >= 5:
        total_grade += grade
        top_stud += 1

average = total_grade / number_of_students

print(f"Top students: {(top_stud / number_of_students * 100):.2f}%")
print(f"Between 4.00 and 4.99: {(btw_four / number_of_students* 100):.2f}%")
print(f"Between 3.00 and 3.99: {(btw_three / number_of_students * 100):.2f}%")
print(f"Fail: {(failed / number_of_students * 100):.2f}%")
print(f"Average: {average:.2f}")

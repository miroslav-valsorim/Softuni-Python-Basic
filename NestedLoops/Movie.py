total_sold_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

command = input()
while command != "Finish":
    movie_name = command
    tickets_for_sale = int(input())
    sold_tickets_for_current_move = 0
    while sold_tickets_for_current_move < tickets_for_sale:
        type_of_tickets = input()
        if type_of_tickets == "End":
            break
        elif type_of_tickets == "student":
            student_tickets += 1
        elif type_of_tickets == "standard":
            standard_tickets += 1
        elif type_of_tickets == "kid":
            kid_tickets += 1
        sold_tickets_for_current_move += 1
        total_sold_tickets += 1
    percentage_of_full_hall = sold_tickets_for_current_move / tickets_for_sale * 100
    print(f"{movie_name} - {percentage_of_full_hall:.2f}% full.")

    command = input()

percent_of_student = student_tickets / total_sold_tickets * 100
percent_of_standard = standard_tickets / total_sold_tickets * 100
percent_of_kid = kid_tickets / total_sold_tickets * 100

print(f"Total tickets: {total_sold_tickets}")
print(f"{percent_of_student:.2f}% student tickets.")
print(f"{percent_of_standard:.2f}% standard tickets.")
print(f"{percent_of_kid:.2f}% kids tickets.")
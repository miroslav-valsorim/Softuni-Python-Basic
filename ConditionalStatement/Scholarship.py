from math import floor

salary = float(input())
middle_rating = float(input())
minimal_salary = float(input())

social_scholarship = minimal_salary * 0.35
excellent_scholarship = middle_rating * 25

if middle_rating >= 5.50:
    if salary < minimal_salary:
        if excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
        else:
            print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
    else:
        print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")
elif middle_rating >= 4.50:
    if salary < minimal_salary:
        print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
    else:
        print(f"You cannot get a scholarship!")
else:
    print(f"You cannot get a scholarship!")


result_one = input()
result_two = input()
result_three = input()

wins = 0
draws = 0
loses = 0

first_one = int(result_one[0])
first_two = int(result_one[2])

second_one = int(result_two[0])
second_two = int(result_two[2])

third_one = int(result_three[0])
third_two = int(result_three[2])


if first_one > first_two:
    wins += 1
elif first_one == first_two:
    draws += 1
elif first_one < first_two:
    loses += 1

if second_one > second_two:
    wins += 1
elif second_one == second_two:
    draws += 1
elif second_one < second_two:
    loses += 1

if third_one > third_two:
    wins += 1
elif third_one == third_two:
    draws += 1
elif third_one < third_two:
    loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")
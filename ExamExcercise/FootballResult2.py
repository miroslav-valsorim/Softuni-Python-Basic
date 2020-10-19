wins = 0
draws = 0
loses = 0

for games in range(3):
    results = input()

    first_one = int(results[0])
    first_two = int(results[2])

    if first_one > first_two:
        wins += 1
    elif first_one == first_two:
        draws += 1
    elif first_one < first_two:
        loses += 1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f"Drawn games: {draws}")
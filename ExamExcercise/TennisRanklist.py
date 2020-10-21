from math import floor
tournaments_played = int(input())
starting_points = int(input())

summ_of_points = starting_points
wins = 0

for tournaments in range(1, tournaments_played + 1):
    tournament_table = input()

    if tournament_table == "W":
        summ_of_points += 2000
        wins += 1
    elif tournament_table == "F":
        summ_of_points += 1200
    elif tournament_table == "SF":
        summ_of_points += 720

average = (summ_of_points - starting_points) / tournaments_played
total_wins = (wins / tournaments_played) * 100

print(f"Final points: {summ_of_points}")
print(f"Average points: {floor(average)}")
print(f"{total_wins:.2f}%")
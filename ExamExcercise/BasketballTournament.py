tournament = input()

total_played = 0
total_won = 0
total_lost = 0

while tournament != "End of tournaments":
    games_per_tournament = int(input())
    games_counter = 0
    total_played += games_per_tournament

    for games in range(1, games_per_tournament + 1):
        desi_team = int(input())
        other_team = int(input())
        games_counter += 1
        if desi_team > other_team:
            total_won += 1
            diff = desi_team - other_team
            print(f"Game {games_counter} of tournament {tournament}: win with {diff} points.")
        elif desi_team < other_team:
            total_lost += 1
            diff = other_team - desi_team
            print(f"Game {games_counter} of tournament {tournament}: lost with {diff} points.")

    tournament = input()

if tournament == "End of tournaments":
    print(f"{((total_won / total_played) * 100):.2f}% matches win")
    print(f"{((total_lost / total_played) * 100):.2f}% matches lost")
from math import floor

year_type = input()
holidays_per_year = int(input())
weekends_per_year = int(input())

weekends_in_sofia = 48 - weekends_per_year
games_in_sofia = weekends_in_sofia * 3 / 4

games_in_sofia_holiday = holidays_per_year * 2 / 3

all_games = games_in_sofia_holiday + games_in_sofia + weekends_per_year

if year_type == "leap":
    leap_play = all_games - all_games * 85 / 100
    leap_year = leap_play + all_games
    print(floor(leap_year))
elif year_type == "normal":
    print(floor(all_games))
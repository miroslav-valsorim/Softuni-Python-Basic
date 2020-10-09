minutes_walk = int(input())
daily_walks = int(input())
calories_for_day = int(input())

calorie_for_minute = 5

daily_walk_in_minutes = minutes_walk * daily_walks
calories_burned = daily_walk_in_minutes * calorie_for_minute

if calories_burned >= calories_for_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burned}.")
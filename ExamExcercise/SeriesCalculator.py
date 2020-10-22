from math import floor
series_name = input()
seasons = int(input())
episodes = int(input())
episode_without_advertising = float(input())

advertising_time = episode_without_advertising - episode_without_advertising * 80 / 100
episode_with_advertising = episode_without_advertising + advertising_time
special_episodes_time = seasons * 10
total_time_for_watching = episode_with_advertising * episodes * seasons + special_episodes_time

print(f"Total time needed to watch the {series_name} series is {floor(total_time_for_watching)} minutes.")
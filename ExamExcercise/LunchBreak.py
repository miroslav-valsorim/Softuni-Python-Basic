import math
from math import floor

series_name = input()
time_for_episode = int(input())
rest_time = int(input())

lunch_time = rest_time / 8
rest = rest_time / 4
time_left = rest_time - lunch_time - rest

diff = time_left - time_for_episode
if time_left >= time_for_episode:
    print(f"You have enough time to watch {series_name} and left with {abs(math.ceil(diff))} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {abs(floor(diff))} more minutes.")
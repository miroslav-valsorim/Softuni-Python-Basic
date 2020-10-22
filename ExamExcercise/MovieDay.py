from math import ceil
from math import floor

time_for_photos = int(input())
number_of_scenes = int(input())
time_on_scene = int(input())

preparation = time_for_photos * 0.15
time_for_shooting = number_of_scenes * time_on_scene
time_needed = time_for_shooting + preparation

diff = time_needed - time_for_photos
if time_needed <= time_for_photos:
    print(f"You managed to finish the movie on time! You have {abs(floor(diff))} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {abs(floor(diff))} minutes.")
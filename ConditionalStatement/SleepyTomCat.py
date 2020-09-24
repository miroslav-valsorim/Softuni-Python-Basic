rest_days = int(input())
play_time_needed = 30000

work_days = 365 - rest_days
play_rest = rest_days * 127
play_work = work_days * 63

hours_both = play_rest + play_work

if play_time_needed > hours_both:
    time_left = play_time_needed - hours_both

    hours = time_left // 60
    minutes = time_left % 60

    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    time_left = hours_both - play_time_needed

    hours = time_left // 60
    minutes = time_left % 60

    print(f"Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")
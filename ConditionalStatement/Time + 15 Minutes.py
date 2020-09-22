hours_entered = int(input())
minutes_entered = int(input())
real_minutes = minutes_entered + 15
real_time = hours_entered * 60 + real_minutes
hours_after_fifteen_minutes = real_time // 60
minutes_after_fifteen_minutes = real_time % 60
if hours_after_fifteen_minutes > 23:
    hours_after_fifteen_minutes -= 24
if minutes_after_fifteen_minutes < 10:
    print(f"{hours_after_fifteen_minutes}:0{minutes_after_fifteen_minutes}")
else:
    print(f"{hours_after_fifteen_minutes}:{minutes_after_fifteen_minutes}")

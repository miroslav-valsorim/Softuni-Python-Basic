minutes_control = int(input())
seconds_control = int(input())
length_in_meters = float(input())
seconds_for_hundred_meters = int(input())

control_in_seconds = (minutes_control * 60) + seconds_control
slowing = length_in_meters / 120
total_slowing = slowing * 2.5
marians_time = (length_in_meters / 100) * slowing - total_slowing

if control_in_seconds >= marians_time:
    print(f"Marin Bangiev won an Olympic quota!")
    print(f"His time is {marians_time:.3f}.")
else:
    diff = marians_time - control_in_seconds
    print(f"No, Marin failed! He was {abs(diff):.2f} second slower.")
import math
record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_meter = float(input())
swimming_distance = distance_in_meters * time_in_seconds_for_meter
slowing = math.floor(distance_in_meters / 15) * 12.5
total_time = swimming_distance + slowing
if record_in_seconds <= total_time:
    total_other_time = total_time - record_in_seconds
    print(f"No, he failed! He was {abs(total_other_time):.2f} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {abs(total_time):.2f} seconds.")

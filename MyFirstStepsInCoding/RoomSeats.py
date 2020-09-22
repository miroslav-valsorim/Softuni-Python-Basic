h = float(input())
w = float(input())
w_in_cm = w * 100
h_in_cm = h * 100
corridor = 100
w_left = w_in_cm - corridor
w_spots = w_left // 70
h_spots = h_in_cm // 120
all_spots = w_spots * h_spots -3
print(all_spots)


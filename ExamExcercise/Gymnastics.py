country = input()
sport = input()

hardness = 0
performance = 0

if country == "Russia":
    if sport == "ribbon":
        hardness = 9.100
        performance = 9.400
    elif sport == "hoop":
        hardness = 9.300
        performance = 9.800
    elif sport == "rope":
        hardness = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if sport == "ribbon":
        hardness = 9.600
        performance = 9.400
    elif sport == "hoop":
        hardness = 9.550
        performance = 9.750
    elif sport == "rope":
        hardness = 9.500
        performance = 9.400
elif country == "Italy":
    if sport == "ribbon":
        hardness = 9.200
        performance = 9.500
    elif sport == "hoop":
        hardness = 9.450
        performance = 9.350
    elif sport == "rope":
        hardness = 9.700
        performance = 9.150

total = hardness + performance
points_left = 20 - total
percentage = (points_left / 20) * 100
print(f"The team of {country} get {total:.3f} on {sport}.")
print(f"{percentage:.2f}%")

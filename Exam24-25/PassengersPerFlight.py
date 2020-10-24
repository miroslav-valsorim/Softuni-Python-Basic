import sys
from math import floor
number_of_flights = int(input())

maximum_passengers = -sys.maxsize
maximum_pass_name = ""
entries = 0

for flights in range(1, number_of_flights + 1):
    flight_company = input()
    entries += 1

    total_passengers_per_company = 0
    number_of_current_flights = 0
    average = 0

    command = input()
    while command != "Finish":

        number_of_passengers = int(command)
        number_of_current_flights += 1
        total_passengers_per_company += number_of_passengers
        average = total_passengers_per_company / number_of_current_flights
        if average > maximum_passengers:
            maximum_passengers = average
            maximum_pass_name = flight_company

    if command == "Finish":
        print(f"{flight_company}: {floor(average)} passengers.")
        if entries == number_of_flights:
            break

        command = input()

    if entries == number_of_flights:
        print(f"{maximum_pass_name} has most passengers per flight: {floor(maximum_passengers)}")
        break




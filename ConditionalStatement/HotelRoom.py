#	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
#	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
#	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
#	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.

month = input()
nights = int(input())

studio = 0
apartment = 0

if month == "May" or month == "October":
    if 7 < nights <= 14:
        studio = 50 - 50 * 5 / 100
        apartment = 65
        price_studio = studio * nights
        price_apartment = apartment * nights
    elif nights > 14:
        studio = 50 - 50 * 30 / 100
        apartment = 65 - 65 * 10 / 100
        price_studio = studio * nights
        price_apartment = apartment * nights
    else:
        studio = 50
        apartment = 65
        price_studio = studio * nights
        price_apartment = apartment * nights

elif month == "June" or month == "September":
    if nights > 14:
        studio = 75.20 - 75.20 * 20 / 100
        apartment = 68.70 - 68.70 * 10 / 100
        price_studio = studio * nights
        price_apartment = apartment * nights
    else:
        studio = 75.20
        apartment = 68.70
        price_studio = studio * nights
        price_apartment = apartment * nights

elif month == "July" or month == "August":
    if nights > 14:
        studio = 76
        apartment = 77 - 77 * 10 / 100
        price_studio = studio * nights
        price_apartment = apartment * nights
    else:
        studio = 76
        apartment = 77
        price_studio = studio * nights
        price_apartment = apartment * nights

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
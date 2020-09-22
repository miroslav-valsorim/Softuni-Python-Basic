movie_budget = float(input())
statist = int(input())
price_clothes = float(input())
movie_decor = movie_budget - movie_budget * 90 / 100
clothes = statist * price_clothes
all_clothes = 0
last_price = 0
if statist > 150:
    all_clothes = clothes - clothes * 10 / 100
    last_price = all_clothes + movie_decor
    price = last_price - movie_budget
    if last_price > movie_budget:
        print(f'Not enough money!')
        print(f'Wingard needs {abs(price):.2f} leva more.')
    elif last_price <= movie_budget:
        print(f'Action!')
        print(f'Wingard starts filming with {abs(price):.2f} leva left.')
else:
    all_clothes = clothes
    last_price = all_clothes + movie_decor
    price = last_price - movie_budget
    if last_price > movie_budget:
        print(f'Not enough money!')
        print(f'Wingard needs {abs(price):.2f} leva more.')
    elif last_price <= movie_budget:
        print(f'Action!')
        print(f'Wingard starts filming with {abs(price):.2f} leva left.')



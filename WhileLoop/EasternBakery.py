price_for_kg_of_flour = float(input())
kg_of_flour = float(input())
kg_of_sugar = float(input())
number_of_egg_card = int(input())
packet_of_may = int(input())

price_for_kg_of_sugar = price_for_kg_of_flour - price_for_kg_of_flour * 25 / 100
price_for_pack_of_eggs = price_for_kg_of_flour + price_for_kg_of_flour * 10 / 100
price_for_pack_of_may = price_for_kg_of_sugar - price_for_kg_of_sugar * 80 / 100

money_for_flour = price_for_kg_of_flour * kg_of_flour
money_for_sugar = price_for_kg_of_sugar * kg_of_sugar
money_for_eggs = price_for_pack_of_eggs * number_of_egg_card
money_for_may = price_for_pack_of_may * packet_of_may

sum_of_all = money_for_flour + money_for_sugar + money_for_eggs + money_for_may
print(f"{sum_of_all:.2f}")
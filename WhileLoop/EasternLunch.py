# Козунак – 3.20 лв.
# Яйца – 4.35 лв. за кора с 12 яйца
# Курабии – 5.40 лв. за килограм
# Боя за яйца - 0.15 лв. за яйце

number_of_kozunak = int(input())
number_of_eggs = int(input())
kg_of_kurabii = int(input())

kozunak_price = 3.20
egg_price = 4.35
kurabii_price = 5.40
paint_for_eggs = 0.15

price_for_kozunaks = number_of_kozunak * kozunak_price
price_for_eggs = number_of_eggs * egg_price
price_for_kurabii = kg_of_kurabii * kurabii_price
price_for_paint = ( number_of_eggs * 12 ) * paint_for_eggs

sum = price_for_kozunaks + price_for_eggs + price_for_kurabii + price_for_paint

print(f"{sum:.2f}")
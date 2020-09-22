vege_kg_price = float(input())
fruit_kg_price = float(input())
all_vege_kg = int(input())
all_fruit_kg = int(input())

vege_price = vege_kg_price * all_vege_kg
fruit_price = fruit_kg_price * all_fruit_kg
all = vege_price + fruit_price
euro_price = all / 1.94
print(f'{euro_price:.2f}')
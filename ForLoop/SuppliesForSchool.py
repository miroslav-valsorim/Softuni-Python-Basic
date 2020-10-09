package_of_pens = int(input())
package_of_markers = int(input())
liters_of_liquid = float(input())
discount_percentage = int(input())

pens = 5.80
marker = 7.20
liquid = 1.20

price_for_pens = package_of_pens * pens
price_for_markers = package_of_markers * marker
price_for_liquid = liters_of_liquid * liquid
price_for_all = price_for_pens + price_for_markers + price_for_liquid
price_with_discount = price_for_all - price_for_all * discount_percentage / 100

print(f"{price_with_discount:.3f}")
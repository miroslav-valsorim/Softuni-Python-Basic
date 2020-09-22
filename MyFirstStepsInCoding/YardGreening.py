square_meters = float(input())
real_price = square_meters * 7.61
discount = 0.18 * real_price
discounted_price = real_price - discount
print(f"The final price is : {discounted_price} lv" )
print(f"The discount is : + {discount} lv")
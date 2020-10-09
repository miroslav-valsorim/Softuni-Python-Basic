bitcoin = int(input())
uan = float(input())
percentage = float(input())

one_bitcoin_value = 1168
one_uan_value = 0.15
one_dollar = 1.76
one_euro = 1.95

bitcoin_entered = bitcoin * one_bitcoin_value
uan_entered = uan * one_uan_value
uan_converted_to_lev = uan_entered * one_dollar
leva_sum = bitcoin_entered + uan_converted_to_lev
euro_sum = leva_sum / one_euro
euro_minus_percentage = euro_sum - euro_sum * percentage / 100

print(f"{euro_minus_percentage:.2f}")
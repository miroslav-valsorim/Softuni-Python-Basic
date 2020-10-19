# при добавен мобилен интернет, към таксата за един месец се добавя:
# при такса по-малка или равна на 10.00 лв. → 5.50 лв.
# при такса по-малка или равна на 30.00 лв. → 4.35 лв.
# при такса по-голяма от 30.00 лв. → 3.85 лв.
# ако договорът e за две години, общата сума се намалява с 3.75%

term_of_contract = input()
type_of_contract = input()
internet = input()
number_of_months_payment = int(input())

plan = 0

if term_of_contract == "one":
    if type_of_contract == "Small":
        plan = 9.98
    elif type_of_contract == "Middle":
        plan = 18.99
    elif type_of_contract == "Large":
        plan = 25.98
    elif type_of_contract == "ExtraLarge":
        plan = 35.99
elif term_of_contract == "two":
    if type_of_contract == "Small":
        plan = 8.58
    elif type_of_contract == "Middle":
        plan = 17.09
    elif type_of_contract == "Large":
        plan = 23.59
    elif type_of_contract == "ExtraLarge":
        plan = 31.79

net = 0
if internet == "yes":
    if plan <= 10:
        net = 5.50
    elif plan <= 30:
        net = 4.35
    elif plan > 30:
        net = 3.85
else:
    net = 0

both = plan + net
discount = 0

if term_of_contract == "two":
    discount = both - both * 3.75 / 100
else:
    discount = both

last = discount * number_of_months_payment
print(f"{last:.2f} lv.")
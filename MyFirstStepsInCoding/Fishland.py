mackerel = float(input())
sprat = float(input())
bonito = float(input())
scad = float(input())
clam = int(input())
clam_price = 7.50

bonito_price = mackerel + mackerel * 60 / 100
last_bonito_price = bonito_price * bonito
scad_price = sprat + sprat * 80 / 100
last_scad_price = scad_price * scad
last_clam_price = clam_price * clam
bill = last_bonito_price + last_scad_price + last_clam_price
print(f'{bill:.2f}')


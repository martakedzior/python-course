# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.


mileage_per_100 = 6.4
distans = 120
price_of_gas = 5.04
price_of_trip = mileage_per_100 * distans/100 * price_of_gas

print(f"koszt_wyprawy to {round(price_of_trip,2)}")
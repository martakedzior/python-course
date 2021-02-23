# Oblicz koszt wyprawy znając dystans, spalanie na 100km i cenę litra benzyny.
# Załóżmy, że spalanie na 100km wynosi 6,4 l, trasa to 120km, litr benzyny kosztuje 5,04 zł.

print("Please provide values for:")
mileage_per_100 = float(input("Mileage per 100 km: "))
distans = float(input("Distance in kilometers: "))
price_of_gas = float(input("Price of gas: "))
price_of_trip = mileage_per_100 * distans/100 * price_of_gas

print(f"Price of the trip is:  {round(price_of_trip,2)}")
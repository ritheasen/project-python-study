cusName = (input("Enter your name: "))
units = int(input("Enter your amount of units: "))

if units >= 500:
    price = 3500
    print("Price per unit: 3500Riel")
elif units > 400:
    price = 3100
    print("Price per unit: 3100Riel")
elif units > 300:
    price = 2750
    print("Price per unit: 2750Riel")
elif units > 200:
    price = 1800
    print("Price per unit: 1800Riel")
else:
    price = 720
    print("Price per unit: 720Riel")

print("Customer name: " + cusName)
print("Price per units :" + str(price) + "Riel")
print("Total units consumed by customer :" + str(units) + "units")
print("Total amount payable:" + str(units * price) + "Riel")
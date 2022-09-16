package_weight = int(input("Enter the weight of your package in pound "))
shipping_charge = 0

if package_weight <= 2:
    shipping_charge = 1.50
elif package_weight > 2 and package_weight <= 6:
    shipping_charge = 3.00
elif package_weight > 6 and package_weight <= 10:
    shipping_charge = 4.00
elif package_weight > 10:
    shipping_charge = 4.75
print("The shipping charges is $", shipping_charge)        


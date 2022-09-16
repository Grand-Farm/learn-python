package_price = 99
quantity = int(input("Enter number of packages purchased "))
discount = 0
total = 0

if quantity >= 10 and quantity <= 19:
    discount = package_price * 0.10
    total = package_price - discount
    print("You have a discount of $", discount, sep="")
    
elif quantity >= 20 and quantity <= 49:
    discount = package_price * 0.20
    total = package_price - discount
    print("You have a discount of $", discount, sep="")

elif quantity >= 50 and quantity <= 99:
    discount = package_price * 0.30
    total = package_price - discount
    print("You have a discount of $", discount, sep="")
elif quantity >= 100:
    discount = package_price * 0.40
    total = package_price - discount
    print("You have a discount of $", discount, sep="")
else:
    print("Not discount applied")    
    
print("The total amount of the purchase after the discount is $", total, sep="" )


    

user_weight = float(input("Enter your weight in in Pound "))
user_height = float(input("Enter your height in Inches "))
body_mass = (user_weight * 703) / (user_height * user_height)

if body_mass >= 18.5 and body_mass <= 25:
    print("This is considered optimal")
elif body_mass < 18.5:
    print("This is considered underweight")
elif body_mass > 25:
    print("This is considered overweight")   
print("Your Body Mass Index is", int(body_mass))          
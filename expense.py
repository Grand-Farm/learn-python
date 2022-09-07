from os import sep
# follow your expensive. 
expensives = []
total = 0
number_expensive = 5
for expensive in range(number_expensive):
    expensives.append(int(input("Amount spend in item: ")))
    total = sum(expensives)
    discount = total * 7 /100
    total2 = total - discount
    print("the total you spend is $", total, sep="")
    print("the total after sales tax of 7 percent is $", total2, sep="")

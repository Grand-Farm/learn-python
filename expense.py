from os import sep
# follow your expensive. 
expensives = []
total = 0
expensives.append(int(input("Amount spend in item: ")))
expensives.append(int(input("Amount spend in item: ")))
expensives.append(int(input("Amount spend in item: ")))
expensives.append(int(input("Amount spend in item: ")))
expensives.append(int(input("Amount spend in item: ")))
total = sum(expensives)
tax = total * 7 /100
total2 = total + tax
print("the total you spend is $", total, sep="")
print("the total after sales tax of 7 percent is $", total2, sep="")

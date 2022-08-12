from os import sep
# follow your expensive. 
expensives = []
total = 0
number_expensive = int(input("how many time you spend money?: "))
for expensive in range(number_expensive):
    expensives.append(int(input("Amount spend: ")))
    total = sum(expensives)
    print("the total you spend is $", total, sep="")

levelocean = 0
year = 0
while year < 25:
    levelocean += 1.6
    print("risen by", float(levelocean),"millimeters", "after", year +1, "year" )
    year += 1


tuition = 8000.0
for year in range(1, 6):
    tuition *= 1.03
    if year == 1:
        print("In ",year, "year, the tuition will be $", tuition)
    else:
        print("In ",year, "year, the tuition will be $", tuition)



number = int(input("Enter number integer:"))
while number<0:
   number = int(input("Enter number integer:"))
factorial = 1
for num in range(1,number+1):
   factorial = factorial * num
print(factorial)

start_number = int(input("Starting number of organisms: "))
increase_number = float(input("Average daily increase: "))
number_day = int(input("Number of days to multiply: "))
print("Day Approximate\tPopulation")
for d in range(start_number, number_day + 1):
    add = start_number * increase_number
    start_number = start_number + add
    print(number_day - 1, '\t', start_number)

rows = 6

for i in range(1, rows):
   
    for j in range(1, i + 1):
        print("#", end=" ")
    print('') 
number = 0
while number < 100:
    number += 2
    print(number)

numbers = 100

for number in range(1, numbers + 1):
    if(number % 2 == 0):

      print(number)

# event number from to 100 with for loop and while loop.

end = 10
for number in range(1, end+1):
   print (number)

student = 1
while student <= 3:
     total = 0
     for score in range (1,4):
          score = int(input("Enter test score: "))
          total += score
     average = total/3
     print("Student ", student, "average: ", average)
     student += 1

for num in range(0, 20, 5):
   num += num
print(num)     


total = 0
for count in range(1,4):
   total += count
   print(total)

count = 4
while count < 12:
   print("counting")
   count = count + 2


for minutes in range (60):
   for seconds in range (60):
      print (minutes, ':', seconds)

count = 0

while count < 10:
   print(count)
   count += 2


num = 0
for num in range(2, 9, 2):
    print(num)

for row in range(5):
    for col in range(3):
        print('*', end='')
    print()

for i in range(3, 12, 1):
      if i%2 != 0:
            print(i, end = " ")

for r in range (1, 3):
   for c in range (1, 2):
       print (c, end = '')
   print()

n = 2
while n < 6:
   n += 1
   print(n, end = " ")   

total = 0
for number in range (1, 6):
    total += number
print(total)
num = 0
for num in range(4):
    print(num)
for num in range(1, 5):
    print(num)

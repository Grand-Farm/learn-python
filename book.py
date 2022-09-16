number_book = int(input("Enter number of books purchases this month "))
earn_point = 0

if number_book == 0:
    earn_point = 0
elif number_book == 2:
    earn_point = 5
elif number_book == 4:
    earn_point = 15
elif number_book == 6:
    earn_point = 30
else:
    earn_point = 60 
print("You earned ", earn_point, "points")              

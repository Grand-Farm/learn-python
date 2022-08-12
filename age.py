from os import sep
# Find how old you are
birthYear = int(input("enter year of birth: "))
yearNow = int(input("enter current year: "))
age = yearNow - birthYear
print("You are ", str(age), " year old.", sep="")

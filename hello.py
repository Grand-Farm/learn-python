def kinetic_energy(m, v):
    z = 1/2 * m * v * v
    return(z) 

num1 = int(input("Enter the mass in kilogram "))
num2 = int(input("Enter the velocity in meter "))
answer = kinetic_energy(num1, num2)
print(answer)

import math

def Future(p,i,t):
    f = p*(math.pow((1+i),t))
    return f
p = float(input("Enter bank balance: ")) 
i = float(input("Enter  interest rate: ")) 
t = int(input("Enter number of months: "))  
total = Future(p,i,t)
print("future value: ", total)

import random

def main():
  
    number = input("I have a number between 1 and 1000. Can you guess my number? Please type your first guess: ")
    guess(number)

def guess(number1):
   
    randomNumber = random.randrange(1, 100)
   
    correct = False
    while not correct:
        if number1 > randomNumber:
            print ("Too high. Try again.")
       
        elif number1 < randomNumber:
            print ("Too low. Try again.")
          
        elif number1 == randomNumber:
           break
        number1 = input ("What number do you guess? ")
    if number1 == randomNumber:
       playAagain = raw_input("Excellent! You guessed the number! Would you like to play again (y or n)? ")
       if playAagain == "y":
            main()

main()

import random
c={1:"rock",2:"paper",3:"scissors"}
comp=random.randint(1,3)
print(c[comp])
while True:
    player=int(input("(1= rock) (2= paper) (3= scissors) Enter your a number according to the choice= "))
    if player==comp:
        continue
    elif player not in range(1,4):
        print("Invalid input, enter again")
    elif (player==1 and comp==2) or (player==2 and comp==3) or (player==3 and comp==1):
        print("Computer wins")
        break
    else:
        print("You win")
        break
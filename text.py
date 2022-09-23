s1 = "Welcome"
print (s1[-4 : ])

print (s1[3 : ])

print (s1)

print (s1[ : ])

print (len(s1) - 1)
import random
import math

print(chr(random.randint(0, 127)))
print(chr(random.randint(ord('a'), ord('z'))))

area = math.pow(4, 3)
print(area)

print("""The cat said "meow".""")

print('The cat said "meow".')

print("The cat said 'meow'.")

print("The cat said \"meow\".")

print('''The cat said "meow".''')

print(3.246)
print(format(3.246,'.2f'))
print(format(0.2 * 100, '.0%'))
print(format(0.2, '%'))

print(format(20, '.0%'))

print(format(0.2, '.0%'))

s1 = "Welcome to Hcc"
r1 = "HCC" in s1
r2 = "come" not in s1
print(r1, r2)

print('One', end='')
print('Two')
print('Three')

s1 = "Welcome to "
s2 = "Hcc"

print(2 * s2)
print(s1 + s2)

x = math.ceil(11.2)
print (x)

x = 1
y = 2
print('x'+'y')

# print("COSC" + str(1436))


# print("COSC" + int(1436))



print("COSC","1436")

print("COSC"+"1436")

print("COSC1436")

s1 = "smith" 
s2 = "Mary"
if s2 < s1:
    temp = s1
    s1 = s2
    s2 = temp
print(s1, s2.capitalize())

interestRate = 0.77
billAmount = 10
result = billAmount * interestRate
print(round(result))
print(format(result, ".2f"))
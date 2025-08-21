# Find the Factorial of number optimiz it as much as you can 
# Function Based 

# #Using Inbuild Math Library using Factorial find
# def factorial(Number):
#     import math
#     return math.factorial(Number)

# Using Loop Find Factorial 
def factorial(Number):
    fact = 1
    for i in range(1,Number+1):
        fact*= i
    return fact

while True:
    Number = input("Enter Your Circular Queue capacity :")
    if not Number.isdigit():
        print('Please Enter Digit Only')
        continue
    else:
        Number = int(Number)
        print(f"{Number} Factorial Number is {factorial(Number)}")
        break
    
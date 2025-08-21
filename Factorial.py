# Find the Factorial of number optimiz it as much as you can 
# Function Based 
def factorial(Number):
    fact = 1
    for i in range(1,Number+1):
        fact*= i
    return fact

while True:
    Number = input("Enter Your Number to find Factorial :")
    if not Number.isdigit():
        print('Please Enter Digit Only')
        continue
    else:
        Number = int(Number)
        print(f"{Number} Factorial Number is {factorial(Number)}")
        break
    
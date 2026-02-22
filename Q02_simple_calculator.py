# Q2 Create a program that: 
#1. Asks user for two numbers 
#2. Performs and displays: Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation

a = int(input("Enter first number: "))  #taken first number input
b = int(input("Enter second number: ")) #second number taken as a input

#perform Arithmetic operations
Addition = a+b
Subtraction = a-b
Multiplication = a*b
Division = a/b
Modulus = a%b
Exponentiation = a**b

#print all the results of performed operations 
print("\nResults:")
print(f"{a} + {b} = {Addition}")
print(f"{a} - {b} = {Subtraction}")
print(f"{a} * {b} = {Multiplication}")
print(f"{a} / {b} = {Division}")
print(f"{a} % {b} = {Modulus}")
print(f"{a} ^ {b} = {Exponentiation}")

# output tested with multiple inputs

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q02_simple_calculator.py
# Enter first number: 6
# Enter second number: 9

# Results:
# 6 + 9 = 15
# 6 - 9 = -3
# 6 * 9 = 54
# 6 / 9 = 0.6666666666666666
# 6 % 9 = 6
# 6 ^ 9 = 10077696

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q02_simple_calculator.py
# Enter first number: 13
# Enter second number: 18

# Results:
# 13 + 18 = 31
# 13 - 18 = -5
# 13 * 18 = 234
# 13 / 18 = 0.7222222222222222
# 13 % 18 = 13
# 13 ^ 18 = 112455406951957393129

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q02_simple_calculator.py
# Enter first number: 15
# Enter second number: 5

# Results:
# 15 + 5 = 20
# 15 - 5 = 10
# 15 * 5 = 75
# 15 / 5 = 3.0
# 15 % 5 = 0
# 15 ^ 5 = 759375

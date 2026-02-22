#Q20) Create the following mathematical functions: 
# 1. factorial(n) - return n!   2. is_prime(n) - return True if prime 3. fibonacci(n) - return nth Fibonacci number 
# 4. sum_of_digits(n) - return sum of digits  5. reverse_number(n) - return number reversed 
# 6. is_armstrong(n) - check if Armstrong number (e.g., 153 = 1³ + 5³ + 3³)  7. gcd(a, b) - greatest common divisor 
# 8. lcm(a, b) - least common multiple  9. is_perfect_number(n) - sum of divisors equals n (e.g., 6 = 1+2+3) 
# 10. math_menu() - menu to test all functions 
# Each function should be callable individually from the menu with appropriate user input. 

#Define Functions for each mathematical tasks
def factorial(n):# Function to compute factorial of a number 
    if n < 0:  # checking conditions for Factorial not defined for negative
        return "Invalid"
    fact = 1 # Start result at 1
    for i in range(1, n+1): # Multiply from 1 to n, Return factorial
        fact *= i
    return fact                      
def is_prime(n):#Function to check prime
    if n <= 1: # 0 and 1 are not prime, returns false
        return False
    for i in range(2, int(n**0.5)+1):  # Check divisibility up to √n
        if n % i == 0: #if this condition met then it returns false 
            return False
    return True
def fibonacci(n):# Function to get nth Fibonacci
    if n <= 0:  #Handle different conditions regarding to n values 
        return "Invalid"
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1 # First two Fibonacci numbers
    for _ in range(3, n+1):
        a, b = b, a+b # Shift sequence for particular values
    return b
def sum_of_digits(n):   # Function to sum digits
    return sum(int(d) for d in str(abs(n)))  # Convert to string, sum digits
def reverse_number(n): # Function to reverse digits
    sign = -1 if n < 0 else 1 # Keep sign negative for reversing
    rev = int(str(abs(n))[::-1]) # Reverse digits ,here abs refers to absolute values 
    return sign * rev
def is_armstrong(n): # Function to check Armstrong
    digits = str(abs(n)) # Get digits
    power = len(digits)  # Number of digits
    total = sum(int(d)**power for d in digits)  # Sum of powers for digits
    return total == abs(n)
def gcd(a, b):# Function for greatest common divisor
    while b != 0:# Euclidean algorithm
        a, b = b, a % b
    return abs(a)
def lcm(a, b):# Function for least common multiple
    if a == 0 or b == 0:
        return 0
    return abs(a*b) // gcd(a, b)# Formula using gcd


def is_perfect_number(n):# Function to check perfect number
    if n <= 0:
        return False
    total = 0
    for i in range(1, n):# Check divisors
        if n % i == 0:
            total += i
    return total == n


def math_menu(): # Main menu functions
    while True:
        print("\n=== MATH MENU ===\n1. Factorial\n2. Prime Check\n3. Fibonacci\n4. Sum of Digits\n5. Reverse Number\n6. Armstrong Check\n7. GCD\n8. LCM\n9. Perfect Number\n10. Exit")
        ch = input("Choose: ")       # take input of User choice

#use if else conditional statements for calling different functions and perform as per user entered choice 
        if ch == "10":
            print("Exiting...")
            break

        if ch == "1":
            n = int(input("Enter n: "))
            print("Factorial:", factorial(n))

        elif ch == "2":
            n = int(input("Enter n: "))
            print("Prime:", is_prime(n))

        elif ch == "3":
            n = int(input("Enter n: "))
            print("Fibonacci:", fibonacci(n))

        elif ch == "4":
            n = int(input("Enter n: "))
            print("Sum of digits:", sum_of_digits(n))

        elif ch == "5":
            n = int(input("Enter n: "))
            print("Reversed:", reverse_number(n))

        elif ch == "6":
            n = int(input("Enter n: "))
            print("Armstrong:", is_armstrong(n))

        elif ch == "7":
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("GCD:", gcd(a, b))

        elif ch == "8":
            a = int(input("Enter a: "))
            b = int(input("Enter b: "))
            print("LCM:", lcm(a, b))

        elif ch == "9":
            n = int(input("Enter n: "))
            print("Perfect:", is_perfect_number(n))

        else:
            print("Invalid choice")

#call the main function math_menu
math_menu()


#tested with multiple inputs
# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q20_Number_System_Functions.py

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 1
# Enter n: 4
# Factorial: 24

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 2
# Enter n: 9
# Prime: False

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 3
# Enter n: 1223
# Fibonacci: 107996923339887323603284429330165352497636293618077164748881014625842857
#           38925020873487784683205571783810115198621325011674475285351477027057245870
#            184357713578062133821547209578364313783025354566070395720268160186654285719
#            46697730583021094317239872427815311

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 4
# Enter n: 73
# Sum of digits: 10

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 5
# Enter n: 6543
# Reversed: 3456

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 6
# Enter n: 34
# Armstrong: False

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 7
# Enter a: 45
# Enter b: 3
# GCD: 3

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 8
# Enter a: 2
# Enter b: 87
# LCM: 174

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 9
# Enter n: 43
# Perfect: False

# === MATH MENU ===
# 1. Factorial
# 2. Prime Check
# 3. Fibonacci
# 4. Sum of Digits
# 5. Reverse Number
# 6. Armstrong Check
# 7. GCD
# 8. LCM
# 9. Perfect Number
# 10. Exit
# Choose: 10
# Exiting...

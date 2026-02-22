#Q18) Create a calculator using functions. 
#Required Functions: 1. add(a, b)   2. subtract(a, b) 3. multiply(a, b)   4. divide(a, b) - handle division by zero   5. modulus(a, b)   6. power(a, b)   7. calculator() - main function with menu 

#Define Functions for different operations
def add(a, b):# Function to add two numbers ,return sum
    return a + b         
def subtract(a, b):# Function to subtract b from a,return difference
    return a - b         
def multiply(a, b): # Function to multiply two numbers,return product
    return a * b          
def divide(a, b): # Function to divide a by b,Check division by zero,return quotient
    if b == 0:            
        return "Error: Division by zero not allowed"
    return a / b          
def modulus(a, b): # Function to get remainder,modulus by zero invalid,return remainder
    if b == 0:             
        return "Error: Division by zero not allowed"
    return a % b     
def power(a, b):# Function to raise a to power b,return exponent result
    return a ** b        

def calculator():# Main calculator function
    while True:#Whil loop until user exits
        print("\n=== CALCULATOR ===")
        print("1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit")
        choice = input("Choose option: ")  #input User menu choice

        if choice == "7": # Exit option
            print("Exiting calculator...")
            break
        # Take numbers for operations
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        # Call appropriate function to perform
        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = subtract(a, b)
        elif choice == "3":
            result = multiply(a, b)
        elif choice == "4":
            result = divide(a, b)
        elif choice == "5":
            result = modulus(a, b)
        elif choice == "6":
            result = power(a, b)
        else:
            print("Invalid choice")
            continue
        print("Result:", result)  #print result
# Run calculator bu calling main function calculator()
calculator()


#Tested with multiple outputs
# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q18_Calculator_Functions.py

# === CALCULATOR ===
# 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit
# Choose option: 1
# Enter first number: 2
# Enter second number: 97
# Result: 99.0

# === CALCULATOR ===
# 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit
# Choose option: 2
# Enter first number: 5
# Enter second number: 6
# Result: -1.0

# === CALCULATOR ===
# 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit
# Choose option: 3
# Enter first number: 43
# Enter second number: 34
# Result: 1462.0

# === CALCULATOR ===
# 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit
# Choose option: 4
# Enter first number: 1
# Enter second number: 0.7
# Result: 1.4285714285714286

# === CALCULATOR ===
# 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit
# Choose option: 5
# Enter first number: 9
# Enter second number: 2
# Result: 1.0

# === CALCULATOR ===
# 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit
# Choose option: 6
# Enter first number: 5
# Enter second number: 3
# Result: 125.0

# === CALCULATOR ===
# 1-Add, 2-Subtract, 3-Multiply, 4-Divide, 5-Modulus , 6-Power , 7- Exit
# Choose option: 7
# Exiting calculator...

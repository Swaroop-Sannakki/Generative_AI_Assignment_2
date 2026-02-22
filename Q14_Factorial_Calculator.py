#Q14 Calculate factorial of a number using a loop. Factorial: n! = n × (n-1) × (n-2) × ... × 1 
#Requirements: - Handle 0 and negative numbers - Display step-by-step calculation

n = int(input("Enter a number: "))  # take input from the  user to enter a number

if n < 0:  # Check or handle for negative number and print 
    print("Factorial not defined for negative numbers")
    
elif n == 0:  #handle Special case for  0! = 1
    print("0! = 1")
    
else:
    fact = 1          # Store factorial result in fact variable
    steps = ""        # Store step-by-step string

    for i in range(n, 0, -1):  # for Loop from n down to 1
        fact *= i              # Multiply factorial
        steps += str(i)        # Adds number to steps
        
        if i != 1:             # Add multiplication sign except after last 
            steps += " × "

    print(f"{n}! = {steps} = {fact}")  # print result in 5! = 5 × 4 × 3 × 2 × 1 = 120 format
    
    
#multiple tested outputs
# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q14_Factorial_Calculator.py
# Enter a number: 3
# 3! = 3 × 2 × 1 = 6

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q14_Factorial_Calculator.py
# Enter a number: 8
# 8! = 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 40320

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q14_Factorial_Calculator.py
# Enter a number: 11
# 11! = 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 39916800

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q14_Factorial_Calculator.py
# Enter a number: 21
# 21! = 21 × 20 × 19 × 18 × 17 × 16 × 15 × 14 × 13 × 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 51090942171709440000

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q14_Factorial_Calculator.py
# Enter a number: 101
# 101! = 101 × 100 × 99 × 98 × 97 × 96 × 95 × 94 × 93 × 92 × 91 × 90 × 89 × 88 × 87 × 86 × 85 × 84 × 83 × 82 × 81 × 80 × 79 × 78 × 77 × 76 × 75 × 74 × 73 × 72 × 71 × 70 × 69 × 68 × 67 × 66 × 65 × 64 × 63 × 62 × 61 × 60 × 59 × 58 × 57 × 56 × 55 × 54 × 53 × 52 × 51 × 50 × 49 × 48 × 47 × 46 × 45 × 44 × 43 × 42 × 41 × 40 × 39 × 38 × 37 × 36 × 35 × 34 × 33 × 32 × 31 × 30 × 29 × 28 × 27 × 26 × 25 × 24 × 23 × 22 × 21 × 20 × 19 × 18 × 17 × 16 × 15 × 14 × 13 × 12 × 11 × 10 × 9 × 8 × 7 × 6 × 5 × 4 × 3 × 2 × 1 = 9425947759838359420851623124482936749562312794702543768327889353416977599316221476503087861591808346911623490003549599583369706302603264000000000000000000000000

    
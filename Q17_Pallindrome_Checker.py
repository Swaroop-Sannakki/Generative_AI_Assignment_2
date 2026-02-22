#Q17) Create a program that checks if a word/number is a palindrome (reads same forwards and backwards). 
#Requirements: Check words (ignore case), check numbers, display step-by-step verification.

text = input("Enter word/number: ") #Take input from user (word or number)

original = text    # Store original input exactly as entered
lower_text = text.lower() # Convert to lowercase for comparison (ignore case)
reversed_text = lower_text[::-1] # Reverse the lowercase text using slicing i.e [::-1]

print("Original:", original) # Show original input
print("Reversed:", reversed_text) # Show reversed version (case-insensitive)

# Step-by-step comparison for sequence 
print("\nStep-by-step check:")
for i in range(len(lower_text)): # for Loop through each character position
    left = lower_text[i]   # Character from start
    right = lower_text[-(i+1)] # check for Matching character from end
    print(f"{left} == {right}")# print comparison for step by step checking

# Final palindrome check or matching check
if lower_text == reversed_text: # If same forwards and backwards then print results 
    print("Result: PALINDROME")
else:
    print("Result: NOT PALINDROME")
    
#Multiple tested outputs

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q1_Pallindrome_Checker.py
# Enter word/number: swaroop
# Original: swaroop
# Reversed: pooraws

# Step-by-step check:
# s == p
# w == o
# a == o
# r == r
# o == a
# o == w
# p == s
# Result: NOT PALINDROME

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q1_Pallindrome_Checker.py
# Enter word/number: 1232332321
# Original: 1232332321
# Reversed: 1232332321

# Step-by-step check:
# 1 == 1
# 2 == 2
# 3 == 3
# 2 == 2
# 3 == 3
# 3 == 3
# 2 == 2
# 3 == 3
# 2 == 2
# 1 == 1
# Result: PALINDROME

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q1_Pallindrome_Checker.py
# Enter word/number: madam
# Original: madam
# Reversed: madam

# Step-by-step check:
# m == m
# a == a
# d == d
# a == a
# m == m
# Result: PALINDROME

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q1_Pallindrome_Checker.py
# Enter word/number: 1432567324
# Original: 1432567324
# Reversed: 4237652341

# Step-by-step check:
# 1 == 4
# 4 == 2
# 3 == 3
# 2 == 7
# 5 == 6
# 6 == 5
# 7 == 2
# 3 == 3
# 2 == 4
# 4 == 1
# Result: NOT PALINDROME
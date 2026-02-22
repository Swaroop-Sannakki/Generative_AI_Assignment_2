# Ask the user how many numbers they want to add. Then take that many numbers as input using a loop. 
# Calculate: 1. Sum  2. Average  3. Maximum number  4. Minimum number


n = int(input("How many numbers ?  "))  # take input of  how many numbers the user wants to enter 
nums = []                     # Create an empty list to store the numbers enterd by user 

for i in range(n):            # lpply for Loop n times i.e user input 
    nums.append(float(input("Enter: ")))  # Takes a number add to list

#print information 
print("Sum:", sum(nums))          # Prints total of all numbers in the list
print("Average:", sum(nums)/n)    # calculates average (sum divided by count)
print("Maximum:", max(nums))          # Prints largest number in the list
print("Minimum:", min(nums))          # Prints smallest number in the list

#Tested outputs

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q13_Sum_and_Average.py
# How many numbers ?  3
# Enter: 10
# Enter: 20
# Enter: 30
# Sum: 60.0
# Average: 20.0
# Maximum: 30.0
# Minimum: 10.0

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q13_Sum_and_Average.py
# How many numbers ?  5
# Enter: 87
# Enter: 78
# Enter: 65
# Enter: 43
# Enter: 547
# Sum: 820.0
# Average: 164.0
# Maximum: 547.0
# Minimum: 43.0

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q13_Sum_and_Average.py 
# How many numbers ?  7
# Enter: 7
# Enter: 8
# Enter: 9
# Enter: 0
# Enter: 4
# Enter: 5
# Enter: 3
# Sum: 36.0
# Average: 5.142857142857143
# Maximum: 9.0
# Minimum: 0.0
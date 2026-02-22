#Ask users for marks in 5 subjects (out of 100 each). Calculate and display: 
#1. Marks in each subject   2. Total marks (out of 500)   3. Percentage   4. Grade   5. Result: Pass/Fail (Pass if all subjects >= 40)

marks = []  # Create an empty list to store marks of 5 subjects

for i in range(1,6):  # iterate Loop from 1 to 5 (for 5 subjects)
    m = float(input(f"Enter marks for subject {i}: "))  # take input  marks for each subject and convert to decimal number
    marks.append(m)  # append() adds or pushes entered marks into the marks list

total = sum(marks)  # Add all marks in the list to get total marks
percent = total/500*100  # Calculate percentage assuming each subject is out of 100 (total 500)

#use if else condition statement to check pass or fail
if all(m>=40 for m in marks):  # all() Checks if every subject mark is at least 40
    result = "Pass"  # If all subjects >=40, student passes
else:
    result = "Fail"  # If any subject <40, student fails

#use nested else if conditional statements to assign grades based on their percentage
if percent>=90:      # If percentage is 90 or above ,Assign grade A+
    grade="A+"       
elif percent>=80: # else If percentage is 80–89,assign grade A
    grade="A"        
elif percent>=70:#esle If percentage is 70–79, assign grade B
    grade="B"     
elif percent>=60:#else If percentage is 60–69 ,assign grade C
    grade="C"        
elif percent>=50:#else If percentage is 50–59,assign grade D
    grade="D"        
else:        #if  percentage below 50, assign fail grade F
    grade="F"        

#print or display all calculated information
print("Total:", total)         
print("Percentage:", percent)   
print("Grade:", grade)          
print("Result:", result)       


#output tested with multiple inputs 
# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q06_Grade_Calculator.py
# Enter marks for subject 1: 91
# Enter marks for subject 2: 100
# Enter marks for subject 3: 93
# Enter marks for subject 4: 96
# Enter marks for subject 5: 98
# Total: 478.0
# Percentage: 95.6
# Grade: A+
# Result: Pass

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q06_Grade_Calculator.py
# Enter marks for subject 1: 35
# Enter marks for subject 2: 65
# Enter marks for subject 3: 43
# Enter marks for subject 4: 76
# Enter marks for subject 5: 45
# Total: 264.0
# Percentage: 52.800000000000004
# Grade: D
# Result: Fail
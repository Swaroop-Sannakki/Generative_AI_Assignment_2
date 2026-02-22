#Q) Create a program that asks the user for a number and a range, then displays the multiplication table. 

num = int(input("Enter the Number: "))  # take the input from user which number table to print and convert to integer
end = int(input("Range: "))   # take input for range or how many multiples to show  

for i in range(1, end+1):     # apply for Loop from 1 up to the entered range
    print(f"{num} x {i} = {num*i}")  # Print multiplication line (num × i = result)
    
#Multiplication Table in grid Format

# Print header row from 1 to 10
print("   ", end="")                # it gives empty corner space
for i in range(1, 11):              # for loop from 1 to 10
    print(f"{i:4}", end="")         # Print column headers with spacing
print()

# Print separator line
print("-" * 44)                     # take horizontal line

# Print table rows
for i in range(1, 11):              # for loop for Each row from 1 to 10
    print(f"{i:2}|", end="")        # Row header number at left

    for j in range(1, 11):          # nested for loop for the columns from 1 to 10 to form grid structure
        print(f"{i*j:4}", end="")   # Prints multiplicates with spacing between them

    print()                         # it helps to go Next row
    
    
#Tested outputs

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q12_Multiplication_Table_Generator.py
# Enter the Number: 7
# Range: 11
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70
# 7 x 11 = 77
#       1   2   3   4   5   6   7   8   9  10
# --------------------------------------------
#  1|   1   2   3   4   5   6   7   8   9  10
#  2|   2   4   6   8  10  12  14  16  18  20
#  3|   3   6   9  12  15  18  21  24  27  30
#  4|   4   8  12  16  20  24  28  32  36  40
#  5|   5  10  15  20  25  30  35  40  45  50
#  6|   6  12  18  24  30  36  42  48  54  60
#  7|   7  14  21  28  35  42  49  56  63  70
#  8|   8  16  24  32  40  48  56  64  72  80
#  9|   9  18  27  36  45  54  63  72  81  90
# 10|  10  20  30  40  50  60  70  80  90 100

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q12_Multiplication_Table_Generator.py
# Enter the Number: 6
# Range: 19
# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
# 6 x 5 = 30
# 6 x 6 = 36
# 6 x 7 = 42
# 6 x 8 = 48
# 6 x 9 = 54
# 6 x 10 = 60
# 6 x 11 = 66
# 6 x 12 = 72
# 6 x 13 = 78
# 6 x 14 = 84
# 6 x 15 = 90
# 6 x 16 = 96
# 6 x 17 = 102
# 6 x 18 = 108
# 6 x 19 = 114
#       1   2   3   4   5   6   7   8   9  10
# --------------------------------------------
#  1|   1   2   3   4   5   6   7   8   9  10
#  2|   2   4   6   8  10  12  14  16  18  20
#  3|   3   6   9  12  15  18  21  24  27  30
#  4|   4   8  12  16  20  24  28  32  36  40
#  5|   5  10  15  20  25  30  35  40  45  50
#  6|   6  12  18  24  30  36  42  48  54  60
#  7|   7  14  21  28  35  42  49  56  63  70
#  8|   8  16  24  32  40  48  56  64  72  80
#  9|   9  18  27  36  45  54  63  72  81  90
# 10|  10  20  30  40  50  60  70  80  90 100

    
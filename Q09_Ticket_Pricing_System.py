#Create a movie ticket pricing system. 
#Age-based Pricing:  Below 3: Free  3-12: ₹150 (Child)  13-59: ₹300 (Adult)  60+: ₹200 (Senior) 
#Day-based Discount:  Monday-Thursday: No discount  Friday-Sunday: 20% discount
# Inputs: Age, Day of week, Number of tickets Display base price, discount (if any), price after discount, and total amount.


#take input from the user age,day,tickets
age = int(input("Age: "))            
day = input("Day: ").lower()         
tickets = int(input("Tickets: "))   

# checks  ticket price per person based on age
if age < 3: # If age less than 3 years,Ticket is free
    price = 0       
elif age <= 12:#else If age between 3 and 12,Child ticket price
    price = 150    
elif age <= 59: # else If age between 13 and 59,Adult ticket price
    price = 300      
else:      # If age 60 or above,Senior citizen price
    price = 200      

total = price * tickets # Calculate total base price for all tickets

# Weekend discount checking
if day in ["friday", "saturday", "sunday"]:  #checks the days in the list for 20% discount
    discount = total * 0.2   
else:
    discount = 0  # this shows No discount on weekdays

final = total - discount  # Final amount after subtracting discount

print("Base:", total)        # Prints total before discount
print("Discount:", discount) # Prints discount amount
print("Final:", final)       # Prints final payable amount


#output tested with multiple inputs

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q09_Ticket_Pricing_System.py
# Age: 2
# Day: monday
# Tickets: 4
# Base: 0
# Discount: 0
# Final: 0

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q09_Ticket_Pricing_System.py
# Age: 2 
# Day: sunday
# Tickets: 4
# Base: 0
# Discount: 0.0
# Final: 0.0

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q09_Ticket_Pricing_System.py
# Age: 21
# Day: tuesday
# Tickets: 7
# Base: 2100
# Discount: 0
# Final: 2100

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q09_Ticket_Pricing_System.py
# Age: 11
# Day: wednesday
# Tickets: 3
# Base: 450
# Discount: 0
# Final: 450

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q09_Ticket_Pricing_System.py
# Age: 10
# Day: saturday
# Tickets: 5
# Base: 750
# Discount: 150.0
# Final: 600.0


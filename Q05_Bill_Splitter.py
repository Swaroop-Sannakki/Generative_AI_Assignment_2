#Q5)Create a restaurant bill splitting program. 
#Inputs: Total bill amount, Number of people, Tax percentage, Tip percentage 
#Calculate and Display: Subtotal, Tax amount, Bill after tax, Tip amount, Total bill, Amount per person 

 
try:  # Start error handling block
#take all the inputs and store in the variables in integer or float where ever required 
    total = float(input("Enter total bill: "))      
    people = int(input("Number of people: "))      
    tax = float(input("Tax percentage: "))          
    tip = float(input("Tip percentage: "))          

    # Validate inputs
    if total < 0 or people <= 0 or tax < 0 or tip < 0:  # Check for invalid values
        print("Invalid input values")
    else:
        tax_amount = total * tax / 100 # Calculates tax amount
        after_tax = total + tax_amount # Adds tax to subtotal
        tip_amount = after_tax * tip / 100# Calculates tip on taxed amount
        final = after_tax + tip_amount # Final bill inclues sum of 
        per_person = final / people  #calculates for per person 
        #print bill breakdown that has all the information     
        print("\n=== BILL BREAKDOWN ===")   
        print(f"Subtotal:    ₹{total:.2f}")  
        print(f"Tax ({tax}%):   ₹{tax_amount:.2f}")  
        print(f"After tax:   ₹{after_tax:.2f}")   
        print(f"Tip ({tip}%):   ₹{tip_amount:.2f}")  
        print(f"Total:       ₹{final:.2f}")       
        print(f"Per person:  ₹{per_person:.2f}")  

except:  # If conversion error occurs the prints invalid input
    print("Invalid input type")
    
#Multiple outputs

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q5_Bill_Splitter.py
# Enter total bill: 5673
# Number of people: 5
# Tax percentage: 10
# Tip percentage: 15

# === BILL BREAKDOWN ===
# Subtotal:    ₹5673.00
# Tax (10.0%):   ₹567.30
# After tax:   ₹6240.30
# Tip (15.0%):   ₹936.04
# Total:       ₹7176.35
# Per person:  ₹1435.27

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q5_Bill_Splitter.py
# Enter total bill: 56rte
# Invalid input type

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q5_Bill_Splitter.py
# Enter total bill: 150
# Number of people: 3
# Tax percentage: 5 
# Tip percentage: 7.5

# === BILL BREAKDOWN ===
# Subtotal:    ₹150.00
# Tax (5.0%):   ₹7.50
# After tax:   ₹157.50
# Tip (7.5%):   ₹11.81
# Total:       ₹169.31
# Per person:  ₹56.44
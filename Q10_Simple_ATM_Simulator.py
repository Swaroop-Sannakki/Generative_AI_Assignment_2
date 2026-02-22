#Create an ATM simulation with initial balance = ₹10,000. 
#Menu: 1. Check Balance  2. Deposit Money  3. Withdraw Money  4. Exit 
#Rules: - Check sufficient balance before withdrawal - Minimum balance of ₹500 must remain at all times - Display transaction messages and updated balance after each transaction


balance = 10000  # Set initial bank account balance to 10000

while True:  # Start infinite loop so ATM menu keeps showing till the user exit 
    print("\n1.Check 2.Deposit 3.Withdraw 4.Exit")  # Display ATM options for the user 
    ch = input("Choice: ")  # takes input from the user  to choose an option

    if ch == "1":  # If user selects Check Balance
        print("Balance:", balance)  # shows current balance
    elif ch == "2":  # If user selects Deposit option
        amount = float(input("Deposit: "))  # Ask deposit amount
        balance += amount
        print("Deposition successfull..")
        print("New Balance:",balance)# Add deposit amount to balance     
    elif ch == "3":  # If user selects Withdraw
        amount = float(input("Enter amount to Withdraw: "))  # Ask withdrawal amount
        # Check if minimum balance of 500 will remain after withdrawal
        if balance - amount >= 500:
            balance -= amount
            print("withdrwa successfull...!!")
            print("New Balance:",balance)# subtract amount from balance
        else:
            print("Minimum balance required")  # Warn if balance would go below 500
    elif ch == "4":  # If user selects Exit
        break  # Stop loop and end ATM program
    
#output tested with multiple inputs 

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q10_Simple_ATM_Simulator.py

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 1
# Balance: 10000

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 2
# Deposit: 500
# Deposition successfull..
# New Balance: 10500.0

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 3
# Enter amount to Withdraw: 300
# withdrwa successfull...!!
# New Balance: 10200.0

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 4

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q10_Simple_ATM_Simulator.py

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 2
# Deposit: 250
# Deposition successfull..
# New Balance: 10250.0

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 3
# Enter amount to Withdraw: 10200
# Minimum balance required

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 3
# Enter amount to Withdraw: 9750
# withdrwa successfull...!!
# New Balance: 500.0

# 1.Check 2.Deposit 3.Withdraw 4.Exit
# Choice: 4

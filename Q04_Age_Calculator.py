#Q4)Ask user for their birth year and calculate: 
# 1. Current age  
# 2. Age in months   
# 3. Age in days (approx 365 days/year)   
# 4. Age in hours   
# 5. Age in minutes   
# 6. Years until age 100
# ask for an exact birth date (day, month, year) and calculate more precisely. 


from datetime import date   # Imports the date class from datetime module to work with dates
try:  # start try block to catch invalid inputs
    # user inputs are taken i.e day , month, year in integer format
    day = int(input("Enter birth day (1-31): "))     
    month = int(input("Enter birth month (1-12): ")) 
    year = int(input("Enter birth year: "))          
    birth_date = date(year, month, day)  # Create a date object using entered year, month, and day
    today = date.today()  # Get today's current date from system
    age_years = today.year - birth_date.year  # Calculate rough age by subtracting birth year from current year

    # Check if birthday has not happened yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):  
        age_years -= 1  # If birthday not reached yet, reduce age by 1

    days_lived = (today - birth_date).days  # Calculate total number of days lived by subtracting dates
    months_lived = days_lived // 30 # calculates approximate months lived by dividing days by 30
    hours_lived = days_lived * 24 # Convert days lived into hours
    minutes_lived = hours_lived * 60 # Convert hours lived into minutes
    #print all the informations
    print("\n AGE DETAILS")          
    print("Years:", age_years)         
    print("Months:", months_lived)     
    print("Days:", days_lived)         
    print("Hours:", hours_lived)       
    print("Minutes:", minutes_lived)   
    print("Years until 100:", 100 - age_years) 

except:  # handles invalid date or non-numeric input
    print("Invalid date or input entered") 


#Multiple outputs
# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q4_Age_Calculator.py
# Enter birth day (1-31): 5
# Enter birth month (1-12): 0
# Enter birth year: 4222
# Invalid date or input entered

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q4_Age_Calculator.py
# Enter birth day (1-31): 05
# Enter birth month (1-12): 03
# Enter birth year: 2004

#  AGE DETAILS
# Years: 21
# Months: 267
# Days: 8024
# Hours: 192576
# Minutes: 11554560
# Years until 100: 79

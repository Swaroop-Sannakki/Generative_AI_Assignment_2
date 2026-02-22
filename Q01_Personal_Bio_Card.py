#Q1.Write a program that displays your information in a formatted card

name = "Swaroop Sannakki" #declared sring variable called 'Name'
age = 21 #used integer variable for age 
course = "Generative AI"  #used string variables 'course','college','email'for storing details
college = "M S R I T Bangalore"
email = "swaroop@gmail.com"


 #print all the above information as given formatted card
print("||===============================||")
print("||       STUDENT BIO CARD        ||")
print("||===============================||")
print(f"|| Name    : {name:<20}||")  #f" " → f-string (lets us to insert variables inside text),{name} → inserts value of variable name,'<20' → left-align text in 20 spaces
print(f"|| Age     : {age} years{'':<12}||") #{'':<12} → it means empty space padded to 12 characters
print(f"|| Course  : {course:<20}||")
print(f"|| College : {college:<20}||")
print(f"|| Email   : {email:<20}||")
print("||===============================||")


#output:
#||===============================||
#||       STUDENT BIO CARD        ||
#||===============================||
#|| Name    : Swaroop Sannakki    ||
#|| Age     : 21 years            ||
#|| Course  : Generative AI       ||
#|| College : M S R I T Bangalore ||
#|| Email   : swaroop@gmail.com   ||
#||===============================||

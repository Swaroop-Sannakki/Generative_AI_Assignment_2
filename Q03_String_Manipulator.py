# Q3 String Manipulator

sentence = input("Enter a sentence: ") #input sentence is taken and stored in variable called "sentence"

words = sentence.split()  #split() function used to split the words from the sentences .. stored in "word" variable

print("Original:", sentence)  #prints original sentence
print("Characters (with spaces):", len(sentence)) # It gives length of sentence i.e len() counts the characters in a sentence
print("Characters (without spaces):", len(sentence.replace(" ", ""))) #here replace(" "," ") removes the spaces the len() counts the characters 
print("Words:", len(words)) #words variable has list of words so len() counts total number of words in that list
print("UPPERCASE:", sentence.upper()) #upper() converts all letter to upper case(capital) letters
print("lowercase:", sentence.lower()) #lower() converts all letters to lower case(small) letters
print("Title Case:", sentence.title()) #title() capitaizes the first letter of every word 
print("First word:", words[0]) #since list index starts from 0 , it prints first word in the list
print("Last word:", words[-1]) #[-1] indicates last word or item in the list , so it prints last word of the word list
print("Reversed:", sentence[::-1]) #[start:end:step], so [::-1] -1 indicates move backward ..hence it reverses the sentence

#output tested with multiple inputs

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q03_String_Manipulator.py
# Enter a sentence: Hii bro ,how are you?
# Original: Hii bro ,how are you?
# Characters (with spaces): 21
# Characters (without spaces): 17
# Words: 5
# UPPERCASE: HII BRO ,HOW ARE YOU?
# lowercase: hii bro ,how are you?
# Title Case: Hii Bro ,How Are You?
# First word: Hii
# Last word: you?
# Reversed: ?uoy era woh, orb iiH

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q03_String_Manipulator.py
# Enter a sentence: It's very hot today.. I need some Ice creams
# Original: It's very hot today.. I need some Ice creams
# Characters (with spaces): 44
# Characters (without spaces): 36
# Words: 9
# UPPERCASE: IT'S VERY HOT TODAY.. I NEED SOME ICE CREAMS
# lowercase: it's very hot today.. i need some ice creams
# Title Case: It'S Very Hot Today.. I Need Some Ice Creams
# First word: It's
# Last word: creams
# Reversed: smaerc ecI emos deen I ..yadot toh yrev s'tI
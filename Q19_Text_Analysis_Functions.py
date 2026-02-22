# Q19) Create the following text analysis functions: 
# 1. count_words(text) - return number of words 
# 2. count_vowels(text) - return number of vowels 
# 3. count_consonants(text) - return number of consonants 
# 4. reverse_text(text) - return reversed text 
# 5. is_palindrome(text) - return True/False 
# 6. remove_vowels(text) - return text without vowels 
# 7. word_frequency(text) - return dictionary of word counts 
# 8. longest_word(text) - return longest word 
# 9. analyze_text(text) - calls all above functions and displays results 


# Define functions for different text analysis
def count_words(text): # function to count number of words
    words = text.split() # Split text into words using spaces,eturn number of words
    return len(words)                  
def count_vowels(text):# Function to count vowels
    vowels = "aeiouAEIOU"# All vowels (lower + upper)
    count = 0          # Start counter at 0 and apply Loop through each character, check if character is a vowel and Increase counter 
    for ch in text:                    
        if ch in vowels:            
            count += 1                
    return count                       
def count_consonants(text):#Function to count consonants
    vowels = "aeiouAEIOU"  # Vowel list
    count = 0              # Counter initialy assigned to 0
    for ch in text:      # for loop through characters
        if ch.isalpha() and ch not in vowels:  #letter but not vowel
            count += 1                 # Increase consonant count , return consonant count
    return count                       
def reverse_text(text):# Function to reverse text,Reverse string using slicing
    return text[::-1]                  
def is_palindrome(text):               # Function to check palindrome, Remove spaces & ignore case,Compare with reversed
    clean = text.replace(" ", "").lower() 
    return clean == clean[::-1]       
def remove_vowels(text):# Function to remove vowels
    vowels = "aeiouAEIOU" # Vowel list
    result = ""   # Empty result string
    for ch in text:  # Loop through characters,If not vowel add to result,return text without vowels
        if ch not in vowels:        
            result += ch               
    return result                      
def word_frequency(text):  # Function to count word frequency
    words = text.lower().split()  # Lowercase & split into words
    freq = {} # Empty dictionary
    for w in words: # for Loop throught  words, if word already counted,Increase count
        if w in freq:                  
            freq[w] += 1               
        else:
            freq[w] = 1 # it indicates First occurrence
    return freq  # Return frequency dictionary
def longest_word(text):# Function to find longest word,Split into words
    words = text.split()               
    longest = ""# Store longest word
    for w in words:  # for loop words,If current word longer  Update longest,  Return longest word
        if len(w) > len(longest):      
            longest = w                
    return longest                     
def analyze_text(text): # Main function to analyze text
    print("=== TEXT ANALYSIS ===")     # print Title or heading for showing functions
    print("Words:", count_words(text)) # Call word count,vowel count, consonent count, reverse
    print("Vowels:", count_vowels(text))          
    print("Consonants:", count_consonants(text))  
    print("Reversed:", reverse_text(text))       

    if is_palindrome(text): # Call palindrome check weather the text is same when it is reversed 
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))  # Remove vowels and print 

    lw = longest_word(text) # Get longest word
    print(f"Longest word: {lw} ({len(lw)} letters)")

    freq = word_frequency(text)# Get frequency dictionary
    # Format frequency output
    freq_list = []  # List for formatted items
    for k, v in freq.items():  # for Loop dictionary and print in format Format word:count
        freq_list.append(f"{k}: {v}") 

    print("Word Frequency:", ", ".join(freq_list))  # Print joined list
#Run program by callindg analyse_text function
text = input("Enter text: ")# Take user input text
analyze_text(text)# call function


#multiple output tested 

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q19_Text_Analysis_Functions.py
# Enter text: Hii bro .. whats upp?
# === TEXT ANALYSIS ===
# Words: 5
# Vowels: 5
# Consonants: 9
# Reversed: ?ppu stahw .. orb iiH
# Palindrome: No
# Without vowels: H br .. whts pp?
# Longest word: whats (5 letters)
# Word Frequency: hii: 1, bro: 1, ..: 1, whats: 1, upp?: 1


# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q19_Text_Analysis_Functions.py
# Enter text:  Evil is a name of a foeman as i live 
# === TEXT ANALYSIS ===
# Words: 10
# Vowels: 15
# Consonants: 12
# Reversed: evil i sa nameof a fo eman a si livE 
# Palindrome: Yes
# Without vowels:  vl s  nm f  fmn s  lv
# Longest word: foeman (6 letters)
# Word Frequency: evil: 1, is: 1, a: 2, name: 1, of: 1, foeman: 1, as: 1, i: 1, live: 1

# C:\Users\swaro\OneDrive\Desktop\Assignment_2>C:/Python313/python.exe c:/Users/swaro/OneDrive/Desktop/Assignment_2/Q19_Text_Analysis_Functions.py
# Enter text: Genrative AI is very intresting course to learn
# === TEXT ANALYSIS ===
# Words: 8
# Vowels: 17
# Consonants: 23
# Reversed: nrael ot esruoc gnitsertni yrev si IA evitarneG
# Palindrome: No
# Without vowels: Gnrtv  s vry ntrstng crs t lrn
# Longest word: intresting (10 letters)
# Word Frequency: genrative: 1, ai: 1, is: 1, very: 1, intresting: 1, course: 1, to: 1, learn: 1

# Problem 2
# Sang Park


number_words = {"zero", "one", "two", "three", "four", "five", "six", "seven", 
    "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", 
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", 
    "twenty", "thirty", "forty", "fifty", "sixty", "seventy", 
    "eighty", "ninety", "hundred", "thousand", "million", "billion"}

def is_number(astring):
    if not astring:
        return False 

    if astring in number_words:
        return True 

    number_digit = False 
    index = 0  
    
    if astring[index] in ('+', '-'):
        index += 1  

    while index < len(astring):
        char = astring[index]  
        
        if char.isdigit():
            number_digit = True   
        else:
            return False  

        index += 1  

    return number_digit  
user_input = input("Enter a string to check if it's a number or a word representation of a number: ")

if is_number(user_input):
    print("The string is a number or a valid word representation of a number.")
else:
    print("The string is not a number.")

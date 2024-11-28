# Problem 5
# Sang Park

# Approach:
# This program cracks a Caesar cipher by trying keys from 1 to 25. 
# It checks if the decrypted message contains any common words from 
# a list read from "common_words.txt".

# Assumptions:
# 1. The common words file contains one word per line.
# 2. The input message is a valid Caesar cipher and contains only letters and spaces.

from problem3 import caesar_decrypt
from problem4 import process_file

encrypted_message = "mpwtpgp jzf nly lyo jzf lcp slwqhlj espcp"

filename, common_words, lines = process_file("common_words.txt")

def crack_caesar_cipher(message, common_words):
    """Try to decrypt a Caesar cipher message using common words for validation."""
    for key in range(1, 26):
        decrypted_message = caesar_decrypt(key, message)
        words = decrypted_message.split()
        found_common_word = False 
        
        for word in words:
            if word in common_words:
                found_common_word = True
                break  
            
        if found_common_word:
            print(f"Key: {key}, Decrypted Message: '{decrypted_message}'")


crack_caesar_cipher(encrypted_message, common_words)
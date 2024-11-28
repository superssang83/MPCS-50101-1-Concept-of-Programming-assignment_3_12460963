# Problem 3
# Sang Park

word = "Experience is the teacher of all things."
shift = 12

def caesar_encrypt(key, message):
    """Encrypt a message"""
    encrypted_message = ""
    for encrypt in message:
        if encrypt.islower():
            encrypted_message += chr(((ord(encrypt) - 97 + key) % 26)+97)
        elif encrypt.isupper():
            encrypted_message += chr(((ord(encrypt) - 65 + key) % 26)+65)
        else:
            encrypted_message += encrypt
    
    return encrypted_message

def caesar_decrypt(key, message):
    """Decrypt a message"""
    decrypted_message = ""
    for decrypt in message:
        if decrypt.islower():
            decrypted_message += chr(((ord(decrypt) - 97 - key) % 26)+97)
        elif decrypt.isupper():
            decrypted_message += chr(((ord(decrypt) - 65 - key) % 26)+65)
        else:
            decrypted_message += decrypt 
    
    return decrypted_message

encrypted = caesar_encrypt(shift, word)
decrypted = caesar_decrypt(shift, encrypted)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

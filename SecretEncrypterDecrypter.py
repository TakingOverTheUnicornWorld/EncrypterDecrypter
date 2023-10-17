# How to encrypt and decrypt my most secret information

# STEP ONE: Caesar Cipher / ROT-n
# since the numerology number of unicorns are 4, I first encode my secret messages with a caesar cipher with a right shift of 4:

import string

alphabets = (string.ascii_lowercase, string.ascii_uppercase, string.digits)

def caesar(text, step, alphabets):

    def shift(alphabet):
        return alphabet[step:] + alphabet[:step]

    shifted_alphabets = tuple(map(shift, alphabets))
    joined_alphabets = ''.join(alphabets)
    joined_shifted_alphabets = ''.join(shifted_alphabets)
    table = str.maketrans(joined_alphabets, joined_shifted_alphabets)
    return text.translate(table)

# Write string to encrypt and chose number of shifts
encrypted_caesar=caesar('Here I enter the message I wish to encrypt', step=4, alphabets=alphabets)


# STEP TWO: Fernet encryption
# I then encrypt my output from the caesar encryption with Fernet:

from cryptography.fernet import Fernet
 
# The following string wil be encrypted
message = encrypted_caesar

#Choose key 
key = b'NgsiRrqIgPCK_HS5eyFKAFBUQKHg0iVF4fYCNkiaPtA='

# Instantiate the Fernet class with the key 
fernet = Fernet(key)

# Encrypt string
encMessage = fernet.encrypt(message.encode())
 
print("Final encrypted string: ", encMessage)

#DONE 

# To decrypt the Fernet encryption
key = b'NgsiRrqIgPCK_HS5eyFKAFBUQKHg0iVF4fYCNkiaPtA='
fernet = Fernet(key)
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)

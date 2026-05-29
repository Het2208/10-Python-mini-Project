import random , string

chars = list(string.punctuation + string.ascii_letters + string.digits + " ")
key = chars.copy()

random.shuffle(key)

# Encyption
plainText = input("Enter message for Encyption : ")
cipherText = ""

for letter in plainText:
    index = chars.index(letter)
    cipherText += key[index]

print(f"Original message: {plainText}")
print(f"Encrypted message: {cipherText}")

# Decryption
cipherText = input("Enter message for Decryption : ")
plainText = ""

for letter in cipherText:
    index = key.index(letter)
    plainText += chars[index]

print(f"Encrypted message: {cipherText}")
print(f"Original message: {plainText}")






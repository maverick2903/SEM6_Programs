text = input("Enter the plaintext: ").upper()

key = input("Enter the key: ").upper()
        
while len(key) != len(text):
    key += key[:len(text)-len(key)]

encrypt = ""
for i in range(len(text)):
    encrypt += chr((ord(text[i]) + ord(key[i]))%26 + 65)

decrypt = ""
for i in range(len(encrypt)):
    decrypt += chr((ord(encrypt[i]) - ord(key[i]))%26 + 65)

print(f"Encrypted value: {encrypt}")
print(f"Decrypted value: {decrypt}")

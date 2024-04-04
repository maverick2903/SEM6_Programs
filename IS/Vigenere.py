text = input("Enter the plaintext: ").upper()

key = input("Enter the key: ").upper()
        
while len(key) != len(text):
    if len(text) > 2*len(text)-1:
        key += key
    else:
        key += key[:len(text)-len(key)]

encrypt = ""
for i in range(len(text)):
    encrypt += chr((ord(text[i]) + ord(key[i]))%26 + 65)

print(encrypt)
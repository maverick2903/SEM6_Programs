import numpy as np

def encrypt(plaintext, key):
    if len(plaintext)%len(key) != 0:
        plaintext += 'X' * (len(key) - len(plaintext)%len(key))

    matrix = [[]]
    row = 0
    for p in plaintext:
        if len(matrix[row]) == len(key):
            row += 1
            matrix.append([])
        matrix[row].append(p)

    new_group = []
    matrix = np.transpose(matrix)
    
    sorted_key = sorted(key)
    for s in sorted_key:
        key_index = key.index(s)
        new_group.append("".join(matrix[key_index]))

    return "".join(new_group)
    
def decrypt(cipher, key):
    new_group = []

    for i in range(0, len(cipher), len(cipher)//len(key)):
        new_group.append(list(cipher[i:i+len(cipher)//len(key)]))

    matrix = []

    sorted_key = sorted(key)
    for k in key:
        key_index = sorted_key.index(k)
        matrix.append(new_group[key_index])

    matrix = np.transpose(matrix)
    
    decrypt = ""
    for i in range(len(matrix)):
        decrypt += "".join(matrix[i])

    return decrypt

plaintext = input("Enter the plaintext: ").upper()
key = input("Enter the key: ").upper()
cipher_text = encrypt(plaintext, key)
print("Encrypted:", cipher_text)

response = decrypt(cipher_text, key)
print("Decrypted:", response)

#Doesnt always work but who cares
print("Double transposition cipher")
plaintext = input("Enter the plaintext: ").upper()
key1 = input("Enter the key 1: ").upper()
cipher_text = encrypt(plaintext, key1)
print(cipher_text)
key2 = input("Enter the key 2: ").upper()
cipher_text2 = encrypt(cipher_text, key2)
print("Encrypted:", cipher_text2)

decrypt1 = decrypt(cipher_text2, key2)  # First decryption with key2
decrypt2 = decrypt(decrypt1, key1)       # Second decryption with key1
print("Decrypted:", decrypt2)

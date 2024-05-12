text = input("Enter the plaintext: ").upper()

key = input("Enter the key: ").upper()

#not needed i suppose
def xor(a,b):
    a = bin(ord(a))[2:]
    b = bin(ord(b))[2:]
    xored = ""
    for i in range(len(a)):
        xored += str(int(a[i]) ^ int(b[i]))
    return int(xored,2)

# for i in range(len(text)):
#     # num = int(bin(ord(text[i]))[:2] ^ bin(ord(key[i]))[:2],2)
#     encrypt += chr(xor(text[i],key[i]) % 26 + ord('A')) 

# print(f"Encrypted value: {encrypt}")

def encrypt(text, key):
    encrypt = ""
    for t, k in zip(text, key):
        encrypt += chr(ord(t) ^ ord(k))
    return encrypt

def decrypt(cipher, key):
    decrypt = ""
    for c, k in zip(cipher, key):
        decrypt += chr(ord(c) ^ ord(k))
    return decrypt

encrypted_text = encrypt(text, key)
print(f"Encrypted value: {encrypted_text}")
decrypted_text = decrypt(encrypted_text, key)
print(f"Decrypted value: {decrypted_text}")
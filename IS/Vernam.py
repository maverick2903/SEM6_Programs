text = input("Enter the plaintext: ").upper()

key = input("Enter the key: ").upper()

encrypt = ""

def xor(a,b):
    a = bin(ord(a))[2:]
    b = bin(ord(b))[2:]
    xored = ""
    for i in range(len(a)):
        xored += str(int(a[i]) ^ int(b[i]))
    return int(xored,2)

for i in range(len(text)):
    # num = int(bin(ord(text[i]))[:2] ^ bin(ord(key[i]))[:2],2)
    encrypt += chr(xor(text[i],key[i]) % 26 + ord('A')) 

print(f"Encrypted value: {encrypt}")
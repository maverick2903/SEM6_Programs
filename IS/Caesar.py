def encrypt(plaintext,shift):
    return "".join([chr((ord(char)-65+shift)%26 + 65) for char in plaintext])

def decrypt(cipher,shift):
    return "".join([chr((ord(char)-65-shift)%26 + 65) for char in cipher])

plaintext = input("Enter the plaintext: ").upper()
shift = int(input("Enter the shift: "))
cipher = encrypt(plaintext,shift)
print("Encrypted:", cipher)
decrypted = decrypt(cipher,shift)
print("Decrypted:", decrypted)
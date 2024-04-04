def encrypt(plain_text, key):
    plain_text = plain_text.replace(" ", "").upper()
    # Remove duplicate characters from the key and sort it alphabetically
    key_sorted = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    key_length = len(key_sorted)
    # Calculate the number of rows needed
    num_rows = (len(plain_text) + key_length - 1) // key_length
    transposed = [''] * key_length

    # Arrange the plaintext into columns based on the sorted key
    for i, char in enumerate(plain_text):
        column = key_sorted.index(key[i % len(key)])
        transposed[column] += char

    cipher_text = ''.join(transposed)
    return cipher_text


plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
cipher_text = encrypt(plaintext, key)
print("Encrypted:", cipher_text)


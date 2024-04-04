import math

# Define MD5 auxiliary functions
def left_rotate(x, c):
    return ((x << c) & 0xffffffff) | (x >> (32 - c))

def F(X, Y, Z):
    return (X & Y) | (~X & Z)

def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)

def H(X, Y, Z):
    return X ^ Y ^ Z

def I(X, Y, Z):
    return Y ^ (X | ~Z)

# Define MD5 constants
T = [int(2**32 * abs(math.sin(i + 1))) & 0xffffffff for i in range(64)]

# Define MD5 functions
def md5(message):
    # Define MD5 parameters
    A = 0x67452301
    B = 0xefcdab89
    C = 0x98badcfe
    D = 0x10325476

    message = bytearray(message, 'utf-8')
    original_length = len(message) * 8
    message.append(0x80)

    while len(message) % 64 != 56:
        message.append(0)

    message += original_length.to_bytes(8, byteorder='little')

    for i in range(0, len(message), 64):
        chunk = message[i:i + 64]
        a, b, c, d = A, B, C, D

        for j in range(64):
            if j < 16:
                f = F(b, c, d)
                g = j
            elif j < 32:
                f = G(b, c, d)
                g = (5 * j + 1) % 16
            elif j < 48:
                f = H(b, c, d)
                g = (3 * j + 5) % 16
            else:
                f = I(b, c, d)
                g = (7 * j) % 16

            f = (f + a + T[j] + int.from_bytes(chunk[g * 4:g * 4 + 4], byteorder='little')) & 0xffffffff
            a = d
            d = c
            c = b
            b = (b + left_rotate(f, [7, 12, 17, 22][j // 16])) & 0xffffffff

        A = (A + a) & 0xffffffff
        B = (B + b) & 0xffffffff
        C = (C + c) & 0xffffffff
        D = (D + d) & 0xffffffff

    return sum(x << (32 * i) for i, x in enumerate([A, B, C, D]))


message = input("Enter the message: ")
hashed_message = md5(message)
print("MD5 Hash:", hex(hashed_message))

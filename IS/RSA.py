import math
import random

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

p = int(input("Enter a prime number p:\n"))
q = int(input("Enter a prime number q:\n"))
pt = int(input("Enter the plaintext:\n"))

n = p * q
fn = (p - 1) * (q - 1)

e = random.randint(2, fn - 1)
while math.gcd(e, fn) != 1:
    e = random.randint(2, fn - 1)

d = pow(e, -1, fn)

print(f"Public key (e, n) is ({e}, {n})")
print(f"Private key (d, n) is ({d}, {n})")

ct = pow(pt, e, n)
print("Encrypted ciphertext:", ct)

decrypted_pt = pow(ct, d, n)
print("Decrypted plaintext:", decrypted_pt)

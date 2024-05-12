import hashlib
import random
import math

print("Setting up RSA")
p = int(input("Enter a prime number p:\n"))
q = int(input("Enter a prime number q:\n"))

n = p * q
fn = (p - 1) * (q - 1)

e = random.randint(2, fn - 1)
while math.gcd(e, fn) != 1:
    e = random.randint(2, fn - 1)

d = pow(e, -1, fn)

print(f"Public key (e, n) is ({e}, {n})")
print(f"Private key (d, n) is ({d}, {n})")

def encrypt(k, plaintext):
    e,n = k
    ct = pow(plaintext, e, n)
    return ct

def decrypt(k, ciphertext):
    d,n = k
    decrypted_pt = pow(ciphertext, d, n)
    return decrypted_pt

hasher = hashlib.md5()

print("\nSender Side")
message = input("Enter the message: ")
hasher.update(message.encode())
message_hash_sender = int(hasher.hexdigest(), 16) % n
print(f"Message Digest : {message_hash_sender}")

signature = encrypt((e, n), message_hash_sender)
print(f"\nSignature : {signature}")
print(f"Sender sends (Message, Signature) to Receiver : {(message, signature)}")

print("\nReceiver Side")

message_hash_receiver = int(hasher.hexdigest(), 16) % n
print(f"\nHash of message at Receiver : {message_hash_receiver}")
hashfromsignature = decrypt((d, n), signature)
print(f"Hash from signature : {hashfromsignature}")
if hashfromsignature == message_hash_receiver:
    print("\nVerifed as both hash matches")
else:
    print("\nError")
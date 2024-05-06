import hashlib
import rsa

def md5_hash(message):
    md5_hasher = hashlib.md5()
    md5_hasher.update(message.encode())
    hash_value = md5_hasher.hexdigest()

    return hash_value

def generate_keys():
    # Generate RSA keys
    public_key, private_key = rsa.newkeys(1024)
    return public_key, private_key

def sign(message, private_key):
    hashed_message = md5_hash(message)
    # Sign the hashed message using the private key
    signature = rsa.sign(hashed_message.encode(), private_key, 'MD5')

    return signature

def verify(message, signature, public_key):
    hashed_message = md5_hash(message)
    # Verify the signature using the public key
    try:
        rsa.verify(hashed_message.encode(), signature, public_key)
        return True
    except rsa.VerificationError:
        return False

message = input("Enter the message: ")
public_key, private_key = generate_keys()

signature = sign(message, private_key)
print("Signature:", signature)

is_verified = verify(message, signature, public_key)
print("Signature Verified:", is_verified)

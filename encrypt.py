import hashlib
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()

def write_key(key, file_name):
    with open(file_name, 'wb') as filekey:
        filekey.write(key)

write_key(key, 'my_key.key')

# Encrypting a file

# Opening the key
def load_key(file_name):
    with open(file_name, 'rb') as filekey:
        key = filekey.read()
    return key

key = load_key('my_key.key')
print(key)

# Using the generated key
f = Fernet(key)

with open('Linux for Beginners.zip', 'rb') as original_file:
    original = original_file.read()

length = len(original)
print(f'Length of this bytes object is {round(length/1024/1024, 2)} megabytes.')
original_sha256_checksum = hashlib.sha256(original).hexdigest()
print(f'Calculate the SHA-256 checksum: {original_sha256_checksum}')

def write_checksum(checksum, file_name):
    with open(file_name, 'w') as filechecksum:
        filechecksum.write(checksum)

write_checksum(original_sha256_checksum, 'original_checksum.txt')

# To encrypt the string string must be encoded to byte string before encryption
encrypted = f.encrypt(original)

length = len(encrypted)
print(f'Length of this encrypted object is {round(length/1024/1024, 2)} megabytes.')

# Writing the encrypted file
with open ('Linux for Beginners.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# Decrypt the encrypted file

# Using the key
key = load_key('my_key.key')
f = Fernet(key)

# Opening the encrypted file
with open('Linux for Beginners.enc', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

length = len(encrypted)
print(f'Length of this encrypted file is {round(length/1024/1024, 2)} megabytes.')

# Decrypting the file
decrypted = f.decrypt(encrypted)

length = len(decrypted)
print(f'Length of this decrypted object is {round(length/1024/1024, 2)} megabytes.')
returned_sha256_checksum = hashlib.sha256(decrypted).hexdigest()
print(f'Calculate the SHA-256 checksum: {returned_sha256_checksum}')

def load_checksum(file_name):
    with open(file_name, 'r') as filechecksum:
        checksum = filechecksum.read()
    return checksum

original_sha256_checksum = load_checksum('original_checksum.txt')

# Compare and verify SHA-256 checksum
if original_sha256_checksum == returned_sha256_checksum:
    print("SHA-256 checksum verified.")

    with open('Linux for Beginners enc.zip', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

else:
    print("SHA-256 checksum verification failed.")

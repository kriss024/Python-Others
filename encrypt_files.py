import hashlib
from cryptography.fernet import Fernet

# Creating a Key
key = Fernet.generate_key()

def write_key(key, file_name):
    with open(file_name, 'wb') as mykey:
        mykey.write(key)
        
write_key(key, 'my_key.key')
    
# Loading a Key
def load_key(file_name):
    with open(file_name, 'rb') as mykey:
        key = mykey.read()
    return key

key = load_key('my_key.key')
print(key)

# Encrypting a File
f = Fernet(key)

with open('biblia_linux.zip', 'rb') as original_file:
    original = original_file.read()

length = len(original)
print(f'Length of this bytes object is {round(length/1024/1024,2)} megabytes.')
original_md5 = hashlib.md5(original).hexdigest()
print(f'Hexadecimal digest of the hash {original_md5}')

encrypted = f.encrypt(original)

length = len(encrypted)
print(f'Length of this encrypted object is {round(length/1024/1024,2)} megabytes.')

with open ('biblia_linux.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
    
ls = list(set(encrypted.decode("utf-8")))
ls.sort()
ls = "".join(ls)
print(f'Decode bytes to string: "{ls}"')
    
#Decrypting a File
key = load_key('my_key.key')
f = Fernet(key)

with open('biblia_linux.enc', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()
    
length = len(encrypted)
print(f'Length of this encrypted file is {round(length/1024/1024,2)} megabytes.')

decrypted = f.decrypt(encrypted)

length = len(decrypted)
print(f'Length of this decrypted object is {round(length/1024/1024,2)} megabytes.')
md5_returned = hashlib.md5(decrypted).hexdigest()
print(f'Hexadecimal digest of the hash {md5_returned}')

# Compare and Verify MD5 hash
if original_md5 == md5_returned:
    print("MD5 verified.")
    
    with open('biblia_linux_enc.zip', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
        
else:
    print("MD5 verification failed.")

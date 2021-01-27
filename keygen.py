import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

password_provided = input("Please enter a password: ")  # This is input in the form of a string
password = password_provided.encode()  # Convert to type bytes
salt =  b'\xc7d\xb4`\xebK\x14\xe7z\x8fQo\xa0\xf8\xb7\xe8\xec#n\xaf\xaf!_\xff\xfeZ\xa1H\x80W\x08\xf4' # a key from os.urandom(32) of type bytes
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
print(key.decode())

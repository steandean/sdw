from cryptography.fernet import Fernet

key = input("Please input the encryption key: ")

cipher = Fernet(key)

filename = 'roster'

with open(filename, 'rb') as f:
    e_file = f.read()  # Read the bytes of the input file

encrypted_file = cipher.encrypt(e_file)

with open("encrypted_" + filename, 'wb') as ef:
    ef.write(encrypted_file)  # Write the encrypted bytes to the output file

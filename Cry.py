#https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
from colorama import init, Fore, Back, Style
from cryptography.fernet import Fernet
import os
from os import scandir
import hashlib
import getpass

init()

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def ls_dir(path):
    return [obj.name for obj in scandir(path) if obj.is_file()]

def hash_password(password):
    hash_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hash_password

try:
    disk_file = open("banner.txt",'r',encoding="utf8")
    banner = disk_file.read()
    print(Style.DIM+Fore.MAGENTA+banner)
    disk_file.close()
except:
    print(Style.DIM+Fore.MAGENTA+"AMG CRY")

print(Style.DIM+Fore.MAGENTA+"[INPUT] Insert your password: ", end="")
password = getpass.getpass("")
password_banner = ""

hash_password = hash_password(password)

print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
print(Style.DIM+Fore.BLUE+"Password Hash: " + hash_password)

if hash_password == "6dc7a808a4185a718dc15bc20449fab5":
    Key_file = "Correct"
    key = "XtfES6tiITwoQuJxMetmC35MTh5-MxmsWYMk7FrF0o8="

    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Dir: "+os.getcwd()+"\Safe_Box")
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"File Key: "+Key_file)
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Files: ")

    files = ls_dir(os.getcwd()+"/Safe_Box")

    for file in files:
        decrypt("Safe_Box/"+file, key)
        print("        ⬡ "+Style.DIM+Fore.MAGENTA+file, end="")
        print(Style.DIM+Fore.BLUE+" File Decrypted")

    print(Style.DIM+Fore.MAGENTA+"[INPUT] ", end="")
    print(Style.DIM+Fore.BLUE+"Press key to continue...", end="")
    input()
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Files: ")

    for file in files:
        encrypt("Safe_Box/"+file, key)
        print("        ⬡ "+Style.DIM+Fore.MAGENTA+file, end="")
        print(Style.DIM+Fore.BLUE+" File Encripted")

else:
    Key_file = "Incorrect"
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"File Key: " + Key_file)
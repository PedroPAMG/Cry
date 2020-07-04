#https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
from colorama import init, Fore, Back, Style
from cryptography.fernet import Fernet
import os
from os import scandir
import hashlib

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

def hash_and_key():
    read_file_key = open("KEY", "r")
    key = read_file_key.read()
    read_file_key.close()
    key = key[:44]
    key_hash = hashlib.md5(key.encode('utf-8')).hexdigest()
    return key_hash, key

try:
    disk_file = open("banner.txt",'r',encoding="utf8")
    banner = disk_file.read()
    print(Style.DIM+Fore.MAGENTA+banner)
    disk_file.close()
except:
    print(Style.DIM+Fore.MAGENTA+"AMG CRY")

key_hash, key = hash_and_key()

print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
print(Style.DIM+Fore.BLUE+"Key Hash: " + key_hash)

if key_hash == "53d0a36d7fb8dcc87f3f0decae52f49e":
    Key_file = "Correct"

    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Dir: "+os.getcwd()+"\Safe_Box")
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"File Key: "+Key_file)
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Files: ")

    files = ls_dir(os.getcwd()+"/Safe_Box")

    for file in files:
        decrypt("Safe_Box/"+file, key)
        print("        "+Style.DIM+Fore.MAGENTA+file, end="")
        print(Style.DIM+Fore.BLUE+" File Decrypted")

    print(Style.DIM+Fore.MAGENTA+"[INPUT] ", end="")
    print(Style.DIM+Fore.BLUE+"Press key to continue...", end="")
    input()
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Files: ")

    for file in files:
        encrypt("Safe_Box/"+file, key)
        print("        "+Style.DIM+Fore.MAGENTA+file, end="")
        print(Style.DIM+Fore.BLUE+" File Encripted")

else:
    Key_file = "Incorrect"
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"File Key: " + Key_file)
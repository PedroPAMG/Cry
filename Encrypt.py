#https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
from colorama import init, Fore, Back, Style
from cryptography.fernet import Fernet
import os
from os import scandir
import hashlib

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def ls_dir(path):
    return [obj.name for obj in scandir(path) if obj.is_file()]

def hash_and_key():
    read_file_key = open("KEY.key", "r")
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

encrypt_file_or_dir = input(Style.DIM+Fore.MAGENTA+"[INPUT]"+Style.DIM+Fore.BLUE+" Encript File(0) or Directory(1): ")

if encrypt_file_or_dir == "0":
    file_name = input(Style.DIM+Fore.MAGENTA+"[INPUT]"+Style.DIM+Fore.BLUE+" What is the file name? : ")
    encrypt(file_name, key)

    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Files: ")
    print("        "+Style.DIM+Fore.MAGENTA + file_name, end="")
    print(Style.DIM+Fore.BLUE+" File Encripted")

elif encrypt_file_or_dir == "1":
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Dir: "+os.getcwd()+"\Safe_Box")
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"Files: ")

    files = ls_dir(os.getcwd()+"/Safe_Box")

    for file in files:
        encrypt("Safe_Box/"+file, key)
        print("        "+Style.DIM+Fore.MAGENTA+file, end="")
        print(Style.DIM+Fore.BLUE+" File Encripted")
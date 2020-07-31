#https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
from colorama import init, Fore, Back, Style
from cryptography.fernet import Fernet
import os
from os import scandir
import hashlib
import getpass

init()

def file_hash_password_and_cripto_key():
    key_file = open("KEY.key","r")
    key_and_password = key_file.read()
    key_hash = key_and_password[:44]
    password_hash = key_and_password[45:]
    return key_hash, password_hash

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

def def_to_hash_password(password):
    hash_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    return hash_password

def write_key():
    new_key = str(Fernet.generate_key())
    new_key = new_key.replace("'","")
    new_key = new_key.replace("b","")
    with open("KEY.key", "r+") as key_file:
        old = key_file.read()
        old_key = old[:44]
        password_hash = old[45:]
    with open("KEY.key", "w+") as key_file:
        key_file.write(new_key+"\n"+password_hash)
    return old_key, new_key

def write_password(new_password):
    new_password = def_to_hash_password(new_password)
    with open("KEY.key", "r+") as key_file:
        old = key_file.read()
        key = old[:44]
    with open("KEY.key", "w+") as key_file:
        key_file.write(key+"\n"+new_password)

try:
    disk_file = open("banner.txt",'r',encoding="utf8")
    banner = disk_file.read()
    print(Style.DIM+Fore.MAGENTA+banner)
    disk_file.close()
except:
    print(Style.DIM+Fore.MAGENTA+"AMG CRY")

key_hash, password_hash = file_hash_password_and_cripto_key()

print(Style.DIM+Fore.MAGENTA+"[INPUT] ", end="")
print(Style.DIM+Fore.BLUE+"Insert your password: ", end="")
password = getpass.getpass("")
password_banner = ""

hash_password = def_to_hash_password(password)

print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
print(Style.DIM+Fore.BLUE+"Password Hash: " + hash_password)

if hash_password == password_hash:
    Key_file = "Correct"
    print(Style.DIM+Fore.BLUE+"\t1) Generate new cripto key \n\t2) Set new password \n\t3) Desencript files")
    print(Style.DIM+Fore.MAGENTA+"[INPUT] ", end="")
    print(Style.DIM+Fore.BLUE+"What do you Want?: ", end="")

    operation = int(input())

    if operation == 1:
        old_key, new_key = write_key()
        files = ls_dir(os.getcwd()+"/Safe_Box")
        
        for file in files:
            decrypt("Safe_Box/"+file, old_key)
            encrypt("Safe_Box/"+file, new_key)

        print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
        print(Style.DIM+Fore.BLUE+"Generate new cripto key successful")

    elif operation == 2:
        print(Style.DIM+Fore.MAGENTA+"[INPUT] ", end="")
        print(Style.DIM+Fore.BLUE+"Insert your new password: ", end="")
        new_password = getpass.getpass("")
        write_password(new_password)
        print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
        print(Style.DIM+Fore.BLUE+"Generate new password successful")

    elif operation == 3:
            print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
            print(Style.DIM+Fore.BLUE+"Dir: "+os.getcwd()+"\Safe_Box")
            print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
            print(Style.DIM+Fore.BLUE+"File Key: "+Key_file)
            print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
            print(Style.DIM+Fore.BLUE+"Files: ")

            files = ls_dir(os.getcwd()+"/Safe_Box")

            for file in files:
                decrypt("Safe_Box/"+file, key_hash)
                print("        ⬡ "+Style.DIM+Fore.MAGENTA+file, end="")
                print(Style.DIM+Fore.BLUE+" File Decrypted")

            print(Style.DIM+Fore.MAGENTA+"[INPUT] ", end="")
            print(Style.DIM+Fore.BLUE+"Press key to continue...", end="")
            input()
            print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
            print(Style.DIM+Fore.BLUE+"Files: ")

            for file in files:
                encrypt("Safe_Box/"+file, key_hash)
                print("        ⬡ "+Style.DIM+Fore.MAGENTA+file, end="")
                print(Style.DIM+Fore.BLUE+" File Encripted")
    else:
        print("Error")
else:
    Key_file = "Incorrect"
    print(Style.DIM+Fore.MAGENTA+"[INFO]  ", end="")
    print(Style.DIM+Fore.BLUE+"File Key: " + Key_file)

print(Style.DIM+Fore.MAGENTA+"[INPUT] ", end="")
print(Style.DIM+Fore.BLUE+"Press key to continue...", end="")
input()
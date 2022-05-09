

import re
import pickle
import string
import json


def check_password(password):
    s = password
    l = 0
    t = 0
    p = 0
    d = 0
    if (len(s) < 16) and (len(s) > 5):
        for i in s:

            # counting lowercase alphabets
            if (i.islower()):
                l += 1

            # counting uppercase alphabets
            if (i.isupper()):
                t += 1

            # counting digits
            if (i.isdigit()):
                d += 1

            # counting the mentioned special characters
            if (
                    i == '@' or i == '$' or i == '_' or i == '!' or i == '#' or i == '%' or i == '&' or i == '*' or i == '.' or i == '?'):
                p += 1
    if (l >= 1 and t >= 1 and p >= 1 and d >= 1):
        return 1
    else:
        print("Invalid Password")
        return 0


def check_email(email):
    x = r'\b[A-Za-z0-9]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(x, email)):
        return 1
    else:
        print("Invalid Email")
        return 0


def Register():
    print('Enter username')
    username = input()
    u = 0
    p = 0
    u = check_email(username)
    print('Enter the password')
    password = input()
    p = check_password(password)
    # python 3 program to write and read dictionary to text file
    if u == 1 and p == 1:

        with open('database.txt', 'a+') as convert_file:
            convert_file.write(username)
            convert_file.write("\n")
            convert_file.write(password)
            convert_file.write("\n")
        with open('database.txt','r') as f:
             # reconstructing the data as a dictionary
             #js = json.loads(data)
             print(f.read())

             print("Registeration complete please login")
             login()
    else:
       Register()


def check_userinfo(username, password):
    file = open("database.txt", "r")
    file_contents = file.read()
    print(file_contents)
    if username in file_contents and password in file_contents:
        print('Logged in ')
    else:
        return 0
    file.close()


def forgot_password():
    print("enter the username")
    key = input()
    #count=0
    flag =0
    file = open("database.txt", "r")
    for line in file:
        #count += 1
        #print(count)
        if key in line:
            print("Your password is  : " + file.readline())
            flag=1
        else:
            continue
    if flag==0:
        print("Your username does not exist please register")
        Register()
    else:
        pass
    file.close()



def login():
    print("Please enter your username")
    username = input()
    # check_email(username)
    print("Enter your password")
    password = input()
    # check_password(password)
    a = check_userinfo(username, password)
    if a == 0:
        forgot_password()


print("enter 0 to login \n enter 1 to register ")
print("If you have forgotton your password and wants to retrieve it please enter 3 ")
n = int(input())
if n == 0:
    login()
elif n == 1:
    Register()
else:
    forgot_password()












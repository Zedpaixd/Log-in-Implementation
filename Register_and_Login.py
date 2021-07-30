from os import system, name
from time import sleep

def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def Encrypt():
    pass

def Decrypt():
    pass

def Register():
    pass

def LogIn():

    access = False

    print ("Username?")
    usernameInput = input()
    clear()

    print ("Password?")
    passwordInput = input()
    clear()

    if (usernameInput in usernames):
        if (passwords[usernames.index(usernameInput)] == passwordInput):
            access = True

    return access



# Loads all accounts into memory

usernames = []
passwords = []

with open("accounts.txt","r") as AccountList:

    temp = AccountList.readlines()

    for i in range(0,len(temp)):

        if (i != len(temp)-1):
            temp[i] = temp[i][:-1]

        tempSplit = temp[i].split(" | ")
        usernames.append(tempSplit[0])
        passwords.append(tempSplit[1])





access = False

while (access != True):

    #Temporary, will use actual UI later
    print("1 - register \n2- log in")

    userInput = input()
    clear()

    if (userInput == 1):
        Register()

    else:
        access = LogIn()
        if (access == False):
            clear()
            print ("Something you have entered is incorrect")
            sleep(2)
            clear()
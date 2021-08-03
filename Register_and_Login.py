from os import system, name
from time import sleep
import json
from datetime import date

# TODO:
# - Tkinter UI
# - More password requirements, such as 1 special character





# Defining a temporary clear screen for the console variant of the program

def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')





# Loads all encrypted accounts into memory



def loadToMemory():

    with open('database.json', 'r') as users:

        global userAccounts
        userAccounts = json.load(users)

    global usernames
    usernames = []
    global passwords
    passwords = []

    for account in userAccounts['users']:
        usernames.append(account['username'])
        passwords.append(account['password'])

    return usernames,passwords





# Budget encrypt function

def Encrypt(toEncrypt):
    toEncrypt = toEncrypt[::-1]
    return toEncrypt





# Budget decrypt function

def Decrypt(toDecrypt):
    toDecrypt=toDecrypt[::-1]
    return toDecrypt




# Similarity check using dynamic programming and a memoization table

def similarityCheck(string1, string2):

    size1 = len(string1)
    size2 = len(string2)

    dp = [[0 for x in range(size2 + 1)] for x in range(size1 + 1)]

    for i in range(size1 + 1):

        for j in range(size2 + 1):
 

            if i == 0:
                dp[i][j] = j   
 
            elif j == 0:
                dp[i][j] = i   
 

            elif string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
 

            else:
                dp[i][j] = 1 + min(dp[i][j-1],      
                                   dp[i-1][j],      
                                   dp[i-1][j-1])    
 
    return dp[size1][size2]




def addToDatabase(username,password):

    encryptedUsername = Encrypt(username)
    encryptedPassword = Encrypt(password)

    tempAccount = {
    "username":encryptedUsername,
    "password":encryptedPassword,
    "creation_date":date.today().strftime("%d/%m/%Y")
    }
    
    userAccounts['users'].append(tempAccount)


    with open('database.json', 'w') as users:

        json.dump(userAccounts, users, indent=2)





# Function handling the registration process

def Register():

    # Handling username input and if it abides by the requirements of a username

    usernameInput = "a"

    while (len(usernameInput) <= 4 or Encrypt(usernameInput) in usernames):

        clear()
        print("For your username, please make sure that:\n- Your username is longer than 4 characters\n- It has not been used before by anyone else\n")
        usernameInput = input("Input your username:")
        if (len(usernameInput) <= 4 or Encrypt(usernameInput) in usernames):
            print("Invalid username.")
            sleep(2)

    # Handling password input and making sure it fits the mandatory criterias

    passwordInput = "a"
    inUsername = False
    digitOrSpChr = False

    while ((len(passwordInput) < 4) or (similarityCheck(passwordInput,usernameInput) <= (len(passwordInput)/2)) or (inUsername == True) or (digitOrSpChr == False)):
        inUsername = False
        digitOrSpChr == False

        clear()
        print("Your username is: {}".format(usernameInput))
        print("For your passsword, please make sure the following criterias are met:\n- Your password must be longer than 4 characters\n- Your password must not be too similar to your username\n- Your password must not appear in your username\n- Your password must contain at least one digit or one special character ( `~!@#$%^&*() )\n")
        passwordInput = input("Input your password:")

        tempPasswordInput = passwordInput
        
        for char in "1234567890!@#$%^&*()`~":
            if char in passwordInput:
                digitOrSpChr = True
                break


        while len(tempPasswordInput) > len(passwordInput)/2:
            tempPasswordInput = tempPasswordInput[:len(tempPasswordInput)-1:]
            if (tempPasswordInput.lower() in usernameInput.lower()):
                inUsername = True

        if (len(usernameInput) < 4) or (similarityCheck(passwordInput,usernameInput) <= (len(passwordInput)/2) or (inUsername == True) or (digitOrSpChr == False)):
            print("Unfitting password.")
            sleep(2)

    clear()
    addToDatabase(usernameInput,passwordInput)
    loadToMemory()



# Function handling the log in process

def LogIn():

    access = False

    usernameInput = input("Input your username: ")
    clear()

    passwordInput = input("Input your password: ")
    clear()

    if (Encrypt(usernameInput) in usernames):
        if (Decrypt(passwords[usernames.index(Encrypt(usernameInput))]) == passwordInput):
            access = True

    return access







# The "main" of the program

access = False
loadToMemory()


while (access != True):

    clear()

    
    print("1 - register \n2 - log in") #Temporary, will use actual UI later via tkinter

    userInput = input()
    clear()

    if (userInput == str(1)):
        Register()

    else:
        access = LogIn()
        if (access == False):
            clear()
            print ("Something you have entered is incorrect")
            sleep(2)
            clear()

        else:
            print("Access Granted")
            sleep(2)
            clear()

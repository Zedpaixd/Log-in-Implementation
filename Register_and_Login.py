from os import system, name
from time import sleep





def clear():

    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')





# Loads all encrypted accounts into memory

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







def Encrypt(toEncrypt):
    toEncrypt = toEncrypt[::-1]
    return toEncrypt







def Decrypt(toDecrypt):
    toDecrypt=toDecrypt[::-1]
    return toDecrypt






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
    print("WIP")
    sleep(5)






def Register():

    # Handling username input

    usernameInput = "a"

    while (len(usernameInput) <= 4 or Encrypt(usernameInput) in usernames):

        clear()
        print("For your username, please make sure that:\n- Your username is longer than 4 characters\n- It has not been used before by anyone else\n")
        usernameInput = input("Input your username:")
        if (len(usernameInput) <= 4 or Encrypt(usernameInput) in usernames):
            print("Invalid username.")
            sleep(2)

    #Handling password input

    passwordInput = "a"
    inUsername = False

    while ((len(passwordInput) < 4) or (similarityCheck(passwordInput,usernameInput) <= (len(passwordInput)/2)) or (inUsername == True)):
        inUsername = False

        clear()
        print("Your username is: {}".format(usernameInput))
        print("For your passsword, please make sure the following criterias are met:\n- Your password must be longer than 4 characters\n- Your password must not be too similar to your username\n- Your password must not appear in your username\n")
        passwordInput = input("Input your password:")

        tempPasswordInput = passwordInput
        
        while len(tempPasswordInput) > len(passwordInput)/2:
            tempPasswordInput = tempPasswordInput[:len(tempPasswordInput)-1:]
            if (tempPasswordInput.lower() in usernameInput.lower()):
                inUsername = True

        if (len(usernameInput) < 4) or (similarityCheck(passwordInput,usernameInput) <= (len(passwordInput)/2) or (inUsername == True)):
            print("Unfitting password.")
            sleep(2)
    clear()
    addToDatabase(usernameInput,passwordInput)


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









access = False

while (access != True):

    clear()
    #Temporary, will use actual UI later
    print("1 - register \n2 - log in")

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

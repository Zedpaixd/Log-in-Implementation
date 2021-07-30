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

    if (Encrypt(usernameInput) in usernames):
        if (Decrypt(passwords[usernames.index(Encrypt(usernameInput))]) == passwordInput):
            access = True

    return access









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

        else:
            print("Access Granted")
            sleep(2)
            clear()

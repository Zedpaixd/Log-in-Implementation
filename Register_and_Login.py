from os import system, name
from time import sleep
import json
from datetime import date
import tkinter as gui
from tkinter import messagebox
from Decryption import *
from Encryption import *

#TODO:
#    add email to account





# ------------ L O G I N  H A N D L I N G ------------

def accessGrantedGui():
    messagebox.showinfo("Welcome in","Access Granted.")



def logInSubmit():
 
    usernameInput=username.get()
    passwordInput=password.get()

    if (Encrypt(usernameInput) in usernames):
        if (Decrypt(passwords[usernames.index(Encrypt(usernameInput))]) == passwordInput):
            global access
            access = True

    if (access == True):
        accessGrantedGui()
        logInGui.destroy()

    username.set("")
    password.set("")



def logIn():
    
    window.destroy()

    global logInGui
    logInGui = gui.Tk()
    logInGui.geometry("325x150")



    global username
    username=gui.StringVar()

    usernameLabel = gui.Label(logInGui, 
                           text = 'Username:', 
                           font=('Cambria',12, 'bold'))
  
    usernameEntry = gui.Entry(logInGui, 
                           textvariable = username, 
                           font=('Cambria',12,'normal'))
  
    usernameLabel.place(x = 15,
                        y = 15)

    usernameEntry.place(x = 105,
                        y = 15)



    global password
    password=gui.StringVar()

    passwordLabel = gui.Label(logInGui, 
                            text = 'Password:', 
                            font = ('Cambria',12,'bold'))

    passwordEntry=gui.Entry(logInGui, 
                          textvariable = password, 
                          font = ('Cambria',12,'normal'), 
                          show = '*')
  
    passwordLabel.place(x = 15,
                        y = 65)

    passwordEntry.place(x = 105,
                        y = 65)



    submitButton=gui.Button(logInGui, 
                       text = 'Submit', 
                       command = logInSubmit)

    submitButton.place(x = 140,
                       y = 105)

    

    logInGui.mainloop()
   


    if (access == False):
        windowCreate()





# ------------ R E G I S T R A T I O N  H A N D L I N G ------------

def registerSubmit():
 
    usernameInput=username.get()
    passwordInput=password.get()
    emailInput=email.get()

    fittingAccount = True

    # Handling username input and if it abides by the requirements of a username

    if (len(usernameInput) <= 4 or Encrypt(usernameInput) in usernames):
        messagebox.showerror("","Unfitting Username") 
        fittingAccount = False

    # Handling password input and making sure it fits the mandatory criterias

    inUsername = False
    digitOrSpChr = False

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
        messagebox.showerror("","Unfitting Password") 
        fittingAccount = False

    if (fittingAccount == True):
        addToDatabase(usernameInput,passwordInput,emailInput)
        loadToMemory()

    registerGui.destroy()

    username.set("")
    password.set("")
    email.set("")



def register():

    window.destroy()

    global registerGui
    registerGui = gui.Tk()
    registerGui.geometry("450x445")

    requirements = gui.Label(registerGui, text = "Username and password requirements:")
    requirements.config(font =("Cambria", 14))
    requirements.place(x = 50,
                       y = 10)

    r1 = gui.Label(registerGui, text = "- The username must be unique and longer than 4 characters")
    r1.config(font =("Cambria", 10))
    r1.place(x = 40,
             y = 45)

    r2 = gui.Label(registerGui, text = "- The password must not appear in, nor be too similar to the username")
    r2.config(font =("Cambria", 10))
    r2.place(x = 15,
             y = 65)

    r3 = gui.Label(registerGui, text = "- The password must be at least 5 characters or longer")
    r3.config(font =("Cambria", 10))
    r3.place(x = 55,
             y = 85)

    r4 = gui.Label(registerGui, text = "- The password must contain one digit / one special character or more")
    r4.config(font =("Cambria", 10))
    r4.place(x = 16,
             y = 105)



    global email

    email=gui.StringVar()

    emailLabel = gui.Label(registerGui, 
                            text = 'Email:', 
                            font = ('Cambria',12,'bold'))

    emailEntry=gui.Entry(registerGui, 
                          textvariable = email, 
                          font = ('Cambria',12,'normal'))  
  
    emailLabel.place(x = 180,
                     y = 145)

    emailEntry.place(x = 130,
                     y = 175)



    global username

    username=gui.StringVar()

    usernameLabel = gui.Label(registerGui, 
                           text = 'Username:', 
                           font=('Cambria',12, 'bold'))
  
    usernameEntry = gui.Entry(registerGui, 
                           textvariable = username, 
                           font=('Cambria',12,'normal'))
  
    usernameLabel.place(x = 180,
                        y = 225)

    usernameEntry.place(x = 130,
                        y = 255)



    global password

    password=gui.StringVar()

    passwordLabel = gui.Label(registerGui, 
                            text = 'Password:', 
                            font = ('Cambria',12,'bold'))

    passwordEntry=gui.Entry(registerGui, 
                          textvariable = password, 
                          font = ('Cambria',12,'normal'), 
                          show = '*')

    passwordLabel.place(x = 180,
                        y = 305)

    passwordEntry.place(x = 130,
                        y = 335)



    submitButton=gui.Button(registerGui, 
                       text = 'Submit',
                       height = 1, 
                       width = 9,
                       command = registerSubmit)

    submitButton.place(x = 180,
                       y = 380)


    registerGui.mainloop()
    windowCreate()





def addToDatabase(username,password,email):

    encryptedUsername = Encrypt(username)
    encryptedPassword = Encrypt(password)
    encryptedEmail = Encrypt(email)

    tempAccount = {
    "email":encryptedEmail,
    "username":encryptedUsername,
    "password":encryptedPassword,
    "creation_date":date.today().strftime("%d/%m/%Y")
    }
    
    userAccounts['users'].append(tempAccount)

    with open('database.json', 'w') as users:
        json.dump(userAccounts, users, indent=2)





# ------------ M A I N  W I N D O W  H A N D L I N G ------------

def windowCreate():

    global window
    window = gui.Tk()
    window.geometry("165x110")



    logInButton = gui.Button(
        text = "Log In",
        width = 8,
        height = 1,
        bg = "grey",
        fg = "white",
        command = logIn)

    logInButton['font'] = "Cambria"

    logInButton.grid(row=3, 
                     column=1, 
                     padx=40, 
                     pady=15)



    registerButton = gui.Button(
        text = "Register",
        width = 8,
        height = 1,
        bg = "grey",
        fg = "white",
        command = register)

    registerButton['font'] = "Cambria"

    registerButton.grid(row=6, 
                        column=1, 
                        padx=40, 
                        pady=0)



    window.mainloop()





# ------------ L O A D I N G  D A T A B A S E  T O  M E M O R Y ------------

def loadToMemory():

    with open('database.json', 'r') as users:
        global userAccounts
        userAccounts = json.load(users)

    global emails
    emails = []

    global usernames
    usernames = []

    global passwords
    passwords = []

    for account in userAccounts['users']:
        usernames.append(account['username'])
        passwords.append(account['password'])
        emails.append(account['email'])





# ------------ C H E C K I N G  S I M I L A R I T Y ------------

def similarityCheck(string1, string2): # Similarity check using dynamic programming and a memoization table

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





# ------------ M A I N  F U N C T I O N ------------

global access
access = False
loadToMemory()
windowCreate()












# Function handling the registration process

def Register():

    # Handling username input and if it abides by the requirements of a username

    usernameInput = "a"

    while (len(usernameInput) <= 4 or Encrypt(usernameInput) in usernames):

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

    addToDatabase(usernameInput,passwordInput)
    loadToMemory()
from os import system, name
from time import sleep
import json
from datetime import date
import tkinter as gui
from tkinter import messagebox
from Decryption import *
from Encryption import *
import re





# ------------ L O G I N  H A N D L I N G ------------

def accessGrantedGui():
    messagebox.showinfo("Welcome in","Access Granted.")



def logInSubmit():

    # Gets username and password from the input boxes
    usernameInput=username.get()
    passwordInput=password.get()

    if (Encrypt(usernameInput) in usernames): # If inputted username in existing usernames
        if (Decrypt(passwords[usernames.index(Encrypt(usernameInput))]) == passwordInput): # If inputted password matches the username's password
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


    # Username text & input box
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


    # Password text & input box
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


    # Submit button
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
 
    # Gets username, password and email from the input boxes
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


    regexMailCheck = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'

    # Making sure the email follows the certain form: [text]@[text].[text]

    if(re.fullmatch(regex, emailInput)):
        fittingAccount = True
    else:
        fittingAccount = False

    #if (("@" not in emailInput) or ("." not in emailInput) or (emailInput.index("@") > emailInput.rfind("."))):
    #    messagebox.showerror("","Unfitting Email") 
    #    fittingAccount = False

    # Used an elif to make the code easier to read, sort of. Same thing from above
    #elif ((emailInput.index("@") == emailInput.rfind(".") - 1) or (emailInput.rfind(".") == len(emailInput)-1) or (emailInput.index("@") == 0) or (emailInput.count("@") > 1)):
    #    messagebox.showerror("","Unfitting Email") 
    #    fittingAccount = False


    if (fittingAccount == True):
        addToDatabase(usernameInput,passwordInput,emailInput)
        loadToMemory()

    registerGui.destroy()

    username.set("")
    password.set("")
    email.set("")



def register():

    window.destroy()

    # Defining + placing window sizes and the UI elements
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



    # Email input box
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



    # Username input box
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



    # Password input box
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

    # Creating a dictionary to "dump" into the json file
    tempAccount = {
    "email":encryptedEmail,
    "username":encryptedUsername,
    "password":encryptedPassword,
    "creation_date":date.today().strftime("%d/%m/%Y")
    }
    
    #Adding the account to currently loaded accounts
    userAccounts['users'].append(tempAccount)

    #Rewriting the DB to also include the newly added account 
    with open('database.json', 'w') as users:
        json.dump(userAccounts, users, indent=2)





# ------------ M A I N  W I N D O W  H A N D L I N G ------------

def windowCreate():

    # UI sizing and handling 
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

    # Opening the DB and reading the list of all dictionaries
    with open('database.json', 'r') as users:
        global userAccounts
        userAccounts = json.load(users)

    global emails
    emails = []

    global usernames
    usernames = []

    global passwords
    passwords = []

    # Making the split for each account, where usernames [0] is username for first account and so on..
    for account in userAccounts['users']:
        usernames.append(account['username'])
        passwords.append(account['password'])
        emails.append(account['email'])





# ------------ C H E C K I N G  S I M I L A R I T Y ------------

# Similarity check using dynamic programming and a memoization table. To not flood the code with comments, the explanation can be easily found online
def similarityCheck(string1, string2): 

    size1 = len(string1)
    size2 = len(string2)

    SimilarityTable = [[0 for x in range(size2 + 1)] for x in range(size1 + 1)]

    for i in range(size1 + 1):

        for j in range(size2 + 1):
            
            if i == 0:
                SimilarityTable[i][j] = j   
 
            elif j == 0:
                SimilarityTable[i][j] = i   
 
            elif string1[i-1] == string2[j-1]:
                SimilarityTable[i][j] = SimilarityTable[i-1][j-1]
 
            else:
                SimilarityTable[i][j] = 1 + min(SimilarityTable[i][j-1],      
                                                SimilarityTable[i-1][j],      
                                                SimilarityTable[i-1][j-1])    
 
    return SimilarityTable[size1][size2]





# ------------ M A I N  F U N C T I O N ------------

global access
access = False
loadToMemory()
windowCreate()
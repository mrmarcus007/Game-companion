from ast import Global
import time
import random
import os
import pyfiglet
import sys
warning = pyfiglet.figlet_format("Warning")

def scoreoutput():
    os.system('cls')
    print("\n current scores are")
    print(" ", Team_1, " score ", Team_1_score)
    print(" ", Team_2, " score ", Team_2_score)
    time.sleep(5)
    menu() 

def score():
    global Team_1_score
    global Team_2_score
    print("You are reseting and changing values \n \n")
    print("\n press N to go to the main menu, \n press any-key to go to score only edit, \n Press Y to full edit,")
    A = input("user: ")
    if A == "N":
        menu()
    if A == "Y":
        warning()
    else: 
        Team_1_score = input("team 1 score: ")
        Team_2_score = input("team 2 score: ")
        scorecheck()

def scoreoutput():
    os.system('cls')
    print("\n current points are:")
    print("\n ", Team_1 + " point(s) " + Team_1_score)
    print("\n ", Team_2 + " point(s) " + Team_2_score)
    time.sleep(5)
    menu()

def entry(): 
    global Team_1
    global Team_1_score
    global Team_2
    global Team_2_score
    print("\n you are now editing data \n")
    Team_1 = input("team 1 name: ")
    Team_2 = input("team 2 name: ")
    Team_1_score = input("team 1 score: ")
    Team_2_score = input("team 2 score: ")
    scorecheck()

def FSetup():
    print("\n This is first time set up: This happens everytime you restart the program \n")
    time.sleep(5)
    os.system('cls')
    warning()

def intro():
    global a
    print("\n Welcome to game companion 1.4.1 by Marcus Allison (Python 3.10)")
    print(" ")
    time.sleep(3)
    print("\n Press any key to continue or N to exit")
    print(" ")
    a = input("user: ")
    if a == "N" or a == "n":
        leaving_1()
    else:
        FSetup()

def menu():
    global y
    os.system('cls')
    print("\n welcome to the score page here is a options list")
    print("\n 1. leave")
    print("\n 2. edit score")
    print("\n 3. scoresheet")
    print("\n 4. flip a coin")
    y = input("user: ")
    if y == "1":
        leaving_0()
    if y == "2":
        score()
    if y == "3":
        scoreoutput()
    if y == "4":
        coin()
    else: 
        os.system('cls')
        gobackto1()

def leaving_0():
    os.system('cls')
    print("\n Are you sure you would like to terminate the program? \n Y: Terminate \n N: Back to menu")
    d = input("User: ")
    if d == "Y" or d == "y":
        os.system('cls')
        print("\n Warning. 10 seconds till program termination \n \n Final score \n")
        print("\n", Team_1 + " point(s) " + Team_1_score)
        print("\n", Team_2 + " point(s) " + Team_2_score)
        time.sleep(5)
        exiting()
    if d == "N" or d =="n":
         menu()
    else: 
        gobackto2()

def leaving_1():
    os.system('cls')
    print("\n Are you sure you would like to terminate the program? \n Y: terminate \n N: back to menu")
    d = input("user: ")
    if d == "Y" or d == "y":
        os.system('cls')
        exiting()
    if d == "N" or d =="n":
        menu()
    else: 
        os.system('cls')
        gobackto2()



def gobackto1():
    os.system('cls')
    print("\n please enter a number on screen\n ")
    time.sleep(2)
    menu()

def gobackto2():
    global error
    if a == "N" or a == "n":
        os.system('cls')
        print(warning)
        print("\n please enter a number on screen\n ")
        time.sleep(2)
        os.system('cls')
        leaving_1()
    elif y == "1":
        os.system('cls')
        print(warning)
        print("\n please enter a number on screen\n ")
        time.sleep(2)
        os.system('cls')
        leaving_0()
    else: 
        error = 1
        ErrorHand(error)

def gobackto3():
    os.system('cls')
    print("\n please enter a number or character on screen\n ")
    time.sleep(5)
    os.system('cls')
    leaving_1()

def scorecheck():
    if Team_1 == "":
        os.system('cls')
        print(warning)
        print("\n you have left data empty")
        time.sleep(2)
        os.system('cls')
        warning()
    if Team_2 == "":
        os.system('cls')
        print(warning)
        print("\n you have left data empty")
        time.sleep(2)
        os.system('cls')
        warning()
    else:
        menu()

def Toss():
    return random.choice(["Heads", "Tails"])

def coin():
    os.system('cls')
    print(" task: cointoss \n")
    print(" 3")
    time.sleep(1)
    os.system('cls')
    print(" task: cointoss \n")
    print(" 2")
    time.sleep(1)
    os.system('cls')
    print(" task: cointoss \n")
    print(" 1")
    time.sleep(1)
    os.system('cls')
    print(" task: cointoss \n")
    print(" flipping coin")
    time.sleep(2)
    os.system('cls')
    print(" task: cointoss \n")
    t1 = Toss()
    t2 = Toss()
    t3 = Toss()
    print(t1, t2, t3)
    time.sleep(5)
    os.system('cls')
    menu()

def ErrorHand(code):
    if code == "1":
        os.system('cls')
        print(error)
        print(" An memory error has occured, entering main menu")
        time.sleep(2)
        menu()
    else:
        os.system('cls')
        print(" Welcome - textual graphics module missing, install pyfiglet \n python - m install pyfiglet ")
        intro()
        print(" unkown error has occured, entering main menu")
        time.sleep(2)
        menu()

def welcome():
    try: 
        ascii_banner = pyfiglet.figlet_format("welcome")
        print(ascii_banner)
        intro()
    except 1: 
        print(" Welcome - textual graphics module missing, install pyfiglet \n python - m install pyfiglet ")
        intro()

def warning():
    try: 
        print(warning)
        entry()
    finally:
        print(" warning")
        entry()
       
def exiting():
     print("\n Game companion 1.4.1")
     print("\n Made by Marcus Allison")
     time.sleep(5) 
     quit(0)

welcome() 
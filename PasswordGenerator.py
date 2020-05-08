import random
import sys


#Create three lists
special = "!@#$%&*"
num = "123456789"
chars = "abcdefghijklmnopqrstuvwxyz"

#Main Menu Prompt
print("Welcome to the Password Generator \n")
print("1. Generate Password")
print("2. Cancel\n")


#Ask for User Input
choice = input("Please Select Option Below: ")

#Check to make sure choice is option 1 or 2
while (choice[0] == "1" or choice[0] == "2") == False:
    choice =  input("Invalid option please try again: ")

print("\n\n")

menu = True

while menu == True:
#Check with option chosen on second menu
    if (choice == "1"):
        print("Password Types\n")
        print("1. Basic Password (QWERTY)")
        print("2. Intermediate Password (Alphanumeric)")
        print("3. Strong Password (Alphanumeric w/ Special Character)")
        print("4. Cancel\n")
        passType = input("Please Select Password Type: ")
    
        while (passType[0] == "1" or passType[0] == "2" or passType[0] == "3" or passType[0] == "4") == False:
            passType =  input("Invalid option please try again: ")
    elif (choice == "2"):
        sys.exit()

    guess = True

    password = ""

    ###QWERTY###
    if (passType == "1"):
      ##  clearScreen()
        while guess == True:
            password = ""
            for x in range (10):
                password += random.choice(chars)
            print("\nYour Password is: " + password)
            guessAgain = input("Would you like to generate another? (Y/N): ")
            if guessAgain[0].lower() == "y":
                guess == True
            elif guessAgain[0].lower() == "n":
                break
            else:
                print("\n\nInvalid Answer!")
                break
        
    ###ALPHA_NUMERIC###
    elif (passType == "2"):
        while guess == True:
            password = ""
            for x in range (5):
                password += random.choice(chars) + random.choice(num)
            print("\nYour Password is: " + password)
            guessAgain = input("Would you like to generate another? (Y/N): ")
            if guessAgain[0].lower() == "y":
                guess == True
            elif guessAgain[0].lower() == "n":
                break
            else:
                print("\n\nInvalid Answer!")
                break
        
    ###SPECIAL_CHAR###
    elif (passType == "3"):
        while guess == True:
            password = ""
            for x in range (5):
                password += random.choice(chars) + random.choice(num) + random.choice(special)
            print("\nYour Password is: " + password)
            guessAgain = input("Would you like to generate another? (Y/N): ")
            if guessAgain[0].lower() == "y":
                guess == True
            elif guessAgain[0].lower() == "n":
                break
            else:
                print("\n\nInvalid Answer!")
                break

    ###CANCEL###
    elif (passType == "4"):
        sys.exit()
    

    
        


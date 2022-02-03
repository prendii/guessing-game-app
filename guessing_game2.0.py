import random, time

"""
Created on Wed Feb  2 03:51:16 2022

@author: prendi bobo

Guessing Game -- updated

"""

i = 1
attempts = 0
n = random.randint(0, 100)

print("")
print("-----------------")
print("| guessing game |")
print("|  by: prendi   |")        
print("-----------------")

while i > 0:    

    try:
        guess = int (input("please enter a number between 1 - 100 inclusive: "))
        if guess < n:
            attempts += 1
            print("guess higher...")
        elif guess == n:
            attempts += 1
            i += -1
            print("correct guess! - {} attempts ".format(attempts))
        else:
            attempts += 1
            print("guess lower...")
            
    except ValueError as err:
        print("invalid input.")
        #print(err)
       
time.sleep(3)
print("thank you for playing.")
time.sleep(4)
print("\033[H\033[J")
    


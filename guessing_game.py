# Prendi Bobo
num = 23
i = 1
attempts = 0
while i > 0:    
    
    print("please enter a number between 1 - 100 inclusive: ")
    guess = int (input())
    
    if guess < num:
        attempts += 1
        print("guess higher...")
    elif guess == num:
        attempts += 1
        i += -1
        print("correct guess! - {} attempts ".format(attempts))
    else:
        attempts += 1
        print("guess lower...")




import random
    
number = random.randint(1, 100)
guess = None
    
while guess != number:
    guess = input("guess a number between 1 and 100. ")
    guess = int(guess)
        
    if guess > number:
        print("lower")
    if guess < number:
        print("higher")
        
    if guess == number:
        print("correct")
        break
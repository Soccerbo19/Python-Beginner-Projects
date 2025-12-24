import random
print("Welcome to the Guessing Game!")
start = input("Do you want to play?: ")
if start == "yes":
    print("Okay let's Play!")
else:
    print("Have a good day")
    exit()

diff = input("Choose a difficulty. Enter 'easy' or 'medium' or 'hard': ")
if diff == "easy":
    number = random.randint(1, 10)
if diff == "medium":
    number = random.randint(1, 50)
if diff == "hard":
    number = random.randint(1, 100) 

while True:
    print("Game Started!")
    guess = int(input("Enter your guess: "))
    if guess < number:
        print("Wrong Answer! Its Higher than that.")
    elif guess > number:
        print("Wrong Answer! Its Lower than that")
    elif guess == number:
        print("Good Job! You Got it Right!")
        play_again = input("Do you want to play again?: ")
        if play_again == "yes":
            diff = input("Choose a difficulty. Enter 'easy' or 'medium' or 'hard': ")
            if diff == "easy":
              number = random.randint(1, 10)
            if diff == "medium":
              number = random.randint(1, 50)
            if diff == "hard":
             number = random.randint(1, 100)
        else:
           print("Thanks For Playing! Have a Good Day!")
        break




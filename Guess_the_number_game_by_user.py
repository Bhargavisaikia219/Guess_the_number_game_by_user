import random

def guess(x,y):

    random_number = random.randint(x, y)

    guess = 0

    while guess != random_number:
        guess = int(input(f"Guess the number between {x} and {y}:"))

        if guess < random_number:
            print("Sorry. Guess again. hint: too low")
        elif guess > random_number:
            print("Sorry. Guess again. hint: too high")

    print(f"Hurray! You have guessed the number {random_number} correctly. ")


x=int(input("Enter a range between which you what to guess a random number: lower limit:"))
y=int(input("Enter a range between which you what to guess a random number: upper limit:"))

guess(x,y)
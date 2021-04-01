import random

#defining a function named guess and passing the value of x and y

def guess(x,y):

    #using random.randint that returns a number from a given range

    random_number = random.randint(x, y)

    guess = 0

    #this loop will continue to run till the guess is not correct

    while guess != random_number:
        guess = int(input(f"Guess the number between {x} and {y}:"))

        #if the guess is less than random_number, it gives a hint as too low, otherwise too high

        if guess < random_number:
            print("Sorry. Guess again. hint: too low")
        elif guess > random_number:
            print("Sorry. Guess again. hint: too high")

    #if while condition is false, it means the guess is correct. It directly comes to this line.

    print(f"Hurray! You have guessed the number {random_number} correctly. ")

#taking lower and upper limit of the range from the user

x=int(input("Enter a range between which you what to guess a random number: lower limit:"))
y=int(input("Enter a range between which you what to guess a random number: upper limit:"))

#calling the function

guess(x,y)
import random

def num_generate(min,max):
    number = random.randint(min,max)
    return number

def get_user_number():
    user_guess = int(input("Please guess a number: " ))
    return user_guess

print("Would range would you like me to think of a number within")
minimum = int(input("Enter the Minimum number: "))
maximum = int(input("Enter the Maximum number: "))

comp_number = num_generate(minimum,maximum)
guesses = 0

while True:

    guesses += 1
    user_guess = get_user_number()

    if user_guess == comp_number:
        print("Congrats! You guessed my number! It was indeed " + str(comp_number))
        print("You got it in only " + str(guesses) + " guesses")
        break

    else:
        print("please try again")


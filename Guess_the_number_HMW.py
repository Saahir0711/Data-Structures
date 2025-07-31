import random

num_list = [1,8,34,96,78,63,81,12,22,44]
print ("The list of numbers is", num_list)
sec_num = num_list[random.randint(0,10)]

guess = int(input("Guess the number: "))
num_guesses = 1

while guess != sec_num:
    num_guesses = num_guesses + 1 
    if guess > sec_num:
        guess = int(input("Incorrect, the number is smaller please guess again: "))
    if guess < sec_num:
        guess = int(input("Incorrect, the number is bigger please guess again: "))
   

print ("Congratulations, you answered correctly in ", num_guesses, "guesses!")
    
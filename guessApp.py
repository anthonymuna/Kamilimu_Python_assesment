print("-"*50)
print(" "*10+"GUESS THE NUMBER APP"+" "*10)
print("-"*50)

import random

guess = 0
secretNumber = random.randint(1,100)
print("Guess of a number")
for guess in range(1,99):
	guess = int(input("Make a guess: "))
	
	if guess < secretNumber:
		print("Sorry your guess %s is too low" %guess)
	elif guess > secretNumber:
		print("Sorry your guess %s is too high" %guess)
	else:
		break
if guess == secretNumber:
	print("Yes! You've got it. The number was %s" %secretNumber)
else:
	break

#!/usr/bin/env python

from random import randint

number = randint(1,10)

c = 1

guess = int(raw_input("Guess a number between 1 and 10: "))
if guess==number:
	print "Congratulations, you got it!"
else:
	while guess!=number:
		c+=1
		guess = int(raw_input("Wrong choice! This is your attempt number %d, try another number between 1 and 10: " %c))

print "Great, you finally got it after %d attempts!"%c
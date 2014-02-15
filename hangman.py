#!/usr/bin/env python

import random

list_of_words = "avere fatto right phone book bottle ball paper neumann wallet picture never earbuds".upper()
word = list(random.choice(list_of_words.split()))
empty = list("_"*len(word))
guessed_letters = []

print "= "*50
print "Welcome to hangman, you have seven chances to get the mystery word."
print "You have %d attempts to get the right word" %(len(word)+3)
print " ".join(empty)

count = 1

while count<=(len(word)+3):
	letter = raw_input("\n Pick a letter ---> ").upper()
	guessed_letters.append(letter)
	print " "
	if letter in word:
		print "Good choice!"
		print "Guessed Letters: "+" ".join(guessed_letters)
		positions = [i for i,x in enumerate(word) if x == letter]
		for i in positions:
			empty[i] = letter
		print " ".join(empty)+"\n"
	else:
		print "Bad choice!"
		print "Guessed Letters: "+" ".join(guessed_letters)
		print " ".join(empty)+"\n"
	if "_" not in empty:
		print "Congratulations, you won!"
		break
	elif count==(len(word)+3) and "_" in empty:
		print "Too late, you did not get the right word!"
		print "the word was "+"".join(word)
	else:
		print "Now guess the next letter"

	count+=1
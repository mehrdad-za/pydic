import scrabble
import string

for word in scrabble.wordlist:
	if "uu" in word:
		print(word)

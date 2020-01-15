# Hang man
import re
word = input("Enter a phrase: ")
dashes = "-" * len(word)
lol = list(dashes)
done = False
hangman = 0

while not done:
    print()
    print("guess this word/phrase?: ")
    print(' '.join(lol))
    letter = str(input("Enter a letter or the answer(s) :"))
    if letter in word:
        get_position = word.index(letter)
        lol[get_position] = letter
    elif letter != word:
        print("That letter is not in the word, try again!")
        hangman+=1
    else:
        print("sorry that is not an option")

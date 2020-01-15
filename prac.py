# Hang man, add spaces, and pics

word = input("Enter a phrase: ")
dashes = "-" * len(word)
lol = list(dashes)
done = False
hangman = 0
wronglist = [""]

while not done:
    print()
    print("guess this word/phrase?: ")
    print(' '.join(lol))
    print()
    print("Your guesses : ", ','.join(wronglist))
    letter = str(input("Enter a letter or the answer(s) : "))
    if letter in word:
        get_position = word.index(letter)
        lol[get_position] = letter
    elif letter != word:
        print(letter, "is not in the word, try again!")
        hangman+=1
        wronglist.append(letter)
    else:
        print("sorry that is not an option")


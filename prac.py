# Hang man, add spaces, and pics
word = input("Enter a phrase: ")
dashes = "-" * len(word)
lol = list(dashes)
done = False
hangman = 0
wl = [""]

while not done:
    print()
    print("guess this word/phrase?: ")
    print(' '.join(lol))
    print()
    print("Your guesses : ", ','.join(wl))
    letter = str(input("Enter a letter or the phrase(s) : "))
    if letter in word:
        get_position = word.index(letter)
        lol[get_position] = letter
    elif letter != word:
        print(letter, "is not in the word, try again!")
        hangman+=1
        wl.append(letter)
    else:
        print("sorry that is not an option")
    if letter == word:
        print("You Win!!!!")
        break
    if hangman == 1:
        print("you got a head!")
    elif hangman == 2:
        print("")
    elif hangman == 3:
        print("")
    elif hangman == 4:
        print("")
    elif hangman == 5:
        print("")
    elif hangman == 6:
        print("")

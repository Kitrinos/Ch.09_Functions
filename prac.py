# Hang man, add spaces, and pics

           #failed

word = input("Enter a phrase: ")
word2 = word
dashes = "-" * len(word)
lol = list(dashes)
done = False
hangman = 0
wl = [""]
for i in word:
    if i == " ":
        pos = word.index(" ")
        lol[pos] = " "
        continue
    else:
        word += "-"

# print(30 * "\n")
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
        continue
    elif letter != word:
        print(letter, "is not in the word, try again!")
        hangman+=1
        wl.append(letter)
        continue
    elif letter == word2:
        print("You win!!!")
        break
    else:
        print("sorry that is not an option")
        continue



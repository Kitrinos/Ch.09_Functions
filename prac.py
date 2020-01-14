#Hang man

word = input("Enter a phrase: ")
dashes = "-" * len(word)
lol = list(dashes)
done = False

while not done:
    print()
    print("guess this word/phrase?:", dashes)
    letter = str(input("Enter a letter or the answer(s) :"))
    if letter in word:
        get_position = word.index(letter)
        # print(get_position)
        dashes = lol[get_position] = letter


                    # m = ["a", "b"]
                    # n = str(input("asdf: "))
                    # m[0] = n
                    # print(m)
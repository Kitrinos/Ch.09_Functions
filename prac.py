#Hang man

word = input("Enter a phrase: ")
dashes = "-" * len(word)
lol = list(dashes)
done = False

while not done:
    print()
    print("guess this word/phrase?:", lol)
    letter = str(input("Enter a letter or the answer(s) :"))
    if letter in word:
        get_position = word.index(letter)
        # print(get_position)
        lol[get_position] = letter


# word = input(" word: ")
# dashes = "-" * len(word)
# lol = list(dashes)
# print("guess:", dashes)
# letter = str(input("asdf: "))
# if letter in word:
#     get_position = word.index(letter)
#     lol[get_position] = letter
#     print(lol)
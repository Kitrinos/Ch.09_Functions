#Hang man

# word = input("Enter a phrase: ")
# dashes = "-" * len(word)
# lol = list(dashes)
# done = False
#
# while not done:
#     print()
#     print("guess this word/phrase?:", dashes)
#     letter = str(input("Enter a letter or the answer(s) :"))
#     if letter in word:
#         get_position = word.index(letter)
#         # print(get_position)
#         dashes = lol[get_position] = letter
#

word = input(" word: ")
lol = list(word)
letter = str(input("asdf: "))
if letter in word:
    get_position = word.index(letter)
    word = lol[get_position] = letter + word
    print(word)
#Hang man
# an = input("Enter a phrase: ")
# # print(30 * "\n")
# win = False
#
# while win == False:
#     print()
#     dashes = "-" * len(an)
#     print("guess this word/phrase?:", dashes)
#     # pg = ("previous guesses: " )
#     li = input("Enter a letter or the answer(s) : ")
#     if li in an:
#         get_position = an.index(li)
#         print(get_position)
#         # dashes = print(dashes.replace(an, get_position ))
#
#     else:
#         print("That is not in the secret phrase try again!")


word = input("Enter a phrase: ")
win = False
dashes = "-" * len(word)
lol = list(dashes)

while win == False:
    print()
    print("guess this word/phrase?:", dashes)
    letter = str(input("Enter a letter or the answer(s) :"))
    if letter in word:
        get_position = word.index(letter)
        print(get_position)
        lol[0] = letter
        # print("You guessed correctly")
        # dashes = (dashes.replace("dashes", "letter"))

                    # string = "geeks for geeks geeks geeks geeks"

                    # print(string.replace("geeks", "Geeks"))

                    # m = ["a", "b"]
                    # n = str(input("asdf: "))
                    # m[0] = n
                    # print(m)



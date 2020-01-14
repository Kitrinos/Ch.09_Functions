#Hang man
an = input("Enter a phrase: ")
# print(30 * "\n")
win = False

while win == False:
    print()
    dashes = "-" * len(an)
    print("guess this word/phrase?:", dashes)
    # pg = ("previous guesses: " )
    li = input("Enter a letter or the answer(s) : ")
    if li in an:
        get_position = an.index(li)
        print(get_position)
        # dashes = print(dashes.replace(an, get_position ))

    else:
        print("That is not in the secret phrase try again!")

# # def update_dashes(an):
# for i in range(len(an)):
#     if an[i] == li:
#         li.index
#     else:
#         print("no")



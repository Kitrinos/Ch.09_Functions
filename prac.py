#Hang man
an = input("Enter a phrase: ")
# print(30 * "\n")
win = False

while win == False:
    print("guess this word/phrase?:")
    dashes = "-" * len(an)
    print(dashes)
    # pg = ("previous guesses: " )
    li = input("Enter a letter or the answer(s) : ")
    if li in an:
        print("you guessed correctly")
    else:
        print("That is not in the secret phrase try again!")

    def update_dashes(an):
        for i in range(len(an)):
            if an[i] == li:
                result = result + li
            else:
                print("no")

        return result



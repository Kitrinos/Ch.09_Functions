#Hang man

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y"]
win = False

an = input("Enter a phrase: ")
al = len(an)
# print(30 * "\n")

print("Welcome to Hangman!")

print("  ______\n |       |\n |\n |\n |\n_|_")

print("guess this word/phrase?:", al * "-")


pg = ("previous guesses: " )
input("Enter a letter or the answers")

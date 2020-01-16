def add_parts(x):
   if x == 0:
       print("   ____   \n  |        |\n  |             \n  |            \n  |                \n_|_                ")
       print()
   if x == 1:
       print("   ____   \n  |        |\n  |        0     \n  |            \n  |                \n_|_                ")
       print()
   if x == 2:
       print("   ____   \n  |        |\n  |        0     \n  |        |    \n  |                \n_|_                ")
       print()
   if x == 3:
       print("   ____   \n  |        |\n  |        0     \n  |       -|    \n  |                \n_|_                ")
       print()
   if x == 3:
       print("   ____   \n  |        |\n  |        0     \n  |       -|-   \n  |                \n_|_                ")
       print()
   if x == 4:
       print("   ____   \n  |        |\n  |        0     \n  |       -|-   \n  |       /        \n_|_                ")
       print()
   if x == 5:
       print("   ____   \n  |        |\n  |        0     \n  |       -|-   \n  |       /\        \n_|_                ")
       print()
   if x == 6:
       print("   ____   \n  |        |\n  |        0     \n  |       -|-   \n  |     _/\        \n_|_                ")
       print()
   if x == 7:
       print( "   ____   \n  |        |\n  |        0     \n  |       -|-   \n  |     _/\_        \n_|_                ")
       print()
# Hang man, add spaces, and pics
word = input("Enter a phrase: ")
for i in range(50):
   print()
done = False
hangman = 0
wl = []
secret_word = ""
swl = []
for i in word:
   if i != " ":
       secret_word += "-"
       swl.append("-")
   else:
       secret_word += " "
       swl.append(" ")
while not done:
   add_parts(hangman)
   print()
   print("Guess this word/phrase?: ")
   print(secret_word)
   # print(wl)
   print("Your guesses : ", ','.join(wl))
   letter = str(input("Enter a letter or the phrase(s) : "))
   if letter in word:
       pok = 0
       for i in word:
           if i == letter:
               swl[pok] = letter
           pok+=1
       secret_word = ("".join(swl))
   elif letter != word:
       print(letter, "is not in the word, try again!")
       hangman+=1
       wl.append(letter)
   else:
       print("Sorry, that is not an option.")
   if letter.lower() == word.lower():
       print("You Win!!!!")
       break
   elif hangman == 7:
       print("You Lose!!!!")
       break

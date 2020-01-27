#Sign your name:________________

'''
1.) Correct the following code: (The user's number should be increased by 1 and printed.)
'''
# def increase(x):
#     '''This will take your number, and increase it by 1'''
#     return x + 1
# x = int(input("Enter a number: "))
# n = increase(x)
# print("Your number has been increased to", n)

'''
2.) Correct the following code to print 1-10:
'''
# def count_to_ten():
#     '''This will print numbers 1-10'''
#     for i in range(1,11):
#         print(i)
#
# count_to_ten()

'''
3.) Correct the following code to sum the list:
'''
# def sum_list(list):
#     '''This code will take the following list and sum it'''
#     sum = 0
#     for i in list:
#         sum+= i
#     return sum
#
# list = [45, 2, 10, -5, 100]
# n = sum_list(list)
# print(n)

'''
4.) Correct the following code which should reverse the sentence that is entered.
'''


def reverse(text):
    '''This will take your text(text) and reverse the text'''
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[text_length - 1]
        text_length -=1
    return result
text = input("Enter a sentence: ")
n = reverse(text)
print(n)


'''
5.) Correct the following code: (if one of the options is not entered it should print the statements
'''

# def get_user_choice():
#     '''You can chose your choices'''
#     while True:
#         command = input("Command: ")
#         if command.lower() == "f":
#             print("f - Full speed ahead")
#         elif command.lower() == "m":
#             print("m - Moderate speed")
#         elif command.lower() == "s":
#             print("s - Status")
#         elif command.lower() == "d":
#             print("d - Drink")
#         elif command.lower() == "q":
#             print("q - Quit")
#         else:
#             print("Hey, that's not a command. Here are your options:" )
#
#         return command
#         break
#
#
# user_command = get_user_choice()
# print("You entered:", user_command)


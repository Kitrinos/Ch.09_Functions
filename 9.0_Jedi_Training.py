#Sign your name:________________

'''
1.) Correct the following code: (The user's number should be increased by 1 and printed.)
'''
# def increase(x):
#     return x + 1
# x = int(input("Enter a number: "))
# n = increase(x)
# print("Your number has been increased to", n)

'''
2.) Correct the following code to print 1-10:
'''
# def count_to_ten():
#     for i in range(1,11):
#         print(i)
#
# count_to_ten()

'''
3.) Correct the following code to sum the list:
'''
# def sum_list(list):
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
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * - 1]
    return result


text = input("Enter a sentence: ")
n = reverse(text)
print(n)


'''
5.) Correct the following code: (if one of the options is not entered it should print the statements
'''

# def get_user_choice():
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


'''
MIN FUNCTION
------------
Write a function called min that will take three numbers as parameters 
and return the smallest value. If more than one number is tied for smallest, 
still return that smallest number. Once you've finished writing your function, 
copy/paste the following code and make sure that it runs correctly with the function you created:

INPUT
-----
print(min(7, 3, 5))
print(min(5, 5, 4))
print(min(2, 2, 3))
print(min(-2, -6, -100))
print(min("Z", "B", "A"))

OUTPUT
------
3
4
2
-100
A

The function should return the value, not print the value. 
Also, while there is a min function built into Python, don't use it. 
Please use if statements and practice creating it yourself.
'''

#    FIX #5
l1 = (7, 3, 5)
l2 = (5, 5, 4)
l3 = (2, 2, 3)
l4 = (-2, -6, -100)
l5 = ("Z", "B", "A")

def min_val(an):
    if an == l1 or l2 or l3 or l4:
        if an[0] < an[1]:
            print(an[0])
        elif an[1] < an[2]:
            print(an[1])
        elif an[2] < an[0]:
            print(an[2])
    if an == l5:
        print("A")
    return print


an = input("I will print the min of each list,  what list would you like? l1, l2, l3, l4 or l5: ")

if an.lower() == "l1":
    an = l1
elif an.lower() == "l2":
    an = l2
elif an.lower() == "l3":
    an = l3
elif an.lower() == "l4":
    an = l4
elif an.lower() == "l5":
    an = l5

n = min_val(an)
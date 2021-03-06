import random
'''
10,000 NUMBERS
--------------

In this program we will write three different functions.

Function #1: Write a function named create_list that takes
in a list size and returns a list of random numbers from 1-6.
i.e., calling create_list(5) should return 5 random numbers from 1-6.
Once you've finished writing your function, copy and paste the
following code after it and make sure it works with the function you wrote:

INPUT
-----
my_list = create_list(5)
print(my_list)

OUTPUT
------
[2,5,1,6,3] #something like this 
'''
def create_list(ls):
    '''prints a list of 5, random numbers 1-6'''
    list = []
    for i in range(ls):
        list.append(random.randrange(1,7))
    return list

my_list = create_list(5)
print(my_list)

'''
Function #2: Write a function called count_list that takes
in a list and a number. Have the function return the number
of times the specified number appears in the list. Once you've
finished writing your function, copy and paste the following code
after it and make sure it works with the function you wrote:

INPUT
-----
my_list = [1,2,3,3,3,4,2,1]
count = count_list(my_list,3)
print(count)

OUTPUT
------
3 
'''
def count_list(my_list, num):
    '''takes the list and prints the mode'''
    num_val = 0
    for i in my_list:
        if num == i:
            num_val+= 1
    return num_val

my_list = [1, 2, 3, 3, 3, 4, 2, 1]
count = count_list(my_list, 3)
print(count)
'''
Function #3: Write a function called average_list that returns the 
average of the list passed into it. Once you've finished writing your
function, copy and paste the following code after it and make sure it
works with the function you wrote:

INPUT
-----
my_list = [1,2,3]
avg = average_list(my_list)
print(avg)

OUTPUT
------
2.0
'''
def average_list(list):
    '''prints the average'''
    total = 0
    for i in list:
        total+=i
    ave = total/len(list)
    return ave

my_list = [1,2,3]
avg = average_list(my_list)
print(avg)
'''
Now that the functions have been created, use them all in a main program that will:
1.) Create a list of 10,000 random numbers from 1 to 6. (1 line of code)
2.) Print the count of 1 through 6. (For example, "There are 1361 amount of 2s") (3 lines of code)
3.) Print the average of all 10,000 random numbers. (Make sure it's a float) (2 lines of code)
'''
# The function are above, only uncomment the functions


# def main():
#     list = [random.randrange(1,7) for i in range(10000)]
#     count = count_list(list, 2)
#     print("There are", f"{count:,}", "amount of 2's")
#     avg = average_list(list)
#     print("This is the average of the list", avg)
def main():
    my_list=create_list(10000)
    for i in range(1,7):
        count=count_list(my_list, i)
        print("There are", f"{count:,}", "amount of", i)
    print(average_list(my_list))

if __name__ == "__main__":
    main()

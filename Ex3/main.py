 

def is_valid_input(data): # we defind this function to validate our data
    if not data.isdigit():
        print("Error: expecting a positive integer!")
        return False
    number = int(data)
    if number <= 0:
        print("Error: expecting a positive integer!")
        return False
    return True


def is_divisable(a, b):
    """return true if b is divisable by a"""
    if(a == b):
        return False # we don't need duplicates in this exersize
    ftemp = b / a # float 
    itemp = b // a # int
    return itemp == ftemp ## this will be true only of ftemp has .0 to it

    


# get user data and validate
user_first = input("Enter the first number: ")

if not is_valid_input(user_first):
    exit(0)

user_second = input("Enter the second number: ")


if not is_valid_input(user_second):
    exit(0)

user_third = input("Enter the third number: ")

if not is_valid_input(user_third):
    exit(0)


# data prosses 

# convert string data to int data so we can use math!
a = int(user_first)
b = int(user_second)
c = int(user_third)


# using math!
sum = a + b + c 
mean = sum/3

# using lists to work out the order by value of the data
og_list = [a, b, c]
mylist = [a, b, c]
mylist.sort() # sort the list from small to large
max = mylist[-1] # the largest number will be in the end of the list

# string formating -> injecting values to a given string
print(f"The sum is: {sum}")
print(f"The mean is: {mean}")
print(f"{max} is the maximum")

print("Sorted numbers:", end=" ")
# list unpacking -> treat the list as indevidial elements 
print(*mylist, sep=", ")


# going in a for loop over the numbers and printing witch is even and witch is odd using the mudolos operator
for i in og_list:
    if i % 2 == 0: # even number
        print(i, "is even")
    else: # odd  number
        print(i, "is odd")



for i in og_list:
    for j in og_list:
        if is_divisable(i, j):
            print(i, "divides", j)














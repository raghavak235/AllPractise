# https://www.geeksforgeeks.org/tag/python-lambda/?type=popular

# There are 3 functions which do different works: map, filter, reduce around lambda
# The map() function is typically used when you need to apply a function to each element of an iterable (like a list) individually. In this case, you only have a single string, str1, rather than a list of strings.
# map:The map() function applies a given function to all items in an input list (or any iterable) and returns a map object (which is an iterator).
# The basic syntax is map(function, iterable).
# Since map() returns an iterator (which is lazy and doesn't store all its results in memory), wrapping it with list() will convert the map object into a list of the results.
# Filter will give you the filtered result


# Given a list, the task is to write a Python program to check if the value exists in the list or not using the lambda function.

def lambda_list(l, v):
    x = lambda l,v: True if v in l else False
    output = x(l,v)
    print(output)

# lambda_list(l=[1, 2, 3, 4, 5], v=4)

# When x is positive, raising x to the power of 1/3 (x ** (1/3)) gives the cube root of x.
def cube_root(x):
    cube_root = lambda x: x **(1/3)
    print(cube_root(x))
# cube_root(x=27)


# The map() function applies a given function to all items in an input list (or any iterable) and returns a map object (which is an iterator).
# The basic syntax is map(function, iterable).
# Since map() returns an iterator (which is lazy and doesn't store all its results in memory), wrapping it with list() will convert the map object into a list of the results.
def square_nums(l):
    sq_nums = list(map(lambda y: y**2, l))
    # or
    # lst = list(map(lambda x: x ** 2, range(1, 5)))
    print(sq_nums)
# square_nums(l=[4, 2, 13, 21, 5])


def odd_nums():
    l = [1,2,3,4,5]
    result = list(filter(lambda x: x%2 !=0,l))
    print(result)
# odd_nums()


def count_even():
    l=[1,2,3,4,5]
    result = len(list(filter(lambda x: x%2==0,l)))
    print(result)
# count_even()

# Given two arrays, find their intersection. Examples:
#
# Input:  arr1[] = [1, 3, 4, 5, 7]
#         arr2[] = [2, 3, 5, 6]
# Output: Intersection : [3, 5]

def intersection_arr():
    l1=[1, 3, 4, 5, 7]
    l2=[2, 3, 5, 6]
    result=list(filter(lambda x: x in l2,l1))
    print(result)
# intersection_arr()


def sorting_with_lambda():
    list = [{"name": "Nandini", "age": 20},
            {"name": "Manjeet", "age": 20},
            {"name": "Nikhil", "age": 19}]

    # using sorted and lambda to print list sorted
    # by age
    print("The list printed sorting by age: ")
    print(sorted(list, key=lambda i: i['age']))

# lambda function to find the maximum among three numbers in Python.

def lambda_max():
    a=10
    b=11
    c=12
    result=lambda a,b,c: max(a,b,c)


# how to find the smaller value between two elements using the Lambda function.

def small_num():
    a=11;b=12
    result= lambda a,b: a if a<b else b

# Given an array of positive and negative numbers, arrange them such that all negative integers appear before all the positive integers in the array

def lambda_pos_neg():
    arr= [12, 11, -13, -5, 6, -7, 5, -3, -6]
    result = list(filter(lambda x: x<0, arr)) + list(filter(lambda x: x >0, arr))
    # or
    # Sample list of mixed positive and negative numbers
    numbers = [3, -1, -4, 2, -7, 5, -6]
    # By default, sorted() arranges the elements in ascending order. Here, it will place all elements that return
    # False (negative numbers) before those that return True (non-negative numbers).
    # Lambda expression to rearrange positive and negative numbers
    rearranged = sorted(numbers, key=lambda x: x >= 0)

    print(rearranged)


 # how to find the max value between two elements using the Lambda function.
def max_lambda():
    val= lambda x,y: max(x,y)


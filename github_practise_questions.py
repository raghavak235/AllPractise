# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# https://github.com/Tanu-N-Prabhu/Python/blob/master/Python%20Coding%20Interview%20Prep/Python%20Coding%20Interview%20Questions%20(Beginner%20to%20Advanced).md

# Level 1
import math
import re

from distlib.compat import raw_input


# Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

def duv_by_7():
    # for divisible word use %, for multiples use /
    l=[]
    for n in range(2000, 3201):
        if n%7==0 and n/5!=0:
            l.append(str(n))
            pass
    print(','.join(l))


# Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

# factorial seven is written 7!, meaning 1 × 2 × 3 × 4 × 5 × 6 × 7. Factorial zero is defined as equal to 1.

def factorial(f):
    if f == 0:
        return 1
    return f * factorial(f-1)

# Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def generate_dict(d):
    gd={}
    for n in range(1, d+1):
        gd[n]=n*n
    print(gd)

# Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
def gen_list_tuple(nums):
    lst = nums.split(',')
    print(lst)
    print(tuple(lst))


# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
class getandprint:
    def __init__(self):
        self.getvalue = None
        pass
    def getString(self):
        self.getvalue = input()
    def printString(self):
        print(self.getvalue.upper())


# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

def calc(c= 50, h =30):
    output=[]
    d = input('enter the input sequence')
    items= [num for num in d.split(',')]
    for i in items:
         output.append(str(round(math.sqrt(2 * c * float(i)/h))))
    print(','.join(output))

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
def matrix_creation():
    rows = 2
    columns = 2
    matrix = []
    for m in range(rows):
        l=[]
        for n in range(columns):
            element = int(input('Enter elements'))
            l.append(element)
            print("l", l)
        matrix.append(l)
        print(matrix)


# Question:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sort_words():
    words = input("enter words")
    list_of_words = words.split(',')
    list_of_words.sort()
    return ','.join(list_of_words)

# Question
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

def word_capitalize():
    words = input('enter words')
    return words.upper()

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def remove_duplicates():
    words = input('enter words')
    l = words.split(' ')
    print(l)
    s = list(set(l))
    print((sorted(s)))
    return ' '.join(sorted(s))

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

def div_5():
    numbers = input("Enter digits")
    # CONVERTING BINARY TO INTEGER 1
    # To convert binary number into Decimal, we have to use the python built-in int function, which takes the binary number and the base of number system as an argument.
    # Syntax: int(string, base) int(i,2)

    int_num = [i for i in numbers.split(',')]
    output_nums = []
    for n in int_num:
        if int(n,2)%5 == 0:
            output_nums.append(str(n))
    print(','.join(output_nums))

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# To retrieve each digit of a number in Python, you can convert the number to a string and then iterate over each character of the string. Here's how you can do it:
# Method 1: Using string manipulation
# number = 12345
# digits = [int(digit) for digit in str(number)]
# print(digits)  # Output: [1, 2, 3, 4, 5]
#
# # Method 2: Using arithmetic operations
# number = 12345
# digits = []
# while number > 0:
#     digit = number % 10
#     digits.insert(0, digit)  # Insert at the beginning of the list to maintain order
#     number //= 10
# print(digits)  # Output: [1, 2, 3, 4, 5]


def each_digit_is_even():
    values = []
    for e in range(1000, 1000+3):
        digits = [int(i) for i in str(e)]
        print(digits)
        for d in digits:
            if d%2==0:
                values.append(d)
    print(values)

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123

def count_cases():
    d={"UPPER CASE":0, "LOWER CASE":0}
    sen=input("Enter something: ")

    for s in sen:
        # print('s', s)
        if s.isupper():
            print('up',s)
            d["UPPER CASE"] += 1

        elif s.islower():
            print('lp', s)
            d["LOWER CASE"]+=1
        else:
            pass
            print('no condition')
    print("UPPER CASE", d["UPPER CASE"])
    print("LOWER CASE", d["LOWER CASE"])
# count_cases()

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# digits should measure with isalpha()
# isalpha()
def digits_count():
    s = input()
    d={"DIGITS":0, "LETTERS":0}
    for c in s:
        if c.isdigit():
            d["DIGITS"]+=1
        elif c.isalpha():
            d["LETTERS"]+=1
        else:
            pass
    print ("LETTERS", d["LETTERS"])
    print ("DIGITS", d["DIGITS"])

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# We need to evaluate the expression a + aa + aaa + aaaa. Each term of this expression is formed by repeating the digit a a certain number of times:
#
# a: Appears once.
# aa: Appears twice.
# aaa: Appears three times.
# aaaa: Appears four times.
def compute_value(a):
    # Construct each term
    term1 = int(a)
    term2 = int(a * 2)
    term3 = int(a * 3)
    term4 = int(a * 4)

    # Sum the terms
    total = term1 + term2 + term3 + term4
    return total



# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

def bank_account():
    netAmount = 0
    while True:
        s = input()
        if not s:
            break
        values = s.split(" ")
        operation = values[0]
        amount = int(values[1])
        if operation == "D":
            netAmount += amount
        elif operation == "W":
            netAmount -= amount
        else:
            pass
    print(netAmount)

# Question:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
def pass_criteria():
    input_str = input("")
    if input_str:
        items = input_str.split(",")
        for password in items:
            if len(password) < 6 or len(password) > 12:
                return False

            if not re.search("[a-z]", password):
                return False

            if not re.search("[A-Z]", password):
                return False

            if not re.search("[0-9]", password):
                return False

            if not re.search("[$#@]", password):
                return False

            return password
            pass


# Question:
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# itemgetter is a function from the operator module in Python. It is used to retrieve items or fields from an object such as a list, tuple, or dictionary.
# In the context of sorting, itemgetter can be used as a key function to specify which item(s) should be used for sorting. When sorting a list of tuples, for example, you can pass itemgetter the index of the item you want to sort by. It will then return a callable object that can be used as the key parameter for sorting functions like sorted() or list.sort().
# you can achieve the same result using lambda functions instead of itemgetter. Here's how you can modify the sorting function to use lambda functions:\
# sorted(tuples, key=lambda x: (x[0], x[1], x[2]))
# In this version, lambda x: (x[0], x[1], x[2]) creates an anonymous function that takes a tuple x as input and returns a tuple containing the elements at indices 0, 1, and 2 of x. This effectively replicates the behavior of itemgetter(0, 1, 2).


def input_sorted():
    l = []
    while True:
        input_txt= input("Enter name, age, and score separated by space: ")
        if not input_txt:
            break
        l.append(tuple(input_txt.split(',')))

        print(l)
    print(sorted(l, key=lambda x:(x[0], x[1], x[2])))
# input_sorted()


# Question:
# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

def generate_numbers(n):
    for i in range(n):
        if i % 7 == 0:
            yield i

# for j in generate_numbers(10):
#     print(j)


# Question
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

# In a typical Cartesian coordinate system:
# Moving up along the y-axis means increasing the y-coordinate.
# Moving down along the y-axis means decreasing the y-coordinate.
# Moving left along the x-axis means decreasing the x-coordinate.
# Moving right along the x-axis means increasing the x-coordinate.
# After processing all movements, it calculates the distance from the original point using the Pythagorean theorem:
# math.sqrt(x ** 2 + y ** 2)

def robot_moves():
    position =[0,0]
    while True:
        s = input()
        if not s:
            break
        moment = s.split(' ')
        direction = moment[0]
        distance = int(moment[1])
        if direction == 'UP':
            position[1] += distance
        elif direction == 'DOWN':
            position[1] -= distance
        elif direction == 'LEFT':
            position[0] -= distance
        elif direction == 'RIGHT':
            position[0] += distance
    # print(position)
    print(int(round(math.sqrt(position[0] ** 2 + position[1] ** 2))))

    pass


# Question:
# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

def alphanumeric_frequency_sort():
    frequency_word = input('Enter the words')
    output = {}
    for w in frequency_word.split(' '):
        # we need to also count the existing frequency count in output output.get(w,0) + 1
        output[w] = output.get(w,0) + 1
    print(output)

    words = output.keys()
    sort_words = sorted(words)
    print(sort_words)
    for s in sort_words:
        print("{}:{}".format(s, output.get(s)))

# alphanumeric_frequency_sort()]


# Question:
#     Write a method which can calculate square value of number
#
# Hints:
#     Using the ** operator
def square(a):
    return  a ** 2


# Question:
# Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.
#     Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
#     And add document for your own function

# The built-in document method is __doc__

def built_in_docs():
    print(abs.__doc__)
    print(int.__doc__)
    print(raw_input.__doc__)


# Question: Define a class, which have a class parameter and have a same instance parameter.

class Person:
    name = "Person"
    def __init__(self, name=None):
        self.name = name


# Question:
# Define a function which can compute the sum of two numbers.

def sum_nums(x,y):
    return x+ y

# Question:
# Define a function that can convert a integer into a string and print it in console.

def casting(a):
    str(a)


# Question:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

def given_tuple():
    t=(1,2,3,4,5,6,7,8,9,10)
    print(t[0:5])
    print(t[5:])


# Question:
# Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# string1 = "Hello"
# string2 = "123"
# string3 = "Hello123"
#
# print(string1.isalpha())  # Output: True
# print(string2.isalpha())  # Output: False
# print(string3.isalpha())  # Output: False

def is_string():
    t='123'
    if t.isalpha():
        print("YES")
    elif isinstance(t, str):
        print('YES')

# Question:
# Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

def filter_even():
    values=[1,2,3,4,5,6,7,8,9,10]
    even_values = filter(lambda x: x%2==0, values)


# Question:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

def map_list():
    l= [1,2,3,4,5,6,7,8,9,10]
    print(map(lambda x: x**2, l))

# Question:
# Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

def map_filter():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    map(lambda x: x**2, filter(lambda x: x%2==0,l))

# Question:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

def numbers():
    print(list(filter(lambda x: x%2==0, range(1,21))))

# Question:
# Define a class named American which has a static method called printNationality.

class American:
    @staticmethod
    def printNationality(country):
        return country

# Question:
# Define a class named American and its subclass NewYorker.

class American:
    pass
class NewYorker(American):
    pass

# Question:
# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width



# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    def __init__(self):
        pass
    def area(self):
        print("Area of shape is 0")
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length = length


    def area(self):
        return self.length * self.length



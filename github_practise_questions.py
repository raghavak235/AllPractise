# Level 1
import math


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


# https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar

# Python program to check whether the string is Symmetrical or Palindrome



# Given a string. the task is to check if the string is symmetrical and palindrome or not. A string is said to be
# symmetrical if both the halves of the string are the same and a string is said to be a palindrome string if one half
# of the string is the reverse of the other half or if a string appears the same when read forward or backward.
def string_palindrome(input_string):
    output_string = ''
    length = len(input_string)- 1
    for s in range(length,-1,-1):
        output_string += input_string[s]
    print(output_string==input_string)


# A string is said to be symmetrical if both the halves of the string are the same
# A string can only be symmetrical if its length n is even. This is because an odd-length string cannot be divided
# nto two equal halves. So we need to write if condition


def string_symmetrical(input_string):
    if len(input_string)% 2 != 0:
        print(False)
    else:
        first_half_len= int(len(input_string)/2)
        first_half = input_string[0:first_half_len]
        sec_half = input_string[first_half_len:]
        print(first_half==sec_half)

# Reverse Words in a Given String in Python
# REVERSED SHOULD BE APPLIED ON A LIST
# (reversed(str_list)


def string_reverse(input_string):
    output_str = ''
    input_string_len = len(input_string) -1
    for s in range(input_string_len, -1, -1):
        output_str += input_string[s]
    print(output_str)

    # OR

    str_list=input_string.split(' ')
    print(' '.join(reversed(str_list)))

# How to Remove Letters From a String in Python
def remove_letters_str(input_string, remove_letters):
    print(input_string.replace(remove_letters,''))


# Check if String Contains Substring in Python

def verifying_substring(input_string, sub_string):
    if sub_string in input_string:
        print('YES')
    else:
        print('NO')

# Words Frequency in String

def string_word_freq(input_string):
    dic_word_count ={}
    for s in input_string.split():
        if s not in dic_word_count:
            dic_word_count[s] = 1
        else:
            dic_word_count[s] += 1
    print(dic_word_count)

# Avoid Spaces in string length
# we check for each character to be equal not to space() using isspace()

# isspace()

def string_len_avoid_spaces(input_string):
    len_count=0
    for i in input_string:
        if not i.isspace():
            len_count += 1
    print(len_count)

    # OR
    print(sum([1 for i in input_string if not i.isspace()]))

# Python program to print even length words in a string

#  The task is to print all words with even length in the given string.

def string_even_length(input_string):
    for w  in input_string.split():
        if len(w)%2 == 0:
            print(w)


# Uppercase Half String
# Given a String, perform uppercase of the later part of the string.
def upper_case_half_string(input_string):
    half_str_length = len(input_string)//2
    print(half_str_length)
    print(input_string[0:half_str_length]+input_string[half_str_length:].upper())


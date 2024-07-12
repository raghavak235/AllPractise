# https://www.geeksforgeeks.org/python-string-exercise/
# https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar
import re


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

# Python program to capitalize the first and last character of each word in a string

# IF YOU WANT TO ACCESS THE STRING USING SLICING
# first char =i[0]
# middle char = i[1:-1] doesnt include last char
# last char = i[-1]
def first_last_char(input_string):
    for i in input_string.split():
        print(i[0].upper()+i[1:-1]+i[-1].upper())


# Python program to check if a string has at least one letter and one number
# Letters can be checked in Python String using the isalpha() method and
# numbers can be checked using the isdigit() method.
def check_string(input_string):
    output = []
    for i in input_string:
        if i.isdigit():
            output.append('digit')
        elif i.isalpha():
            output.append('char')

    if output.count('digit')  >= 1 and output.count('char') >= 1:
        print(True)
    else:
        print(False)


# ANOTHER LOGIC
    flag_1 = False
    flag_2 = False
    for i in input_string:
        if i.isdigit():
            flag_1 = True
        elif i.isalpha():
            flag_2 = True

    print(flag_1 and flag_2)

# Python Program to Accept the Strings Which Contains all Vowels

def string_vowels(input_string):
    input_string_low = input_string.lower()
    vowles_dict = {'a':0, 'e':0, 'i':0, 'o':0,'u':0}
    for v in vowles_dict:
        if v in input_string_low:
            vowles_dict[v] += 1

    print(vowles_dict)
    if not 0 in vowles_dict.values():
        print(True)
    else:
        print(False)

# Count the Number of matching characters in a pair of string
# (consider the single count for the character which have duplicates in the strings).

# Another logic, you can also take the string to covert to sets and remove duplicates/ unique

def count_chars(input_string1, input_string2):
    count_dict = []
    for c in input_string1:
        if c in input_string2 and c not in count_dict:
            count_dict.append(c)
    print(count_dict)

# ANOTHER LOGIC
    str1 = set(input_string1)
    str2 = set(input_string2)
    matching = str1.intersection(str2)
    print(matching)

# Python program to count number of vowels using sets in given string

# Example: Retrieving Values from a Set
# Initialize a set
# my_set = {1, 2, 3, 4, 5}
#
# # Iterate over the set to retrieve values
# for value in my_set:
#     print(value)


# In Python, the pop method for sets does not guarantee that it will return the last value added to the set.
# Instead, pop removes and returns an arbitrary element from the set. Since sets in Python are unordered collections,
# there is no concept of the "last" element in the way that there is with lists.
#
#
# # Initialize a set
# my_set = {1, 2, 3, 4, 5}
#
# # Retrieve and remove an arbitrary value from the set
# retrieved_value = my_set.pop()
# print(f"Retrieved value: {retrieved_value}")
# print(f"Set after pop: {my_set}")


def count_vowels(input_string):
    count = 0
    vowel = set('aeiou')
    print(vowel)
    for s in input_string:
        if s in vowel:
            count += 1

    print(count)

# Remove All Duplicates from a Given String in Python
# We are given a string and we need to remove all duplicates from it.
# What will be the output if the order of character matters?

def remove_duplicates(input_string):
    str_no_duplicates_no_order = ''.join(list(set(input_string)))
    # print(str_no_duplicates_no_order)
    new_str=''
    for i in input_string:
        if i not in  new_str:
            new_str += i
    print(new_str)

 # Least Frequent Character in String

def least_frequent_str(input_string):
    count_dic = {}
    for i in input_string:
        if i not in count_dic:
            count_dic[i]=1
        else:
            count_dic[i] += 1
    print(count_dic)
    min_value =  min(count_dic.values())
    for k,v in count_dic.items():
        if v == min_value:
            print(k)

# Maximum frequency character in String
# methods to find the frequency of maximum occurring character in a python string.


# The code max(all_freq, key=all_freq.get) finds the key with the maximum value in a Python dictionary all_freq.
#
# Here's a breakdown of how it works:
#
# all_freq: This represents a dictionary where keys are elements and values are their corresponding frequencies.
# .get(key, default): This is a method of dictionaries that retrieves the value for a given key.
# If the key doesn't exist, it returns a default value (usually None).
# In this case, .get is used without specifying a default value.
# key=all_freq.get: This part is passed as a keyword argument to the max function.
# It specifies a function for sorting the dictionary elements. Here,
# it uses the all_freq.get method to get the value (frequency) for each key in the dictionary.

def max_frequency_string(input_string):
    all_max = {}
    for i in input_string:
        if i not in all_max:
            all_max[i] = 1
        else:
            all_max[i] += 1

    max_values = max(all_max, key=all_max.get)
    print(max_values)

# Odd Frequency Characters
# we need to extract all the string characters which have odd number of occurrences.
def odd_frequency_chars(input_string):
    all_max = {}
    for i in input_string:
        if i not in all_max:
            all_max[i] = 1
        else:
            all_max[i] += 1

    for k,v in all_max.items():
        if v%2 !=0:
            print(k)

# Specific Characters Frequency in String List
# extract frequency of specific characters in the whole strings list.
def specific_character_frequency(input_string, specific_characters):
    chars_count={}
    for word in input_string:
        for c in word:
            if c in specific_characters and c not in chars_count:
                chars_count[c] = 1
            elif c in specific_characters and c in chars_count:
                chars_count[c] += 1
    print(chars_count)


# Frequency of numbers in String

def frequency_number_string(input_string):
    res = len(re.findall(r'\d+', input_string))
    print(res)

# Program to check if a string contains any special character

def special_char_string(input_string):
    regex = re.compile('[@_!#$%^&*()<>?/|}{~:]')
    if None == regex.search(input_string):
        print("String Accepted")
    else:
        print('String Not Accepted')

# Find words which are greater than given length k

def word_length(input_string, k):
    for w in input_string.split():
        if len(w) > k:
            print(w)

# Python program for removing i-th character from a string
def remove_ith_character(input_string,i):
    # ONE APPROACH USING POP
    #Input value  'Geek'
    a = list(input_string)
    # Output of a:['G', 'e', 'e', 'k']
    print(a)
    # You can provide any index number from POP
    a.pop(i)
    print(a)
    # ['G', 'e', 'k']

    print(''.join(a))
    new_str = ''
    print(input_string.split())

    # Another Approach

    for s in input_string.split():
        for ind, v in enumerate(s):
            # print(ind, v)
            if ind == i:
                pass
            else:
                new_str += v
    print(new_str)

    # Another Approach
    input_string =input_string[0:i]+input_string[i+1:]
    print(input_string)

 # Check if a given string is binary string or not


#A binary string is a string that only has two characters, usually the numbers 0 and 1, and it represents a series of binary digits.

def binary_string(input_string):


        # initialize the variable t
        # with '01' string
        t = '01'

        # initialize the variable count
        # with 0 value
        count = 0

        # looping through each character
        # of the string .
        for char in input_string:

            # check the character is present in
            # string t or not.
            # if this condition is true
            # assign 1 to the count variable
            # and break out of the for loop
            # otherwise pass
            if char not in t:
                count = 1
                break
            else:
                pass

        # after coming out of the loop
        # check value of count is non-zero or not
        # if the value is non-zero the en condition is true
        # and string is not accepted
        # otherwise string is accepted
        if count:
            print("No")
        else:
            print("Yes")


# Python program to find uncommon words from two Strings
# Given two sentences as strings A and B. The task is to return a list of all uncommon words.
# A word is uncommon if it appears exactly once in any one of the sentences, and does not appear in the other sentence.
# Note: A sentence is a string of space-separated words. Each word consists only of lowercase letters.


def uncommon_words(input_string1, input_string2):
    count_dict={}

    for i in input_string1.lower().split():
            # print(input_string1.split())
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
    print(count_dict)

    for j in input_string2.lower().split():
        # print(input_string2.split())
        if j not in count_dict:
            count_dict[j] = 1
        else:
            count_dict[j] += 1
    # print(count_dict)

    for k,v in count_dict.items():
        if v == 1:
            print(k)

# Check for URL in a String

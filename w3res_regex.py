# https://www.w3resource.com/python-exercises/re/
#
#
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
#
#
# #### Sample Regexs ####
#
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
import re

# Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9).

pattern=''
re.search()

# Matches a string that has an a followed by zero or more b's
def text_match(string):
    pattern = '^ab*$'
    re.search(pattern, string)

print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))



# Write a Python program that matches a string that has  a followed by one or more b's.

# The ? after + is added to make the quantifier non-greedy (lazy).
# Without the ?, the + would match as many 'b' characters as possible (greedy).
# With the ?, the +? matches the minimum number of 'b' characters needed to satisfy the pattern.
def text_match(string):
    pattern = 'ab+?'
    re.search(pattern, string)


print(text_match("ab"))
print(text_match("abc"))

# Matches a string that has a followed by zero or one 'b'

def text_match(string):
    pattern = 'ab?'
    re.search(pattern, string)
print(text_match("ab"))
print(text_match("abc"))
print(text_match("abbc"))
print(text_match("aabbc"))

# Write a Python program that matches a string that has an a followed by three 'b'.

def text_match(string):
    pattern = 'ab{3}'
    re.search(pattern, string)

print(text_match("abbb"))
print(text_match("aabbbbbc"))

# Write a Python program that matches a string that has an a followed by two to three 'b'.
def text_match(string):
    pattern = 'ab{2,3}'
    re.search(pattern, string)

print(text_match("ab"))
print(text_match("aabbbbbc"))


# Write a Python program to find sequences of lowercase letters joined by an underscore.

def text_match(string):
    pattern = '^[a-z]+_[a-z]+$'
    re.search(pattern, string)

print(text_match("aab_cbbbc"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

def text_match(string):
    pattern = '[A-Z]+[a-z]+$'
    re.search(pattern, string)

print(text_match("AaBbGg"))
print(text_match("Python"))
print(text_match("python"))
print(text_match("PYTHON"))
print(text_match("aA"))
print(text_match("Aa"))

# Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.

def text_match(string):
    pattern = 'a.*?b$'
    re.search(pattern, string)




# Write a Python program that matches a word at the beginning of a string.
def text_match(string):
    pattern = '^\w+'
    re.search(pattern, string)

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match(" The quick brown fox jumps over the lazy dog."))
# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.
#
# Solution:
# import re
# emailAddress = raw_input()
# pat2 = "(\w+)@((\w+\.)+(com))"
# r2 = re.match(pat2,emailAddress)
# print r2.group(1)
import re


def split_name_email():
    input_val=input('Enter value')
    print(input_val.split('@')[0])

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


# Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

# Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
#
# Example:
# If the following words is given as input to the program:
#
# 2 cats and 3 dogs.
#
# Then, the output of the program should be:
#
# ['2', '3']
# All Coding Questions related to lists
# https://www.geeksforgeeks.org/python-list-exercise/?ref=lbp
# https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/
# Python program to interchange first and last elements in a list

def interchange_ele_list():
    Input = [12, 35, 9, 56, 24]
    first = Input[0]
    last = Input[-1]
    Input[-1] = first
    Input[0] = last
    print(Input)

# Python Program to Swap Two Elements in a List
# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

def swap_elements_list(pos1, pos2):
    input_list = [1, 2, 3, 4, 5]
    ind1 = pos1-1
    ind2 = pos2-1
    first = input_list[ind1]
    sec = input_list[ind2]
    input_list.remove(first)
    input_list.remove(sec)
    input_list.insert(ind1, sec)
    input_list.insert(ind2, first)
    print(input_list)

# The better logic
# POP ALSO WORKS ON INDEX

    first_ele = input_list.pop(ind1)
    # THE REASON WHY WE ARS ADDING -1 in POP is once you have the POP operation on list, it removes existing element so
    # the length becomes less so -1
    sec_ele = input_list.pop(ind2-1)
    input_list.insert(ind1, sec_ele)
    input_list.insert(ind2, first_ele)
    print(input_list)

# Swap elements in String list

def swap_ele_list(list_str):
    list_str = [i.replace('G', '-').replace('e','G').replace('-','e') for i in list_str]
    print(list_str)

# Different ways to clear a list in Python

def clear_list(input_list):
    print(input_list.clear())

# Reversing a List in Python
def reverse_list(input_list):
    output_list = []
    for i in range(len(input_list)-1, -1, -1):
        output_list.append(input_list[i])
    print(output_list)

    # ALTERNATIVE LOGIC
    print(input_list[::-1])

# Count occurrences of an element in a list
def count_elements(input_list, x):
    from collections import Counter
    dict = Counter(input_list)
    print(dict, dict.get(x))


# sum and average of List in Python

def sum_avg_list(input_list):
    sum_va = sum(input_list)
    avg = sum_va/len(input_list)
    print(sum_va, avg)

# Multiply all numbers in the list
def multiply_List(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

 # program to find smallest number in a list
def smallest_number_list(input_list):
    smaller = input_list[0]
    for v  in input_list:
        if v < smaller:
            smaller = v
    print(smaller)

# Program to Find Largest Number in a List
def largest_number_list(input_list):
    large = input_list[0]
    for l in input_list:
        if l > large:
            large = l
    print(large)

# program to find second largest number in a list

def second_largest_number(input_list):
    first_large = input_list[0]
    sec_large = input_list[1]

### Programs on List of Strings

# Python program to find the character position of Kth word from a list of strings

# Given a list of strings. The task is to find the index of the character position for the word, which lies at the Kth index in the list of strings.
def kth_index():
    test_list = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
    k = 16
    count = 0  # Start count from 0

    for word in test_list:
        for i, char in enumerate(word):
            count += 1
            if count == k:
                print(f"The character at position {k} is '{char}' and it's the {i}th element of the word '{word}'")
                return i  # Returning the index within the word

    print("The list does not contain that many characters.")
    return -1  # Return -1 if k is out of bounds




 # Convert Character Matrix to single String

def conversion():
    t=[['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
    ''.join(c for r in t for c in t)


# Filter the List of String whose index in second List contains the given Substring
def filter_lists():
    l1= ['Gfg', 'is', 'not', 'best', 'and', 'not', 'for', 'CS']
    l2=  ['Its ok', 'all ok', 'wrong', 'looks ok', 'ok', 'wrong', 'ok', 'thats ok']
    res=[]
    sub_str='ok'
    # Use zip() to iterate through both lists at the same time and map elements with the same index together.
    # Check if the substring is in the second element (ele2) using the in operator.\
    # If the substring is present, append the corresponding element from test_list1 to res\

    for ele1, ele2 in zip(l1,l2):
        print(ele1, ele2)
        if sub_str in ele2:
                res.append(ele1)

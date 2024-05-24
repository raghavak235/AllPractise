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

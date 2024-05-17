# All Coding Questions related to lists
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


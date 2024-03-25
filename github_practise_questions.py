# Level 1


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

gen_list_tuple(nums='34,67,55,33,12,98')

# Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.
class getandprint:
    def __init__(self):
        self.getvalue = None
        pass
    def getString(self):
        self.getvalue = input()
    def printString(self):
        print(self.getvalue.upper())
        
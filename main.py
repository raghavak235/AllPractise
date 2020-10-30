from collections import defaultdict, OrderedDict, Counter 
from itertools import permutations 


def list_of_tuples(l):
    list_cubes = [(i, i**3) for i in l]
    print (list_cubes)
#list_of_tuples(l = [1, 2, 3])

def join_tuple(jt):
    mapp = defaultdict(list)
    print(mapp)
    for key, val in jt:
        #print('k',key,'m',val)
        mapp[key].append(val)
    print(mapp)
    res_new = [(key, *val) for key, val in mapp.items()]
    print(res_new)

    res = []
    for sub in jt:
        #print('sub',sub)
        if res and res[-1][0] == sub[0]:
            # print('if',res)
            # print('2 if',res[-1][0], sub[0] )
            res[-1].extend(sub[1:])
        else:
            res.append([ele for ele in sub])
            # print('else',res)

    res = list(map(tuple, res))
    print(res)
#join_tuple(jt= [(5, 6), (5, 7), (6, 8), (6, 10), (7, 13)])

def arguemnt_tuples(at1, at2):
  at_final = [(a,b) for a in at1 for b in at2]
  
  at_final= at_final + [(c,d) for c in at2 for d in at1]
  print(at_final)
  
#arguemnt_tuples(at1=(7, 2), at2=(7,8))

def remove_tuples_length(tl, k):
  new_list = [a for a in tl if len(a) !=2 ]
  print(new_list)
#remove_tuples_length(tl= [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], k=2)

def sort_tuples_second_value(st):
  st.sort(key = lambda x:x[1])
  print(st)
  d ={i[1]:i for i in st}
  print(d)
  sort_d = [d[j] for j in sorted(d)]
  print(sort_d)
#sort_tuples_second_value(st=[('for', 24), ('Geeks', 8), ('Geeks', 30)] )\

def nested_tuple(test_tuple, keys):
  d = [{'keys':b[0], 'value':b[1], 'id':b[2] } for b in test_tuple]
  print(d)
#nested_tuple(test_tuple=((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10)), keys = ['key', 'value', 'id'])

lis = [{ "name" : "Nandini", "age" : 20}, 
{ "name" : "Manjeet", "age" : 20 },
{ "name" : "Nikhil" , "age" : 19 }]
 
sorted(lis, key=lambda x:x['age'])

def flat_dict(d):
  pass
  for i, j in zip(d['name'], d['month']):
    print(i,j)

#flat_dict(d={'name': ['Jan', 'Feb', 'March'], 'month': [1, 2, 3]})

def ordered_dict(od, item_to_be_inserted):
# insertion of items in beginning of ordered dict 
# For Python 3.2 and later, you should use the move_to_end method. The method accepts a last argument which indicates whether the element will be moved to the bottom (last=True) or the top (last=False) of the OrderedDict.


  pass
  od.update(item_to_be_inserted) 
  print(od)
  od.move_to_end('manjeet', last = False)
  print(od)

#ordered_dict(od=OrderedDict([('akshat', '1'), ('nikhil', '2')]) ,item_to_be_inserted = {'manjeet':'3'}
 #)

 
def checkOrder(input, pattern): 
      
    # create empty OrderedDict 
    # output will be like {'a': None,'b': None, 'c': None} 
    dict = OrderedDict.fromkeys(input) 
    print(dict)
  
    # traverse generated OrderedDict parallel with 
    # pattern string to check if order of characters  
    # are same or not 
    ptrlen = 0 
    for key,value in dict.items(): 
        print('out', key)
        if (key == pattern[ptrlen]): 
            ptrlen = ptrlen + 1
            print(ptrlen, key)
          
        # check if we have traverse complete  
        # pattern string 
        if (ptrlen == (len(pattern))): 
            return 'true'
  
    # if we come out from for loop that means  
    # order was mismatched 
    return 'false'


#print(checkOrder(input='engineers rock' ,pattern= 'gsr'))

def winner_of_election(votes):
  # If there is tie, print a lexicographically smaller name.(sort it using ascending)
  pass
  max_votes = {}
  for i in votes:
    if i in max_votes:
      max_votes[i] += 1
    else:  
      max_votes[i] = 1

  print(max_votes)

  value = max(max_votes.values())
  
  winner = [a for a,b in max_votes.items() if b == value]
  print(winner[0])


# winner_of_election(votes =['john','johnny','jackie','johnny','john','jackie', 
#     'jamie','jamie','john','johnny','jamie','johnny','john']  
#   )

def dict_sort():
  pass
  key_value ={}     
  
# Initializing value  
  key_value[2] = 56       
  key_value[1] = 2 
  key_value[5] = 12 
  key_value[4] = 24
  key_value[6] = 18      
  key_value[3] = 323 
  print(key_value)

  # for i in sorted(key_value.keys()):
  #   print(i, key_value[i])

  print(sorted(key_value.items(), key = lambda x: x[1]))
    
#dict_sort()

def dict_multiple_inputs():

    dict = {} 
      
    # Insert first triplet in dictionary 
    x, y, z = 10, 20, 30
    dict[x, y, z] = x + y - z; 
      
    # Insert second triplet in dictionary 
    x, y, z = 5, 2, 4
    dict[x, y, z] = x + y - z; 
      
    # print the dictionary 
    print(dict)   

#dict_multiple_inputs()

def anagrams():
	#one more logic to be witten is number of characters should match 
	word = sorted('rac')
	alternatives = ['car', 'girl', 'tofu', 'rca']

	for alt in alternatives:
		if word == sorted(alt):
			print(word, sorted(alt), alt )
#anagrams()

def kth_non_repeating_word(strg, k):
	pass
	d = {}
	for i in strg:
		if i in d: d[i] +=  1
		else: d[i] = 1
	print(d)	
	non_rep = [i for i,j in d.items() if j == 1]
	print(non_rep[k-1])

#kth_non_repeating_word(strg = 'geeksforgeeks', k = 2)

def largest_anagram_size(input):
	pass
	l_input = input.split()
	#print(l_input)
	d_large={}
	for i in l_input:
		print(i, ''.join(sorted(i)) )
		if  ''.join(sorted(i)) in d_large:
			d_large[''.join(sorted(i))] += 1
		else:
			d_large[''.join(sorted(i))] = 1

	large_size=max(d_large.values())
	print(large_size)
		
#largest_anagram_size(input='cars bikes arcs steer ')

def duplicate_words(w):
	pass
	print(' '.join(set(w.split())))
#duplicate_words(w= 'Python is great and Java is also great')

def mirror_chars(s):
	pass


def rearranging_characters(s1,s2):
	pass
	c=0
	for i in s1:
		if i in s2:
			c +=1
	if len(s1) == c:
		print('Possible')
	else:
		print('Not Possible')


#rearranging_characters(s1='GeeksforGeeks',s2='rteksfoGrdsskGeggehes')

def count_frequencies(string):
	pass
	   # calculate frequency of each character 
    # and convert string into dictionary 
	dict=Counter(string) 
  
    # now get list of all values and push it 
    # in set 
	same = list(set(dict.values())) 
	print(same, len(same))

	if len(same)>2: 
		print('No') 
	elif len (same)==2 and same[1]-same[0]>1: 
		print('No') 
	else: 
		print('Yes') 

#count_frequencies(string = 'xyyzz')

def Possible_words(dicty, arr):
	pass
	for word in dicty:
		dict_word = Counter(word)
		#print(dict_word)
		flag = 1
		for key in dict_word.keys():
			if key not in arr:
				flag=0
		if flag == 1:
			print(word)


# Possible_words(dicty=["go","bat","me","eat","goal","boy", "run"],
# arr= ['e','o','b', 'a','m','g', 'l'])

def key_associated_with_values(test_dict):
	pass
	res = defaultdict(list)
	for key,value in test_dict.items():
		for ele in value:
			res[ele].append(key) 
	print(res)
#key_associated_with_values(test_dict = {'abc': [10, 30], 'bcd' : [30, 40, 10]})

def reverse_a_word(w):
	pass
	print(w.split(' '))
	list_words = w.split(' ')
	for i in range(len(list_words), 0, -1):
		print(list_words[i-1])

#reverse_a_word(w= "geeks quiz practice code")

def word_frequencty(wf):
	pass
	dict = Counter(wf.split(' '))
	print(dict)

#word_frequencty(wf ='Gfg is best . Geeks are good and Geeks like Gfg')

def uncommon_words(A,B):
	pass

	print(set(A.split(' ')).symmetric_difference(set(B.split(' '))))

#uncommon_words(A= "Geeks for Geeks" ,B="Learning from Geeks for Geeks")

def permutation_of_string(ps):
	pass
	pts = permutations(ps)
	
	for w in pts:
		print(''.join(list(w)))

#permutation_of_string(ps='ABC')

def remove_duplicate_occurances(rdo, repl_dict):
	pass
	count = set()
	test_split= rdo.split()
	for i, v in enumerate(test_split):
		if v in repl_dict:
			if v in count:
				test_split[i] = repl_dict[v]
			else:
				count.add(v)
	print(test_split)

			

# remove_duplicate_occurances(rdo= 'Gfg is best . Gfg also has Classes now. Classes help understand better', repl_dict = {'Gfg' :  'It', 'Classes' : 'They' } )

def replace_string_to_make_empty(str, sub_str):
	pass
	res = str.replace(sub_str,'')
	res = res.replace(sub_str,'')

#replace_string_to_make_empty( str = "GEEGEEKSKS", sub_str = "GEEKS")

def rotate_string(s, d):
	pass
	lr_f = s[:d]
	left_final= s[d:]+lr_f
	print(left_final)

	r_f = s[len(s)-d:]
	print(r_f)
	right_final = r_f + s[:len(s)-d] 
	print(right_final)
#rotate_string(s= "GeeksforGeeks", d=2)

def reverse_a_list(rl):
	rl.reverse()
	print(rl)

	for i in range(len(rl), 0, -1):
		print(rl[i-1])

#reverse_a_list(rl=[10, 11, 12, 13, 14, 15] )


def sort_one_list_using_other(l1, l2):
	pass
	s_pairs = zip(l2, l1)
	#print(sorted(s_pairs))
	sorted_list = [b for a,b in sorted(s_pairs)]
	print(sorted_list)

# sort_one_list_using_other(l1= ["a", "b", "c", "d", "e", "f", "g", "h", "i"], l2= [ 0,   1,   1,    0,   1,   2,   2,   0,   1])


def n_largest_numbers(input, N):
	pass
	lar_list = sorted(input, reverse=True)
	print(lar_list[:N])
#n_largest_numbers(input=[81, 52, 45, 10, 3, 2, 96]  , N=3)


def second_largest_in_list(list1):
	pass
	first = second = list1[0]
	
	for i in range(1, len(list1)):
	#	print(list1[i])
		if list1[i] > first:
			second = first
			first = list1[i]
		elif list1[i] > second and  list1[i] < first:
			second =  list1[i]
			

	print(first, second)


#second_largest_in_list(list1 =[12, 45, 2, 41, 31, 10, 8, 6, 4])


def sort_list_without_inbuilt_funcs(numlist):
	pass
	for i in range(len(numlist)):
		for j in range(i+1, len(numlist)):
			print(i,j)
			if numlist[i] >  numlist[j]:
				temp = numlist[i]
				numlist[i] =numlist[j]
				numlist[j] = temp
	
	print(numlist)
#sort_list_without_inbuilt_funcs(numlist=[86,67,34,55])


def isPall(s): 
    return s[::-1]==s


def palindrome_count(pc):
	pass
	s = pc
	for i in range(1, len(s)):
		start =0 
		end = i
		while end <= len(s):
			if isPall(s[start:end]):
				print('Palindrome', s[start:end])
			start += 1
			end += 1

#palindrome_count(pc='madam')

def factorial(f):
	pass
	if f == 1 or 0:
		print(1)
	elif f > 1:
		mul = 1
		while f > 1:
			
			mul *= f
			f = f-1
		print(mul)

	if f == 0 or f ==1:
		return 1
	else:
		return f * factorial(f-1)
#print(factorial(f=4))

def check_prime_number(num):
	pass
	if num == 1:
		return False
	for i in range(2, num):
		if (num%i) == 0:
			return False
		return True


#print(check_prime_number(num=23))

def prime_number_interval(start, end):
	pass
	for i in range(start, end):
		print(i)
		if i > 1:
			for j in range(2, i):
				if(i % j==0): break
			else:
				print('A Prime Number:', i)


#prime_number_interval(start=11, end=25)

def Fibonacci_number(n):
	pass
	a = 0
	b = 1
	if n == 0:
		return 0
	elif n == 1:
		return b
	elif n > 1:
		for i in range(2, n):
			c = a + b
			#print(c)
			a = b
			#print(a,b)
			b = c
			#print(b,c)
		return b

	# if n<0:
	# 	print("Incorrect input")
	# # First Fibonacci number is 0
	# elif n==1:
	# 	return 0
	# # Second Fibonacci number is 1
	# elif n==2:
	# 	return 1
	# else:
	# 	return Fibonacci_number(n-1)+Fibonacci_number(n-2)
#print(Fibonacci_number(n=9))

def check_armstrong_number(num):
	pass
	sum = 0

	# find the sum of the cube of each digit
	temp = num
	while temp > 0:
		digit = temp % 10
		#print(digit)
		sum += digit ** 3
		temp //= 10
		print(temp)

	# display the result
	if num == sum:
		print(num,"is an Armstrong number")
	else:
		print(num,"is not an Armstrong number")

#check_armstrong_number(num=153)


lst1 = [1,2,3,4,'a','v','d',[1,2,3,[14,13,12],'as','sd0','sd1'],'a',[2.4,5]] 
lst2 = [10,20,30,40,'a','v','d',[1,2,3,[14,13,12],'as','sd0','sd1'],'a',[2.4,5]] 
newlist = [] 
def nestedlists(lst, newlist=None): 
	if newlist is None: 
  	  newlist= [] 
	for i in lst: 
		if type(i)!=list: 
			newlist.append(i) 
		else: 
			nestedlists(i, newlist) 
	return newlist 
# print(nestedlists(lst1)) 
# print(nestedlists(lst2)) 

def multiples_5_and_7(n):
	pass
	for i in range(n):
		if i%5 ==0 and i%7==0:
			print('in 5 and 7')
		elif i%5 ==0:
			print('in 5')
		elif i%7 ==0:
			print('in 7')
		else:
			print(i)

#multiples_5_and_7(n=100)

def convert_binary_integer(b):
	int_value = int(b)
	print(int_value)

#convert_binary_integer(b='1000')


def string_to_ascii(s):
	pass
	ascii_value = [str(ord(i)) for i in s]
	print(''.join(ascii_value))

#string_to_ascii(s='abcd')


def tuples_comparision(t1,t2):
	pass
	#all(x < y for x, y in zip(test_tup1, test_tup2)) 
	unique_val = [i for i in t1 if i not in t2]
	print(unique_val)

#tuples_comparision(t1=(1,2,3),t2=(1,4,5,))

def set_comparision(s1, s2):
	pass
	#s.symmetric_difference(t) new set with elements in either s or t but not both
	#s.difference_update(t) return set s after removing elements found in t
	#s.symmetric_difference_update(t) return set s with elements from s or t but not both
	# _update method updates the original set

	intersection = s1.intersection(s2)
	difference = s1.difference(s2)
	union = s1.union(s2)
	symmertic_difference = s1.symmetric_difference(s2)
	#difference_update = s1.difference_update(s2)
	#symmertic_difference_update = s2.symmetric_difference_update(s1)
	print(intersection,difference,union,symmertic_difference)
	print(difference, s1)
	print(s1.issubset(s2))
	print(s1.issuperset(s2))

#set_comparision(s1={1,2,3}, s2={1,2,3,4,5,6})

def remove_blank_lines(t):
	pass
	lines = [s.strip() for s in t.split("\n") if s.strip()]
	print(lines)
# remove_blank_lines(t='hi there here is\na big line\n\nof empty\nline\neven some with spaces\n     \nlike that\n\n    \nokay now what?\n' 
# )


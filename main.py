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

# def isPall(s): 
#     return s[::-1]==s


# def count_palindrome(s):
# 	#s=str(input("enter the string:-"))

# 	for i in range(1, len(s)+1): 
# 		start = 0 
# 		end = i 
# 		while end<len(s)+1: 
# 			if isPall(s[start:end]): 
# 				print(s[start:end]) 
# 			start+=1 
# count_palindrome(s='madam')

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
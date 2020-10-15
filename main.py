from collections import defaultdict, OrderedDict 

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
#Source: #https://www.w3resource.com/python-exercises/pandas/index.php


#https://www.w3resource.com/python-exercises/pandas/index.php


import pandas as pd

df = pd.DataFrame({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})

print(df)

# 2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels.

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, 9, 20, 14.5, 1,2, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df1 = pd.DataFrame(index=labels, data=exam_data)

print(df1)


# Write a Pandas program to display a summary of the basic information about a specified DataFrame and its data.

df2 = pd.DataFrame(index=labels,data=exam_data)

print(df2.info())
print(df2['name'])
# Pandas program to select the specified columns and rows from a given data frame.
print(df2[['name','score']])

# Pandas program to select the rows where the number of attempts in the examination is greater than 2.

print(df2[df2['attempts']>2])

#  Write a Pandas program to count the number of rows and columns of a DataFrame

print(len(df2.axes[0]))

print(len(df2.axes[1]))

#  Write a Pandas program to select the rows where the score is missing, i.e. is NaN.

print(df2[df2['score'].isnull()])

#  Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).

print(df2[df2['score'].between(10,15)])


#  Write a Pandas program to select the rows where number of attempts in the examination is less than 2 and score greater than 1

print(df2[(df2['attempts']<2) & (df2['score']>15)])


# Pandas Indexing: Exercises, Practice, Solution

#  Write a Pandas program to display the default index and set a column as an Index in a given dataframe

df3 = pd.DataFrame({
    'school_code': ['s001','s002','s003','s001','s002','s004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'date_Of_Birth': ['15/05/2002','17/05/2002','16/02/1999','25/09/1998','11/05/2002','15/09/1997'],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4'],
    't_id':['t1', 't2', 't3', 't4', 't5', 't6']})

print(df3)

print("Default Index :{}" .format(df3.head(10)))

df3.set_index('school_code', inplace=True)

print("New Index :{}" .format(df3.head(10)))

# multi Index frame using two columns and using an Index and a column


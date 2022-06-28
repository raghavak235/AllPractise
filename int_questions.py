# input_1 = {
#     "devices": {
#         "1": {
#             "name": "lenovoZ570",
#             "ip": "1.1.1.1"
#             },
#         "2": {
#             "name": "iphone12",
#             "ip": "10.20.1.2"
#             }
#         }
# }
#
#
# # expected_output={'lenovoZ570': '1.1.1.1', 'iphone12': '10.20.1.2'}
# #
# # def device_map(input):
# #     new_device_map={}
# #     devices=input.get("devices",{})
# #     for key in devices:
# #         device=devices[key]
# #         name,ip=device.get("name"),device.get("ip")
# #         new_device_map[name]=ip
# #     return new_device_map
# #
# #
# # print(device_map(input_1))
#
#
# # class First():
# #     def get_details(self):
# #         print("Calling get_details() from Class 'First'")
# #
# #
# # class Second():
# #     def get_details(self):
# #         print("Calling get_details() from Class 'Second'")
# #
# #
# # class Child(First, Second):
# #     def get_details(self):
# #         super(Child,self).get_details()
# #
# # child=Child()
# # child.get_details()
#
# # Input: ‘657’ let us say regular expression contain following characters-
# # (‘78653’)
# # Output: Valid
# # Explanation: The Input string only consist of characters present in the given string
# #
# # Input: ‘7606’ let us say regular expression contain following characters-
# # (‘102’)
# # Output: Invalid
#
#
# import re
#
# str1=""""
# vsnfovjsv
# sv
# vsfb;msf  pbhdio bd
# v enet'enet   b; b;dgbkd
# bnlkdboie t8 tt hteoi t
# """
#
#
# # lines=str1.split('\n')
# # print(lines)
# # print("total numbe of lines ", len(lines))
# # word_count=0
# # for line in lines:
# #     words=line.split()
# #     word_count+=len(words)
# # print("word count",word_count)
# #
# #
# Weather
#
# id 		Date 			temp
# 1 		2021/12/01 		33
# 2 		2021/12/02 		34
# 3 		2021/12/03 		20
# 4 		2021/12/04 		30
#
#
# select w2.id from weather w1 join weather w2 on w2.id-w1.id=1 where w2.temp>w1.temp;
#
# # Output => [2, 4, 6]
# #######################
# arr = [1, 2, 3]
#
# l = [e * 2 for e in arr]
# print(l)
#
# # # Output => [2, 4, 6]
# ##############################
# arr = [1, 2, 3, 4, 5]
#
# l = [e * 2 for e in arr if e <= 3]
# print(l)
#
# # Output => {1: 2, 2: 4, 3: 6}
# #######################
# arr = [1, 2, 3]
#
# d = {e: e * 2 for e in arr}
# print(d)
#
#
# def gen():
#     for i in range(10):
#         yield i
#
#
# assert gen() == 0
# assert gen() == 1
#
#
# class User(models.model):
#     name = models.Charfeild(max_length=100)
#     email = models.charfeild(max_legnth=100)
#
#     def __str__(self):
#         return self.email
#
#
# class Playlist(models.model):
#     name = model.charfield(max_lengh=100)
#     user = models.ForeignKey(User)
#     songs = models.ManyToManyFeild(Song)
#
#
# class Song(models.Model):
#     name = models.CharField()
#     duration = models.NumberField()
#     singler = models.ForeignKey()
#
#
# playlist_object = Playlist.objects.get(id=100)
#
# # list down all the songs related to playlist id 100
# # Song Name | Song Duration
# p = Playlist.objects.get(id=100)
#
# # p playlist has 1000 songs
#
# for song in p.songs.all():
#     print(song.name, song.duration)
#
# # List down all the playlists and their related username
# # Playlist 1, User1
# # Playlist 2, User 1
# # P3, U2
#
# # 1000 playlist
# users = Playlist.objects.all().users()
#
#
# playlist_cache = {}
# song_cache = {}
# # database perf issue
# for playlist in Playlist.objects.all():
#
# for song in playlist.songs.all():
#     print(playlist.name, song.name)
#
# # user can have multiple playlists
# # a song can be in multiple playlists and multiple playlist can have same song
#
# # Find out playlist with id 100

# A binary tree
#          1
#     2       3
# 4     5  6   7
#
# 4251637

    #   root
    # left right

# class Node:
#     def __init__(self,val,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
#
#
# def inorder(root):
#     output=[]
#     def traverse(node):
#         if not node:
#             return []
#         traverse(node.left)
#         output.append(node.val)
#         traverse(node.right)
#
#     traverse(root)
#     return output
#
#
# two=Node(2,Node(val=4),Node(val=5))
# three=Node(3,Node(val=6),Node(7))
# root=Node(1,two,three)
#
# print(inorder(root))

#
# import pandas as pd
#
# df = pd.read_csv("us-500.csv")
#
# print(df.head(5))
#
#
# print(df[['zip','first_name']])
#
# spark-submit test.py --master --cores --vir

# def square_root(x):
#     for i in range(0, x, 0.1):
#         print(round(i / 2 * i / 2, 0))
#         if i*i == x:
#             print(i)
#         elif int(round(i/2 * i/2,0)) == x:
#             print(i/2)
#
#
# square_root(5)
# import unittest
#
# def add(a,b):
#     return a+b
#
# def test_add(unitest):
#
#     self.assertEqual(2,3)==5
#

a=[1,2,3,4]
b=a
a=a+[5,6,7,8]
c=[1,2,3,4]
d=c
c+=[5,6,7,8]
print(a,b,c,d)




raw=[""]*3
board=[raw]*3
print(board)
print(board[0])
board[0][0] ='X'
print(board)

#
# permutation logic for strings
# using all and any with monotomic list
# l1=[1,3,5,7]
# l2=[1,2,37,2,3]
# l3=[5,4,3]
# write a single line logic to check wherthe its increasing or descreasing list using all and any
#
# x={0: None}
# for i in x:
#     del x[i]
#     x[i+1]=None
#     print(x[i])

# for i in range(7):
#     if i == 6:
#         print('Exists')
# else:
#     print('Doesnot exists')
#

# for i in range(3):
#     if i == 2:
#         print(i)
# print(i)

#
# def run_job(job_id):
#     print("")
#     return job_id
#
# def stop_job(job_id):
#     return job_id
#
# class MyJobScheduler:
#     jobs_dict = dict()
#     def __init__(self):
#
#         self.ALL_JOBS = dict()
#
#     def add_job(self, job_id):
#         jobs_dict=dict()
#
#         jobs_dict[job_id] = ''
#         self.ALL_JOBS[job_id]=''
#
#
#         jobs_exe=tuple()
#         jobs_exe.add(run_job(job_id))
#         pass
#     def delete_job(job_id):
#         pass
#     def execute_single_job(self,job_id):
#
#
#
#         if run_job(self.ALL_JOBS[job_id]):
#             self.ALL_JOBS[job_id] = True
#
#         elif time(run_job(self.ALL_JOBS[job_id])) >= 600:
#             self.delete_job(job_id)
#
#
#         pass
#     def execute_all_jobs(self):
#         for i in self.ALL_JOBS.keys():
#             if self.ALL_JOBS[i] == False:
#                 self.execute_single_job(i)
#
#
#         pass
#     def is_job_executed(job_id):
#
#         if self.ALL_JOBS[i] == False return True else False
#
#         if self.ALL_JOBS[i] == True:
#             return True
#         else:
#             return False
#
#         pass
#
#
# select j.job_id, j.job_name from Jobs j inner join job_details jd on j.job_id = jd.job_id
# where j.JOB_TYPE = 'PRIVATE' and jb.start_time = '2021-01-26 06:00' \
# and jd.end_time='2021-01-27 06:00'
#
#
# select max(end_time - start_time) from job_detials where job_id not in(
#
# select job_id, max(end_time - start_time) from job_detials
#
# )
#
# select j.job_id, j.job_name from Jobs j inner join job_details jd on j.job_id = jd.job_id
# where j.JOB_TYPE = 'RELEASE' and end_time - start_time > 60 ;
#
#
# def test_user_info():
#     val=extract_user_info('Raghava K', 'Dev')
#     self.assertEqual()
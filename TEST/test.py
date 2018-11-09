import os,sys
import time
import pandas as pd
from operator import itemgetter
os.chdir('E:\Sample Data')

# num_lines = sum(1 for line in open('00_0683828_D06_LDAP_INFO.full.convert.errors'))

# def file_len(fname):
#     with open(fname) as f:
#         for i, l in enumerate(f):
#             pass
#     return i + 1
# start_time = time.time()
# print(num_lines)
# print("--- %s seconds ---" % (time.time() - start_time))
# start_time = time.time()
# print(file_len('00_0683828_D06_LDAP_INFO.full.convert.errors'))
# print("--- %s seconds ---" % (time.time() - start_time))

# Slicer = 0

# with open('00_0683828_D06_LDAP_INFO.full.convert.errors') as afile:
#     for line in afile:
        
test = {'c': {'a': {'aa':None,'aaa':None}},'d':{'b':{'bb':None}}}
# file_name = []
# column_list = []
# column_comb = []
# # for key,value in test.items(:
# #     print(key)
# #     print(value)
# for key,value in test.items():
#     item = []
#     file_name.append(key)
#     for i in value:
#         column_comb.append(i)
#         item.append(i)
#     column_list.append(item)

# print(file_name,column_comb,column_list)
# a = {'a': {'aa': {'cc':'1','a':'11'},'aaaa': None}}
# test['c'].update(a)
# print(test)
# b = {'a': {'aa': {'cc':'2'},'aaaa': None}}
# test['c'].update(b)
# print(test)

# test1 = {'b': 'aa'}
# test2 = {'b': 'bb'}

# # test1.update(test2)
# # print(test1)

# print('start')
# print(a)
# try:
#     a['a']['aa'].update(test1)
# except KeyError:
#     a['a']['aa'] = test1

# print(a)

# d = {}
# print(d['a'])
# col = ['max_speed', 'shield']

# index = [1,2]
# df = pd.DataFrame([[1, 2], [4, 5], [7, 8]],columns=col)

# for col in col :
#     print(df.loc[:,col])
#     df.loc[:,col] = 1
# print(df)


# s2 = pd.Series([7, 8, 9])
d = {'A': [1, 2], 'C': [3, 4]}
df_f = pd.DataFrame(data=d)
df = pd.DataFrame(  columns =  ["A", "B", "C"])
# df_f = pd.DataFrame([1,3],columns = ['A','C'])
# print(df_f)
# df.loc[-1] = [7, 3, 4]  # adding a row
# df.index = df.index + 1  # shifting index
# df = df.sort_index()

a = 0

while a <=5:
    
    if a ==0:
        print(a)
        a = a +1
        continue
    df.loc[a-1] = [a,a+1,a+2]
    a = a +1

df_f =df_f.append(df)
print('df:')
print(df_f)

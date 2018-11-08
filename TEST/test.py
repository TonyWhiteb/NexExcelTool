import os,sys
import time


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
a = {'a': {'aa': {'cc':'1','a':'11'},'aaaa': None}}
test['c'].update(a)
print(test)
b = {'a': {'aa': {'cc':'2'},'aaaa': None}}
test['c'].update(b)
print(test)

test1 = {'b': 'aa'}
test2 = {'b': 'bb'}

# test1.update(test2)
# print(test1)

print('start')
print(a)
try:
    a['a']['aa'].update(test1)
except KeyError:
    a['a']['aa'] = test1

print(a)

# d = {}
# print(d['a'])
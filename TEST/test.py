import os,sys
import time
import pandas as pd
from operator import itemgetter
from itertools import islice
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

# a = 100
# b = 15
# print(a/b)
# print(int(a/b))

# def SheetName(Slicer):
#     sheet_list = []
#     for i in range(Slicer):
#         sheet_list.append('Sheet%d' %int(i+1))
#     return sheet_list

# a = 5

# b = SheetName(a)

# print (b)
os.chdir('E:\TEST')

def file_block(fp, number_of_blocks, block):

 
    assert 0 <= block and block < number_of_blocks
    assert 0 < number_of_blocks
 
    fp.seek(0,2)
    file_size = fp.tell()
    print('file_size: %s' %(file_size))
    ini = file_size * block / number_of_blocks
    print('ini: %s' %(ini))
    end = file_size * (1 + block) / number_of_blocks
    print('end: %s' %(end))
 
    if ini <= 0:
        fp.seek(0)
    else:
        fp.seek(ini-1)
        mid = fp.readline()
        print('mid: %s' %(mid))
 
    while fp.tell() < end:
        yield fp.readline()
 
if __name__ == '__main__':
    fp = open('test.txt')
    number_of_chunks = 4
    for line in file_block(fp, number_of_chunks, 0):
        print(line)
    # fo = open("test.txt")
    # print ("Name of the file: ", fo.name)

    # # Assuming file has following 5 lines
    # # This is 1st line
    # # This is 2nd line
    # # This is 3rd line
    # # This is 4th line
    # # This is 5th line

    # # line = fo.readline()
    # # print ("Read Line: %s" % (line))

    # # Again set the pointer to the beginning
    # fo.seek(0)
    # line = fo.readline()
    # print ("Read Line: %s" % (line))

    # pos = fo.tell()
    # print ("Current Position: %d" % (pos))

    # # Close opend file
    # fo.close()

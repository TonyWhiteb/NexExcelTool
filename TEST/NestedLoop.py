import os,sys
import time
import pandas as pd
from operator import itemgetter
from itertools import islice

test = ['a','b','c','d','e']
test2 = ['f','g','h','i','j']

# for i in range(5):
#     print(test[i])

#     for j in range(5):
#         print(test2[j])
        
#         for m in range(5):
#             print(m)
#             if  m == 3:
#                 break
# for i in range(5):
#     print(test[i])

#     for j in range(5):
#         print(test2[j])
        
#         for m in range(5):
#             print(m)
#             if  m == 3:
#                 continue

for i in range(5):
    print(test[i])

    for j in range(5):
        print(test2[j])
        
        for m in range(5):
            print(m)
            if  m == 3:
                pass
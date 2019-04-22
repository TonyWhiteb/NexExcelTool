import os,sys
import time
import pandas as pd
from operator import itemgetter
from itertools import islice

os.chdir('E:\TEST')

with open('PAYTODAT_ERROR.errors') as f:
    test = sum(1 for _ in f )

print(test)
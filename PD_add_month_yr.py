import pandas as pd
from collections import defaultdict
import datetime

##df = pd.read_csv('survey_data.csv')

def add_month_yr(x):
    assert isinstance(x, pd.core.frame.DataFrame)
    col = []
    for i in x['Timestamp']:
        my = ''
        nums = i.split('/')
        datetime_object = datetime.datetime.strptime(nums[0], "%m")
        my+=datetime_object.strftime("%b")
        my+='-'
        my+=nums[2][:4]
        col.append(my)
        
    x['month-yr'] = col
    return x

def count_month_yr(x):
    ''' Write a function count_month_yr to create the following dataframe using your new column month-yr, '''
    assert isinstance(x, pd.core.frame.DataFrame)
    ct = defaultdict(int)
    for i in x['month-yr']:
        ct[i]+=1
    tups = []
    for k in ct.keys():
        tups.append((k, ct[k]))
    tups.sort(key = lambda x:x[1])
    idx = ['month-yr']
    ts = [0]
    for t in tups:
        idx.append(t[0])
        ts.append(t[1])
    ts[0] = None
    dic = {}
    dic['Timestamp'] = ts
    return pd.DataFrame(dic, index = idx)

##print(count_month_yr(add_month_yr(df)))

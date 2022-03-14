import pandas as pd
from collections import defaultdict

##df = pd.read_csv('survey_data.csv')
##a = df['Is there anything in particular you want to use Python for?']

def split_count(x):
    '''Here is the function signature: split_count(x) where x is a pd.Series object and it returns a pd.DataFrame object.'''
    assert isinstance(x, pd.core.series.Series)
    dic = defaultdict(int)
    for i in x:
        left = -2
        for c in range(len(i)):
            if i[c] == ',':
                dic[i[left+2:c]]+=1
                left = c
        dic[i[left+2:]]+=1
    dicdata = []
    for k in dic.keys():
        dicdata.append((k,dic[k]))
    dicdata.sort(key=lambda x:x[1])
    idx = []
    ct = []
    for d in dicdata:
        idx.append(d[0])
        ct.append(d[1])
    dic = {}
    dic['count'] = ct
    return pd.DataFrame(dic, index = idx)


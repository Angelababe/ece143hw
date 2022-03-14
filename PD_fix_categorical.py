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

def fix_categorical(x):
    ''' Convert the month-yr column dtype to a Pandas CategoricalDtype with the correct order'''
    assert isinstance(x, pd.core.frame.DataFrame)
    x['month-yr']= pd.Categorical(x['month-yr'], ['Sep-2017', 'Jan-2018', 'Feb-2018', 'Mar-2018','Apr-2018', 'Sep-2018', 'Oct-2018', 'Jan-2019'], ordered = True)
    ##print(x.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())
    return x

##fix_categorical(add_month_yr(df))

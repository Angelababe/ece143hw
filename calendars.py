import calendar
def number_of_days(year,month):
    '''Write a function that returns the number of calendar days in a given year and month.'''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert 1<=month<=12
    assert year>0
    obj = calendar.Calendar()
    ret = 0
    for day in obj.itermonthdays(year, month):
        if day:
            ret+=1
    return ret

def number_of_leap_years(year1,year2):
    '''Write a function to find the number of leap-years between (including both endpoints) two given years.'''
    assert isinstance(year1, int)
    assert isinstance(year2, int)
    assert year1>0
    assert year2>0
    assert year2>year1
    ret = 0
    for i in range(year1, year2+1):
        if calendar.isleap(i):
            ret+=1
    return ret

def get_day_of_week(year,month,day):
    '''Write a function to find the string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year.'''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert isinstance(day, int)
    assert year>0
    assert 1<=month<=12
    assert 1<=day<=31
    return calendar.day_name[calendar.weekday(year, month, day)]
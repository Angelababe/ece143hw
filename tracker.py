def tracker(p, limit):
    '''Write a generator that tracks the output of this producer and ultimately returns the number of odd numbered seconds that have been iterated over.'''
    assert isinstance(limit, int)
    assert limit>0
    l = limit
    while limit>0:
        sec = int(next(p).total_seconds())
        if sec%2:
            limit -= 1
        temp = yield l-limit
        if temp:
            l = temp
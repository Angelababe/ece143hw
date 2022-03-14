from collections import defaultdict
def gather_values(x):
    '''Write a function gather_values that can produce the following output from x'''
    assert isinstance(x, list)
    ret = defaultdict(list)
    for b in x:
        assert isinstance(b, str)
        z = 0
        o = 0
        for c in b:
            assert 48<=ord(c)<=49
            if c=='0':
                z+=1
            else:
                o+=1
        if z>o:
            ret[b].append(0)
        else:
            ret[b].append(1)

    return ret

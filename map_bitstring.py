def map_bitstring(l):
    '''Write a function map_bitstring that takes a list of bitstrings (i.e., 0101) and maps each bitstring to 0 if the number of 0s in the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1.'''
    assert isinstance(l, list)
    ret = {}
    for b in l:
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
            ret[b] = 0
        else:
            ret[b] = 1

    return ret

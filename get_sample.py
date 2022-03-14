def get_sample(nbits=3,prob=None,n=1):
    '''Given a number of bits, write the get_sample function to return a list n of random samples from a finite probability mass function defined by a dictionary with keys defined by a specified number of bits.'''
    assert isinstance(nbits, int)
    assert nbits>0
    assert isinstance(n, int)
    assert n>0
    assert isinstance(prob, dict)
    ret = []
    i=0
    sum = 0
    for p in prob.keys():
        assert isinstance(p, str)
        assert len(p) == nbits
        assert isinstance(prob[p], float)
        assert 0<=prob[p]<=1
        sum += prob[p]
        if i<n:
            ret.append(p)
            i+=1

    assert sum==1
            
    return ret

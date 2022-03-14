from collections import defaultdict
def threshold_values(seq, threshold):
    '''threshold those values based upon their frequency and value.'''
    assert isinstance(threshold, int)
    assert threshold>0
    assert threshold<=len(seq)
    dic =gather_values(seq)
    tups=[]
    for d in dic:
        if dic[d][0] == 1:
            tup = (d, len(dic[d]))
            tups.append(tup)
    assert threshold<=len(tups)
    tups.sort(key=lambda x:x[1], reverse = True)
    print(tups)
    if threshold == len(tups):
        for d in dic:
            dic[d] = 1
        return dic
    bucket = []
    ret = []
    for i in range(len(tups)-1):
        if tups[i+1][1] == tups[i][1]:
            bucket.append(tups[i])
        else:
            bucket.append(tups[i])
            if len(bucket)>threshold:
                bucket.sort(key=lambda x:x[0])
                ret += bucket[:threshold+1]
                threshold = 0
            else:
                ret+=bucket
                threshold -= len(bucket)
            if not threshold:
                break
            bucket = []

    for d in dic:
        if (d, len(dic[d])) in ret:
            dic[d] = 1
        else:
            dic[d] = 0
    return dic

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

def get_trapped_water(seq):
    '''Compute how many units of water remain trapped between the walls in the map.'''
    assert isinstance(seq, list)
    for s in seq:
        assert isinstance(s, int) and s>=0
    height = seq
    if len(height)<3:
        return 0
    if height[0] <= height[1]:
        idxstack = [1]
    else:
        idxstack = [0, 1]
    ret = 0
    for i in range(2, len(height)):
        while idxstack and height[i] > height[idxstack[-1]]:
            idx = idxstack.pop()
            if not idxstack:
                break
            ret += (i-idxstack[-1]-1) * (min(height[i], height[idxstack[-1]]) - height[idx])
        idxstack.append(i)
    return ret

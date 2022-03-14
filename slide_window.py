def slide_window(x,width,increment):
    '''The function should take the window width and the window increment as inputs and should produce a sequence of overlapping lists from the input list.'''
    assert isinstance(x, list)
    assert isinstance(width, int)
    assert width>0
    assert isinstance(increment, int)
    assert increment>0
    ret = []
    for i in range(int((len(x)-width)/increment) + 1):
        ret.append(x[i*increment:i*increment+width])
        
    return ret
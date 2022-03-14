import numpy as np

def gen_rand_slash(m=6,n=6,direction='back'):
    '''write a function that can produce a uniformly random forward or backslashed image (i.e., Numpy array) of at least two non-zero pixels'''
    assert isinstance(m, int)
    assert isinstance(n, int)
    assert m>1 and n>1
    assert isinstance(direction, str)
    assert direction == 'back' or direction == 'forward'
    mapp = np.zeros((m, n))
    x = np.random.randint(m-1)
    y = np.random.randint(n-1)
    length = np.random.randint(2, min(m-x, n-y)+1)
    for i in range(length):
        mapp[x][y] = 1
        x+=1
        y+=1
    if direction == 'back':
        return mapp
    else:
        return np.flip(mapp, 1)

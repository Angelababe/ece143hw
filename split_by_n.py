import os

def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert isinstance(n, int)
    assert n>0
    assert isinstance(fname, str)
    filesize = os.path.getsize(fname)
    chunksize = int(filesize/n)
    fd = open(fname, 'rt')
    postfixs = []
    for i in range(n):
        postfixs.append('_'+'0'*(3-len(str(i))) + str(i)+'.txt')

    chunk = fd.read(chunksize)
    for i in range(n):
        writename = fname + postfixs[i]  
        with open(writename, 'wt') as output:
            if i<n-1:
                c = chunk.rsplit('\n', 1)[0]
            else:
                c = chunk+fd.read(chunksize)
            output.write(c)
        chunk = '\n' + chunk.rsplit('\n',1)[1] + fd.read(chunksize)
    fd.close()
    return

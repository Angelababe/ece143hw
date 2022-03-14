def fibonacci(n):
    '''The Fibonacci numbers are defined by the following recursion: F[n] = F[n-1]+F[n-2] with initial values F[1]=F[0]=1. Write a generator to compute the first n Fibonacci numbers.'''
    assert isinstance(n, int)
    assert n>0
    ret = [1, 1]
    for i in range(n):
        if i==0 or i==1:
            yield 1
            continue
        ret.append(ret[i-2]+ret[i-1])
        yield ret[-1]
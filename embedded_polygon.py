import numpy as np
def est_prob(n:int, m:int, niter:int=100)->float: 
    '''                                                                                        
    :param n: num sides in regular polygon (n>=4)                                           
    :type n: int                                                                               
    :param m: num vertices for inscribed polygon (m>=3)                                     
    :type m: int                                                                               
    :param niter: num iterations for simulation 
    :type m: int                                                                               
    '''
    assert isinstance(n, int) and n>=4
    assert isinstance(m, int) and m>=3
    assert isinstance(niter, int) and niter>0
    assert m<n
    all_iter = niter
    pass_iter = 0
    res = 0
    while niter >= 0:
        ver = np.random.choice(n, size = m, replace = True)
        if len(set(ver)) == m:
            pass_iter += 1
        niter -= 1
    return pass_iter/all_iter

def f(n):
    if n == 0:
        return 1
    else:
        return n*f(n-1)

def get_prob_shape(n:int, m:int, equilateral:bool=False)->float:     
    '''                                                                                                           
    :param n: num sides in regular polygon (n>=4)                                                              
    :type n: int                                                                                                  
    :param m: num vertices for inscribed polygon (m>=3)                                                        
    :type m: int                                                                                                  
    '''
    assert isinstance(n, int) and n>=4
    assert isinstance(m, int) and m>=3
    assert isinstance(equilateral, bool)
    assert m<n
    if not equilateral:
        return f(n)/(f(n-m)*(n**m))
    else:
        if n%m != 0:
            return 0
        else:
            return (n/m) * f(m) /n**m

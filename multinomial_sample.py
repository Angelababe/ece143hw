import random

def multinomial_sample(n,p,k=1):  
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                             
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''
    assert isinstance(n, int)
    assert isinstance(p, list)
    assert sum(p) == 1
    assert isinstance(k, int)
    for i in range(1, len(p)):
        p[i] = p[i]+p[i-1]
    ret = []
    print(p)
    
    for _ in range(k):
        result = [0]*len(p)
        for i in range(n):
            rand = random.random()
            for j in range(len(p)):
                if rand<p[j]:
                    result[j]+=1
                    break
        ret.append(result)

    return ret
        

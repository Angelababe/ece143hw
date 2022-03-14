def get_power_of3(num):
    '''Write a compute_average_word_length(instring,unique=False) function to compute the average length of the words in the input string (instring). If the unique option is True, then exclude duplicated words.'''
    assert isinstance(num, int)
    assert 1<=num<=40
    nums = [1,3,9,27]
    res = []
    def backtrack(i, remain, ret):
        nonlocal res
        if not remain:
            if len(ret)<4:
                complen = 4-len(ret)
                for j in range(complen):
                    ret.append(0)
            res = ret
            return
        if i==4:
            return
        for op in [-1, 0, 1]:
            backtrack(i+1, remain-(nums[i]*op), ret+[op])
    
    backtrack(0, num, [])
    return res
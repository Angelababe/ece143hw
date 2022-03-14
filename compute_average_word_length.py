from collections import defaultdict
def compute_average_word_length(instring,unique=False):
    '''Write a compute_average_word_length(instring,unique=False) function to compute the average length of the words in the input string (instring). If the unique option is True, then exclude duplicated words.'''
    assert isinstance(instring, str)
    assert len(instring)>0
    assert not instring[-1] == ' ' and not ord(instring[-1]) == 10
    words = defaultdict(int)
    space = 0
    for i in range(len(instring)):
        assert 65<=ord(instring[i])<=90 or 97<=ord(instring[i])<=122 or instring[i] == ' ' or ord(instring[i])==10
        if instring[i] == ' ' or ord(instring[i])==10:
            assert not instring[i-1] == ' ' and not ord(instring[i-1])==10
            words[instring[space:i]]+=1
            space = i+1
            
    words[instring[space:]]+=1
    
    ret = 0
    num = 0
    if unique:
        for w in words:
            ret+=len(w)
            num+=1
        return ret/num
    else:
        for w in words:
            ret+=len(w)*words[w]
            num+=words[w]
        return ret/num
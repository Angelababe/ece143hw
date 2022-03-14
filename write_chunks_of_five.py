def write_chunks_of_five(words,fname):
    '''Using corpus of 10,000 common English words, create a new file that consists of each consecutive non-overlapping sequence of five lines merged into one line. Here are the first 10 lines of ouptut corresponding to the above sample corpus:'''
    assert isinstance(words, list)
    assert isinstance(fname, str)
    for w in words:
        assert isinstance(w, str)
    i = 0
    f = open(fname, "w")
    while i<len(words):
        if i<len(words)-5:
            f.write(words[i]+" "+words[i+1]+" "+words[i+2]+" "+words[i+3]+" "+words[i+4]+"\n")
        else:
            line = ""
            for j in range(i, len(words)):
                line+=words[j]
                if j<len(words)-1:
                    line+=" "
            f.write(line)
        i+=5
    f.close()
    return
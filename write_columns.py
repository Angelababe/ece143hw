def write_columns(data,fname):
    '''Write a function that can write the following formula to three columns to a comma-separated file:'''
    assert isinstance(data, list)
    assert isinstance(fname, str)
    f = open(fname, "w")
    itr = 0
    for d in data:
        assert isinstance(d, int) or isinstance(d, float)
        line = ""
        n1 = round(d*100)/100
        if not n1%1:
            n1 = int(n1)
        line += str(n1)
        line += ","
        n2 = round(d**2*100)/100
        if not n2%1:
            n2 = int(n2)
        line += str(n2)
        line += ","
        n3 = round(((d+d**2)/3)*100)/100
        if not n3%1:
            n3 = int(n3)
        line += str(n3)
        itr+=1
        if itr<len(data):
            line += "\n"
        f.write(line)
    f.close()
    return
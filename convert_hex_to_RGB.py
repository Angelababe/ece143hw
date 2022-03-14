def convert_hex_to_RGB(colors):
    '''Given a list of color hex-codes (e.g., ['#FFAABB']), write a function to convert these into a list of RGB-tuples. For example, [(255,170,187)] corresponds to the example above. Please name the function convert_hex_to_RGB.'''
    assert isinstance(colors, list)
    hextodec = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}
    tuples = []
    for c in colors:
        assert isinstance(c, str)
        assert c[0] == '#'
        assert len(c) == 7
        f = 0
        s = 0
        t = 0
        for i in range(1, 7):
            assert 48<=ord(c[i])<=57 or 65<=ord(c[i])<=90
            if 48<=ord(c[i])<=57:
                if i==1:
                    f+=int(c[i])*16
                elif i==2:
                    f+=int(c[i])
                elif i==3:
                    s+=int(c[i])*16
                elif i==4:
                    s+=int(c[i])
                elif i==5:
                    t+=int(c[i])*16
                elif i==6:
                    t+=int(c[i])
            else:
                if i==1:
                    f+=hextodec[c[i]]*16
                elif i==2:
                    f+=hextodec[c[i]]
                elif i==3:
                    s+=hextodec[c[i]]*16
                elif i==4:
                    s+=hextodec[c[i]]
                elif i==5:
                    t+=hextodec[c[i]]*16
                elif i==6:
                    t+=hextodec[c[i]]
        tup = (f,s,t)
        tuples.append(tup)
            
    return tuples
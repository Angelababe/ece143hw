import math
import numpy as np
from collections import defaultdict
def find_convex_cover(pvertices,clist):
    ''' find_convex_cover(pvertices,clist)'''
    assert isinstance(pvertices, np.ndarray) and isinstance(clist, list)
    for p in pvertices:
        assert len(p) == 2
        for n in p:
            assert isinstance(n, float) or isinstance(n, int)
    for c in clist:
        assert isinstance(c, tuple) and len(c) == 2
        for n in c:
            assert isinstance(n, float) or isinstance(n, int)
            
    dists = []
    for i in range(len(pvertices)):
        x1, y1 = pvertices[i][0], pvertices[i][1]
        dislist = []
        for j in range(len(clist)):
            x2, y2 = clist[j][0], clist[j][1]
            d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            dislist.append((d,j))
        dislist.sort(key = lambda x:x[0])
        dists.append(dislist[0])

    ret = [0]*len(clist)
    for d in dists:
        ret[d[1]] = max(ret[d[1]], d[0])

    return ret


    

def count_paths(m,n,blocks):
    '''find the number of connected paths between the top-left square and the bottom right square by traversing only the intermediate squares with the . symbol.'''
    assert isinstance(m, int) and m>0
    assert isinstance(n, int) and n>0
    assert isinstance(blocks, list)
    for b in blocks:
        assert isinstance(b, tuple)

    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        if (i,0) in blocks:
            break
        else:
            dp[i][0] = 1
    for i in range(n):
        if (0,i) in blocks:
            break
        else:
            dp[0][i] = 1

    for i in range(1, m):
        for j in range(1, n):
            if not (i,j) in blocks:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
            else:
                dp[i][j] = 0
    
    return dp[-1][-1]

#print(count_paths(3,4,[(0,1),(1,0)]))

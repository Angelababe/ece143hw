def next_permutation(t:tuple)->tuple:
    '''Given a permutation of any length, generate the next permutation in lexicographic order.'''
    assert isinstance(t, tuple)
    se = set()
    for n in t:
        assert isinstance(n, int) and n<=len(t)
        assert not n in se
        se.add(n)

    stack = []
    for i in reversed(range(len(t))):
        if i>0 and t[i-1]<t[i]:
            stack.append(t[i])
            stack.append(t[i-1])
            break
        stack.append(t[i])
        
    if i==0:
        return tuple(stack)
    last = stack[-1]
    stack.sort()
    idx = 0
    for j in range(len(stack)-1):
        if stack[j] == last:
            idx = j+1
    stack = [stack[idx]] + sorted(stack[:idx] + stack[idx+1:])

    return t[:i-1]+tuple(stack)

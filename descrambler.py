import itertools
from collections import defaultdict
def descrambler(w,k):
    '''You are given a sequence of n lower-case letters and a k-tuple of integers that indicate partition-lengths of the sequence.'''
    assert isinstance(w, str)
    assert isinstance(k, tuple)
    for num in k:
        assert isinstance(num, int)
        assert num>0

    with open("/tmp/google-10000-english-no-swears.txt", "r") as fd:
        lines = fd.read().splitlines()
    word = defaultdict(set)
    for l in lines:
        word[len(l)].add(l)
    let = defaultdict(int)
    for le in w:
        let[le]+=1
    visited = []
    def helper(i, letters, ret):
        string = ""
        for le in letters:
            for n in range(letters[le]):
                string+=le
        for per in itertools.permutations(string, k[i]):
            perword = ""
            for p in per:
                perword+=p
            if perword in word[k[i]]:
                if i == len(k)-1:
                    output = ret+" "+perword
                    if not output in visited:
                        visited.append(output)
                        yield output[1:]
                else:
                    for p in per:
                        letters[p] -= 1
                    yield from helper(i+1, letters, ret+" "+perword)
                    for p in per:
                        letters[p] += 1
                    
    yield from helper(0, let, "")

    

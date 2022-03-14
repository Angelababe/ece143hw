import random
from collections import defaultdict

def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
       
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message, str)
    assert isinstance(fname, str)
    for c in message:
        assert (c.isalpha() and c.islower()) or c==' '
    code = en_codebook(fname)
    ret = []
    for m in message.split():
        assert m in code
        tup = random.choice(list(code[m]))
        del code[m][tup]
        ret.append(tup)
    return ret

def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message. 
      
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist, list)
    assert isinstance(fname, str)
    for i in range(len(inlist)):
        assert isinstance(inlist[i], tuple)
        assert isinstance(inlist[i][0], int)
        assert isinstance(inlist[i][1], int)
        for j in range(i+1, len(inlist)):
            assert not inlist[i] == inlist[j]
    code = de_codebook(fname)
    ret = ""
    for il in inlist:
        ret += (code[il]+' ')
    return ret[:-1]

def en_codebook(fname):
    codebook = defaultdict(dict)
    with open(fname, 'r') as fd:
        lines = fd.read().splitlines()
        for i in range(len(lines)):
            words = lines[i].split()
            for j in range(len(words)):
                word = [c.lower() for c in words[j] if c.isalpha()]
                word = "".join(word)
                if word:
                    codebook[word][(i, j)] = 1

    return codebook

def de_codebook(fname):
    codebook = {}
    with open(fname, 'r') as fd:
        lines = fd.read().splitlines()
        for i in range(len(lines)):
            words = lines[i].split()
            for j in range(len(words)):
                word = [c.lower() for c in words[j] if c.isalpha()]
                word = "".join(word)
                if word:
                    codebook[(i,j)] = word

    return codebook

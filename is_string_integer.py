def is_string_integer(string):
    '''Write a function that takes a single string character (i.e., 'a','b','c') as input and returns True or False if that character represents a valid integer in base 10.
    param string: input chart\ntype string: str\nreturn: boolean'''
    assert isinstance(string, str)
    assert len(string) == 1
    if ord(string)<48 or ord(string)>57:
        return False
            
    return True
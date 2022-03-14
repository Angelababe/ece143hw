class Interval(object):
    def __init__(self,a,b):
        """
        :a: integer
        :b: integer
        """
        assert a<b
        assert isinstance(a,int)
        assert isinstance(b,int)
        self._a = a
        self._b = b
    
    def __repr__(self):
        ''' return '''
        return 'Interval(' + str(self._a) + ',' + str(self._b) + ')'

    def __eq__(self,other):
        ''' a=b '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)
     
        return self._a == other._a and self._b==other._b

    def __lt__(self,other):
        ''' a<b '''
        if self._a>=other._a and self._b<=other._b:
            return True
        else:
            return False
        
    def __gt__(self,other):
        ''' a>b '''
        if self._a<=other._a and self._b>=other._b:
            return True
        else:
            return False

    def __add__(self,other):
        ''' a+b '''
        assert isinstance(self, Interval)
        assert isinstance(other, Interval)

        if self == other:
            return self

        if self._b<=other._a or self._a>=other._b:
            return[self, other]

        if self<other:
            return other
        if self>other:
            return self
        
        return Interval(min(self._a, other._a), max(self._b, other._b))

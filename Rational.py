from fractions import Fraction
import math

class Rational(object):
    def __init__(self, numer, denom):
        '''
        num: numerator
        den: denominator
        '''
        assert isinstance(numer, int)
        assert isinstance(denom, int)
        assert denom
        if not numer % denom:
            self.n = int(numer/denom)
            self.d = 1
        else:
            self.n = numer
            self.d = denom
            
    def __repr__(self):
        ''' return '''
        if self.d == 1:
            return str(self.n)
        return str(self.n)+'/'+str(self.d)

    def __rtruediv__(self, other):
        ''' / '''
        assert isinstance(other, int)
        return Rational(self.d*other, self.n)

    def __truediv__(self, other):
        assert isinstance(other, int)
        return Rational(self.n, self.d*other)
    
    def __float__(self):
        '''float'''
        return self.n/self.d

    def __int__(self):
        '''int'''
        return int(self.n/self.d)
    
    def __mul__(self, other):
        ''' * '''
        assert isinstance(other, int) or isinstance(other, Rational)
        if isinstance(other, int):
            return Rational(self.n*other, self.d)
        else:
            return Rational(other.n*self.n, other.d*self.d)

    def __sub__(self, other):
        ''' - '''
        assert isinstance(other, Rational)
        frac = Fraction(self.n, self.d) - Fraction(other.n, other.d)
        return Rational(frac.numerator, frac.denominator)
    def __eq__(self, other):
        '''eq'''
        assert isinstance(other, int) or isinstance(other, Rational)
        return self.n == other.n and self.d == other.d
        
    def __neg__(self):
        ''' - '''
        return Rational(-self.n, self.d)

    def __lt__(self, other):
        ''' < '''
        return self.n/self.d < other.n/other.d

    def __add__(self, other):
        ''' + '''
        frac = Fraction(self.n, self.d) + Fraction(other.n, other.d)
        return Rational(frac.numerator, frac.denominator)

def square_root_rational(x,abs_tol=Rational(1,1000)):
    '''write a function square_root_rational which takes an input rational number x and returns the square root of x to absolute precision abs_tol'''
    assert isinstance(x, Rational) and isinstance(abs_tol, Rational)
    assert x.d
    assert x.n/x.d>0
    num = x.n/x.d
    precision = str(abs_tol.n/abs_tol.d)
    npre = len(precision.split('.')[1])
    string = "{:."+str(npre)+"f}"
    fmt = float(string.format(math.sqrt(num)))
    frac = Fraction(fmt)
    return Rational(frac.numerator, frac.denominator)

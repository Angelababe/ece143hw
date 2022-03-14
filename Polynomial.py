from collections import defaultdict
class Polynomial(object):
    
    def __init__(self, dic):
        '''init'''
        assert isinstance(dic, dict)
        self.max = 0
        for d in dic:
            assert isinstance(d, int) and d>=0 and isinstance(dic[d], int)
            self.max = max(self.max, d)
        self.dic = defaultdict(int)
        for d in dic:
            self.dic[d] = dic[d]

    def __repr__(self):
        '''repr'''
        ret = ''
        for d in sorted(self.dic.keys()):
            if self.dic[d] == 0:
                continue
            else:
                coef = self.dic[d]
                if coef >= 0:
                    ret += "+"
                else:
                    ret += "-"
                if not abs(coef) == 1 or d == 0:
                    ret += str(abs(self.dic[d]))
                if d == 0:
                    pass
                elif d == 1:
                    ret += "x"
                else:
                    ret += "x^({})".format(d)

        if ret[0] == "+":
            ret = ret[1:]
        return ret

    def __mul__(self, other):
        '''mul'''
        assert isinstance(other, Polynomial) or isinstance(other, int)
        temp = defaultdict(int)
        if type(other) == int:
            for d in self.dic:
                temp[d] = self.dic[d]*other
            return Polynomial(temp)
        else:
            for i in self.dic:
                for j in other.dic:
                    temp[i+j] += self.dic[i]*other.dic[j]
            return Polynomial(temp)

    def __rmul__(self, other):
        '''mul'''
        assert isinstance(other, int)
        temp = defaultdict(int)
        for d in self.dic:
            temp[d] = self.dic[d]*other
        return Polynomial(temp)

    def __add__(self, other):
        '''mul'''
        assert isinstance(other, Polynomial) or isinstance(other, int)
        temp = self.dic.copy()
        if type(other) == int:
            for d in self.dic:
                if d == 0:
                    temp[d] = self.dic[0]+other
                else:
                    temp[d] = self.dic[d]
            return Polynomial(temp)
        else:
            for d in other.dic:
                temp[d] += other.dic[d]
            return Polynomial(temp)

    def __sub__(self, other):
        '''mul'''
        assert isinstance(other, Polynomial) or isinstance(other, int)
        temp = self.dic.copy()
        if type(other) == int:
            temp[0] -= other
            return Polynomial(temp)
        else:
            for d in other.dic:
                temp[d] -= other.dic[d]
            return Polynomial(temp)

    def subs(self, num):
        '''mul'''
        assert isinstance(num, int)
        ret = 0
        for d in self.dic:
            ret+=pow(num, d) * self.dic[d]
        return ret

    def __eq__(self, other):
        '''mul'''
        assert isinstance(other, Polynomial) or isinstance(other, int)
        if type(other) == int:
            ret = False
            for d in self.dic:
                if d and self.dic[d]:
                    return False
            return self.dic[0] == other
        else:
            if not self.max == other.max:
                return False
            for i in range(self.max+1):
                if not self.dic[i] == other.dic[i]:
                    return False
            return True

    def __neg__(self):
        temp = self.dic.copy()
        for t in temp:
            temp[t] = -temp[t]
        return Polynomial(temp)

    def __truediv__(self, other):
        '''mul'''
        assert isinstance(other, Polynomial) or (isinstance(other, int) and other)
        temp = defaultdict(int)
        if type(other) == int:
            for d in self.dic:
                temp[d] = self.dic[d]/other
                if temp[d]%1:
                    raise NotImplementedError
                temp[d] = int(temp[d])
            return Polynomial(temp)
        else:
            if self.max<other.max:
                raise NotImplementedError
            copy = self.dic.copy()
            for i in reversed(range(other.max, self.max+1)):
                diff = self.dic[i]/other.dic[other.max]
                if diff%1:
                    self.dic = copy
                    raise NotImplementedError
                for j in reversed(range(other.max)):
                    self.dic[i-other.max+j] -= other.dic[j]*diff
                    if i==other.max:
                        if self.dic[i-other.max+j]:
                            self.dic = copy
                            raise NotImplementedError
                temp[i-other.max] = int(diff)
            
            self.dic = copy    
            return Polynomial(temp)

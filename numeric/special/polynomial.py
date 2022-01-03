from numeric.expression import Number, Expression

class Polynomial():
    def __init__(self, vals):
        self.vals = vals
        for x in list(self.vals.keys()):
            if not self.vals[x]:
                del self.vals[x]
        
    @staticmethod
    def _cast(obj):
        if isinstance(obj, Polynomial):
            return obj
        else:
            if isinstance(obj, Expression):
                return Polynomial(vals={0:obj})
            else:
                return Polynomial(vals={0:Number(obj)})
        
    def __radd__(self, other):
        # due to symmetry
        return self + other
    def __add__(self, other):
        other = Polynomial._cast(other)
        m = {}
        for x in self.vals:
            m[x] = self.vals[x]
        for x in other.vals:
            if x in m:
                m[x] = m[x] + other.vals[x]
            else:
                m[x] = other.vals[x]
        return Polynomial(m)
        
    def __rsub__(self,other):
        return (-self) + other
    def __sub__(self,other):
        return self + (-other)
    
    def __neg__(self):
        m = {x : -self.vals[x] for x in self.vals}
        return Polynomial(m)
    
    def __rmul__(self, other):
        # due to symmetry
        return self.__mul__(other)
    def __mul__(self, other):
        other = Polynomial._cast(other)
        m = {}
        for x1 in self.vals:
            for x2 in other.vals:
                if x1+x2 in m:
                    m[x1+x2] = m[x1+x2] + self.vals[x1]*other.vals[x2]
                else:
                    m[x1+x2] = self.vals[x1]*other.vals[x2]
        return Polynomial(m)
                    
    def __truediv__(self, other):
        m = {x : self.vals[x]/other for x in self.vals}
        return Polynomial(m)
        
    def simplify(self):
        m = {}
        for x in self.vals:
            m[x] = self.vals[x].simplify()
        return Polynomial(m)
        
    def eval(self, x):
        s = None
        for i in self.vals:
            if s:
                s = s + self.vals[i]*x**i
            else:
                s = self.vals[i]*x**i
        return s if s else 0
        
    def __str__(self):
        s = None
        for x,y in self.vals.items():
            if not s:
                s = ''
            else:
                s += '+' if y.value() > 0 else ' '
            if not x:
                s += str(y)
            else:
                s += ('%s x%s' % ((y if (y - 1) else ''), ('^{%d}' % x) if x > 1 else ''))
        return s if s else ''
#        return ' + '.join([('%s x%s' % ((y if (y - 1) else ''), ('^{%d}' % x) if x > 1 else '')) if x else str(y) for x,y in self.vals.items()])
        
x = Polynomial(vals={1:Number(1)})

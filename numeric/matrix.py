class Matrix():

    @staticmethod
    def _det(m):
        if len(m) == 2:
            return m[0][0]*m[1][1] - m[0][1]*m[1][0]
        d = None
        for i in range(0, len(m[0])):
            if m[0][i]:
                expr = Matrix._det([ m[c][:i] + m[c][i+1:] for c in range(1, len(m))]) * m[0][i]
                if d:
                    if not i % 2:
                        d = d + expr
                    else:
                        d = d - expr
                else:
                    if not i % 2:
                        d = expr
                    else:
                        d = - expr
            
        if not d:
            d = m[0][0]
            
        return d

    def __init__(self, m):
        self._m = m

    def __getitem__(self, key):
         return self._m[key]
        
    def __abs__(self):
        return Matrix._det(self._m)
        
    def __str__(self):
        return r'\begin{pmatrix}' + r' \\ '.join([' & '.join([str(v) for v in r]) for r in self._m]) + r'\end{pmatrix}'
    
    def minor(self, i, j):
        return Matrix([self._m[c][:i] + self._m[c][i+1:] for c in range(0, j)] + 
                      [self._m[c][:i] + self._m[c][i+1:] for c in range(j + 1, len(self._m))])
        
    def adjugate(self):
        return Matrix([
            [((-1) if ((i + j) % 2) else 1)*abs(self.minor(i, j)) for j in range(0, len(self._m[0]))]
                for i in range(0, len(self._m))])

    def __pow__(self, other):
        if other == -1:
            return self.inverse()
            
    def map(self, f):
        return Matrix([[f(v) for v in r] for r in self._m])
        
    def __mul__(self, other):
    #TODO rewrite this shit
        if isinstance(other, Matrix):
            m = [
                [None for j in range(0, len(other._m[0]))]  
                for i in range(0, len(self._m))
            ]
            for i in range(0, len(self._m)):
                for j in range(0, len(other._m[0])):
                    for c in range(0, len(self._m[0])):
                        if m[i][j]:
                            m[i][j] = m[i][j] + self._m[i][c] * other._m[c][j]
                        else:
                            m[i][j] = self._m[i][c] * other._m[c][j]
            return Matrix(m)



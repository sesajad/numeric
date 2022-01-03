from numexpr import *
from numexpr.math import sqrt
#fixed point

iterexpr = lambda x : sqrt(8/(x+6))
x_0 = Number(1.5, name='x_0')

print('\\[ x_0 = 1.5 \\]')

def fixed(x, level=1):
    xn = iterexpr(x)
    print('\\[', 'x_{%d}' % level, '=', xn.simplify(4) ,'\\]')
    print('\\[ \\rightarrow ', 'x_{%d}' % level, '=', xn.simplify(2) ,'\\]')
    print('\\[ \\rightarrow ', 'x_{%d}' % level, '=', xn.simplify(0) ,'\\]')
    if level < 3:
        fixed(xn.simplify(), level + 1)


fixed(x_0)

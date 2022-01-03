from numexpr import *
from numexpr.math import sin, cos, e
#scant method
min = -5
max = -3

expr = lambda x : 2*sin(x) - e**x/4 - 1
iterexpr = lambda x : x - (2*sin(x) - e**x/4 - 1)/(2*cos(x) - e**x/4)
x_0 = Number(-4, name='x_0')

print('\\[ x_0 = -4 \\]')

def newtonraphsone(x, level=1):
    xn = iterexpr(x)
    print('\\[', 'x_{%d}' % level, '=', xn.simplify(4) ,'\\]')
    print('\\[ \\rightarrow ', 'x_{%d}' % level, '=', xn.simplify(2) ,'\\]')
    print('\\[ \\rightarrow ', 'x_{%d}' % level, '=', xn.simplify(0) ,'\\]')
    print('\\[ E \simeq |x_{%d}-x_{%d}|' % (level, level - 1), '=', abs(xn-x).simplify(), '\\]')
    if abs(xn-x).value() > 0.001:
        newtonraphsone(xn.simplify(), level + 1)



newtonraphsone(x_0)

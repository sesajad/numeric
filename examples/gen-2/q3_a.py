from numexpr import *
from numexpr.math import sin, e
#bisection
min = -5
max = -3

expr = lambda x : 2*sin(x) - e**x/4 - 1

print('\\[ f(x) = ', expr(Number(1, name='x')) , ' \\]\n\n')

print('\\[ \\begin{cases} ')
x_min = Number(min, name='x_{\\text{min}}')
t_expr = expr(x_min)
print('f(x_\\text{min})  = ', t_expr, '=', t_expr.simplify(0))
print('\\\\')
x_max = Number(max, name='x_{\\text{max}}')
t_expr = expr(x_max)
print('f(x_\\text{max})  = ', t_expr, '=', t_expr.simplify(0))
print('\\end{cases} \\]\n\n')

def bisection(min, max, level=1):
    mid = (min + max) / 2
    if (abs(max - min)/2 <= 0.001):
        return
    print('\\[ x \\in [%s, %s] \\]' % (min, max))
    x = Number(mid, name='x_{%d}' % level)
    print('\\[',x , '=', x.simplify(), ' \\rightarrow ', 'f(x_{%d})' % level, '=', expr(x) ,'\\]')
    print('\\[ \\rightarrow ', 'f(x_{%d})' % level, '=', expr(x).simplify(2) ,'\\]')
    print('\\[ \\rightarrow ', 'f(x_{%d})' % level, '=', expr(x).simplify(0) ,'\\]')
    if expr(x).value()*expr(min).value() > 0:
        bisection(x.value(), max, level + 1)
    else:
        bisection(min, x.value(), level + 1)


bisection(min, max)

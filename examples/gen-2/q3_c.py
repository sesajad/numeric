from numexpr import *
from numexpr.math import sin, e
#scant method
min = -5
max = -3

expr = lambda x : 2*sin(x) - e**x/4 - 1

print('\\[ f(x) = ', expr(Number(1, name='x')) , ' \\]\n\n')

print('\\[ \\begin{cases} ')
x_min = Number(min, name='x_{\\text{min}}')
t_expr = expr(x_min)
print('f(x_\\text{min})  = ', t_expr, '=' , t_expr.simplify(2), '=', t_expr.simplify(0))
print('\\\\')
x_max = Number(max, name='x_{\\text{max}}')
t_expr = expr(x_max)
print('f(x_\\text{max})  = ', t_expr, '=' , t_expr.simplify(2), '=', t_expr.simplify(0))
print('\\end{cases} \\]\n\n')

def scant(a, b, level=1):
    if (abs(b - a).value()/2 <= 0.001):
        return
    print('\\[ x_{%d} \\in [%s, %s] \\]' % (level, a if a.value() < b.value() else b, b if a.value() < b.value() else a))
    x = b - (b - a)/(expr(b).simplify() - expr(a).simplify())*expr(b).simplify()
    print('\\[', x , '=', x.simplify(), '\\]')
    print('\\[ \\rightarrow ', 'x_{%d}' % level, '=', x.simplify(2) ,'\\]')
    print('\\[ \\rightarrow ', 'x_{%d}' % level, '=', x.simplify(0) ,'\\]')
    print('\\[ f(x_{%d})' % level, '=', expr(x.simplify()) ,'\\]')
    print('\\[ \\rightarrow ', 'f(x_{%d})' % level, '=', expr(x.simplify()).simplify(2) ,'\\]')
    print('\\[ \\rightarrow ', 'f(x_{%d})' % level, '=', expr(x.simplify()).simplify(0) ,'\\]')
    scant(b.simplify(), x.simplify(), level + 1)



scant(x_min, x_max)

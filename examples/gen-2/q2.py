from numexpr import *
xi = Number(1.0, name='x_i')
expr = xi - (2*xi**3 + xi - 5)*(6*xi**2 + 1)/(24*xi**4 + 6*xi**2 + 30*xi + 1)
print('\\[', expr, '\\]\n\n\n')
x = []
x.append(Number(1.5, name='x_0'))
for i in [0, 1]:
    expr = x[i] - (2*x[i]**3 + x[i] - 5)*(6*x[i]**2 + 1)/(24*x[i]**4 + 6*x[i]**2 + 30*x[i] + 1)
    print('\\[ x_%d = ' % (i+1), expr, ' \\]')
    expr = expr.simplify(6)
    print('\\[ x_%d = ' % (i+1), expr, ' \\]')
    expr = expr.simplify(4)
    print('\\[ x_%d = ' % (i+1), expr, ' \\]')
    expr = expr.simplify(2)
    print('\\[ x_%d = ' % (i+1), expr, ' \\]')
    expr = expr.simplify(0)
    x.append(Number(expr.value(), exact = expr.exact(), name='x_%d' % (i+1)))
    print('\\[ x_%d = ' % (i+1), expr, ' \\]')

from sympy import *


x = Symbol('x')

raw_data = [('12','64.5'), ('24','100.4'), ('36','129'), ('48', '151.5'), ('60', '168')]

flat = []
for d in raw_data:
    plat = d[1]
    for p in raw_data:
        if p != d:
            plat += '\\left(\\frac{x-%s}{%s-%s}\\right)' % (p[0], d[0], p[0])
    flat += [plat]
    
print('f(x) = & ', ' + \\\\ & '.join(flat))

symdata = [(
    Number(x[0],1), 
    Number(x[1],1)) for x in raw_data]

fexpr = 0
for d in symdata:
    pexpr = d[1]
    for p in symdata:
        if p != d:
            pexpr *= (x-p[0])/(d[0]-p[0])
    fexpr += pexpr
    
# TODO needs cleaning
print(latex(fexpr))
    
fexpr = []
for d in symdata:
    pexpr = d[1]
    for p in symdata:
        if p != d:
            pexpr *= (x-p[0])/(d[0]-p[0])
    fexpr += [latex(expand(pexpr).n(2))]
    
print('f(x) = & ', ' + \\\\ & '.join(fexpr))
    
fexpr = 0
for d in symdata:
    pexpr = d[1]
    for p in symdata:
        if p != d:
            pexpr *= (x-p[0])/(d[0]-p[0])
    fexpr += pexpr
    
print(latex(simplify(expand(fexpr)).n(2)))
    

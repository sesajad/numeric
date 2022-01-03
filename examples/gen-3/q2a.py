from math import factorial
from numeric.expression import *
from numeric.special.polynomial import *

raw_data = [(0.5,269.12), (1.5,170.19), (2.5,164.83), (3.5, 183.21), (4.5, 192.99)]

c = [Number(y) for x,y in raw_data]
l = [Number(x) for x,y in raw_data]

def diff(f,x):
    n = len(x) - len(f)
    df = []
    for i in range(1,len(f)):
        df += [((f[i] - f[i-1])/(x[i+n]-x[i-1])).simplify()]
    return df

ended = False
cs = [ c ]
while not ended:
    c = diff(c, l)
    cs += [c]
    ended = True
    for b in c:
        if b:
            ended = False

print('''\\[ \\begin{array}{r|l|l|l|l|l|l}
x & f & 2nd & 3rd & 4th & 5th \\\\ \\hline''')
s = ''
for i in range(0,len(l)):
    s += str(l[i]) + ' & ' + ' & '.join(['' if i < j else str(cs[j][i-j]) for j in range(0, len(cs))]) + ' \\\\ \n '

print(s)
print('\\]')

p = Polynomial._cast(0)
print('\\[ P_{%d}(x) = ' % (len(cs)-1))
for i in range(0, len(cs) - 1):
    a = Polynomial._cast(cs[i][0])
    print('\\frac{%s}{%d!}' % (a, i))
    a = a / factorial(i)
    for j in range(0,i):
        print('(', (x-Polynomial._cast(l[j])) ,')')
        a = a*(x-Polynomial._cast(l[j]))
    
    p = p + a
    if i < len(cs)-2:
        print(' + \\\\ &')
print('\\]')


print('\\[ P_{%d}(x) = ' % (len(cs)-1))
print(p.simplify())
print('\\]')


print('\\[ P_{%d}(5) = ' % (len(cs)-1))
print(p.simplify().eval(5) ,' = ', p.simplify().eval(5).simplify(2), ' = ',p.simplify().eval(5).simplify(),' \\]')


print('now Lagrange method for $2$')

print('''\\[ 
\\begin{split}
f(x) = & ''')

fexprs = []
for d in raw_data:
    print(d[1])
    pexpr = d[1]
    for p in raw_data:
        if p != d:
            print('\\left(', ((x-p[0])/(d[0]-p[0])).simplify(), '\\right)')
            pexpr = pexpr*(x-p[0])/(d[0]-p[0])
    print(' + \\\\ & ')
    fexprs += [pexpr]
print('\\end{split} \\]')


print('''\\[ 
\\begin{split}
f(x) = & ''')

f = 0
for p in fexprs:
    f = f + p
    print(p.simplify(), ' \\\\ &')

print('\\end{split} \\]')

print('\\[ f(x) = ', f.simplify(), '\\]')



print('\\[ f(2) = ')
print(f.simplify().eval(2) ,' = ', f.simplify().eval(2).simplify(2), ' = ',f.simplify().eval(2).simplify(),' \\]')


from numeric.special.polynomial import *

raw_data = [(12,64.5), (24,100.4), (36,129), (48, 151.5), (60, 168)]

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

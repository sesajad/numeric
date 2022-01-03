from math import factorial
from numeric.expression import *
from numeric.special.polynomial import *

raw_data = [(-1,269.12), (-.5,170.19), (0,164.83), (3.5, 183.21), (4.5, 192.99)]

c = [Number(y) for x,y in raw_data]
l = [Number(x) for x,y in raw_data]

def diff(f,x):
    n = len(x) - len(f)
    df = []
    for i in range(1,len(f)):
        df += [((f[i] - f[i-1])).simplify()]
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

print('\\[ \\begin{array}{r|', '|'.join(len(cs)*'l'), '}')
print('x & ', ' & '.join([str(_+1) for _ in range(0,len(cs))]), '\\\\ \\hline')

s = ''
for i in range(0,len(l)):
    s += str(l[i]) + ' & ' + ' & '.join(['' if i < j else str(cs[j][i-j]) for j in range(0, len(cs))]) + ' \\\\ \n '

print(s)
print('\\]')

p = Polynomial._cast(0)
print('\n\n \\[ \\begin{split} P_{%d}(x) = & ' % (len(cs)-1))
for i in range(0, len(cs) - 1):
    a = Polynomial._cast(cs[i][0])
    print('\\frac{%s}{%d!}' % (a, i))
    a = a / factorial(i)
    for j in range(0,i):
        print('(', (x-Polynomial._cast(l[j])) ,')')
        a = a*(x-Polynomial._cast(l[j]))
    
    p = p + a
    if i < len(cs)-2:
        print(' + \\\\ & ')
print('\\end{split} \\]')


print('\\[ P_{%d}(x) = ' % (len(cs)-1))
print(p.simplify())
print('\\]')


print('\\subsubsection{Newton Backward Method}\n\n')

c = [Number(y) for x,y in raw_data]
l = [Number(x) for x,y in raw_data]

ended = False
cs = [ c ]
while not ended:
    c = diff(c, l)
    cs += [c]
    ended = True
    for b in c:
        if b:
            ended = False

print('\\[ \\begin{array}{r|', '|'.join(len(cs)*'l'), '}')
print('x & ', ' & '.join([str(_+1) for _ in range(0,len(cs))]), '\\\\ \\hline')

s = ''
for i in range(0,len(l)):
    s += str(l[i]) + ' & ' + ' & '.join(['' if i >=len(cs[j]) else str(cs[j][i]) for j in range(0, len(cs))]) + ' \\\\ \n '

print(s)
print('\\]')

p = Polynomial._cast(0)
print('\n\n \\[ \\begin{split} P_{%d}(x) = & ' % (len(cs)-1))
for i in range(0, len(cs) - 1):
    a = Polynomial._cast(cs[i][-1])
    print('\\frac{%s}{%d!}' % (a, i))
    a = a / factorial(i)
    for j in range(0,i):
        print('(', (x-Polynomial._cast(l[-1-j])) ,')')
        a = a*(x-Polynomial._cast(l[-1-j]))
    
    p = p + a
    if i < len(cs)-2:
        print(' + \\\\ & ')
print('\\end{split} \\]')


print('\\[ P_{%d}(x) = ' % (len(cs)-1))
print(p.simplify())
print('\\]')

print('\\subsubsection{Newton Central Forward Method}\n\n')

c = [Number(y) for x,y in raw_data]
l = [Number(x) for x,y in raw_data]

ended = False
cs = [ c ]
while not ended:
    c = diff(c, l)
    cs += [c]
    ended = True
    for b in c:
        if b:
            ended = False

print('\\[ \\begin{array}{r|', '|'.join(len(cs)*'l'), '}')
print('x & ', ' & '.join([str(_+1) for _ in range(0,len(cs))]), '\\\\ \\hline')

s = ''
for i in range(0, 2*len(l)-1):
    if not (i % 2):
        s += str(l[i//2])
    s += ' & '
    for j in range(0, len(cs)):
        if not (i-j) % 2:
            if (i-j)//2 >= 0 and (i-j)//2 < len(cs[j]):
                s += str(cs[j][(i-j)//2])
        if j < len(cs) - 1:
            s += ' & '
    s += ' \\\\ \n '

print(s)
print('\\]')

p = Polynomial._cast(0)
print('\n\n \\[ \\begin{split} P_{%d}(x) = & ' % (len(cs)-1))
for i in range(0, len(cs) - 1):
    a = Polynomial._cast(cs[i][(len(l)-i)//2])
    print('\\frac{%s}{%d!}' % (a, i))
    a = a / factorial(i)
    for j in range(0,i):
        print('(', (x-Polynomial._cast(l[len(l)//2 + (-1 if not j % 2 else +1)*((j+1)//2) ])) ,')')
        a = a*(x-Polynomial._cast(l[len(l)//2 + (-1 if not j % 2 else +1)*((j+1)//2) ]))
    
    p = p + a
    if i < len(cs)-2:
        print(' + \\\\ & ')
print('\\end{split} \\]')


print('\\[ P_{%d}(x) = ' % (len(cs)-1))
print(p.simplify())
print('\\]')


print('\\subsubsection{Newton Central Backward Method}\n\n')

c = [Number(y) for x,y in raw_data]
l = [Number(x) for x,y in raw_data]

ended = False
cs = [ c ]
while not ended:
    c = diff(c, l)
    cs += [c]
    ended = True
    for b in c:
        if b:
            ended = False

print('\\[ \\begin{array}{r|', '|'.join(len(cs)*'l'), '}')
print('x & ', ' & '.join([str(_+1) for _ in range(0,len(cs))]), '\\\\ \\hline')

s = ''
for i in range(0, 2*len(l)-1):
    if not (i % 2):
        s += str(l[i//2])
    s += ' & '
    for j in range(0, len(cs)):
        if not (i-j) % 2:
            if (i-j)//2 >= 0 and (i-j)//2 < len(cs[j]):
                s += str(cs[j][(i-j)//2])
        if j < len(cs) - 1:
            s += ' & '
    s += ' \\\\ \n '

print(s)
print('\\]')

p = Polynomial._cast(0)
print('\n\n \\[ \\begin{split} P_{%d}(x) = & ' % (len(cs)-1))
for i in range(0, len(cs) - 1):
    a = Polynomial._cast(cs[i][(len(l)-i-1)//2])
    print('\\frac{%s}{%d!}' % (a, i))
    a = a / factorial(i)
    for j in range(0,i):
        print('(', (x-Polynomial._cast(l[len(l)//2 + (1 if not j % 2 else -1)*((j+1)//2) ])) ,')')
        a = a*(x-Polynomial._cast(l[len(l)//2 + (1 if not j % 2 else -1)*((j+1)//2) ]))
    
    p = p + a
    if i < len(cs)-2:
        print(' + \\\\ & ')
print('\\end{split} \\]')


print('\\[ P_{%d}(x) = ' % (len(cs)-1))
print(p.simplify())
print('\\]')

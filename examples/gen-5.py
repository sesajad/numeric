LANG = 'en'

inf = {
    'en': {
        'author': r'''Seyed Sajad Kahani'''
        }
}

title = r'''Numerical Methods - HW5'''

_= r'''
\documentclass{article}
\usepackage{fullpage}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{physics}
\renewcommand\thesubsection{\thesection.\alph{subsection}}
\newcommand{\sn}[2]{\ensuremath{{0.#1}{\times}10^{#2}}}

'''

_+= r'''
\title{%s}
\author{%s}
''' % (title, inf[LANG]['author'])

## Q1

_+= r'''
\begin{document}
\maketitle
\section{}
'''

from numeric.system import System
from math import nan
from numeric.math import sqrt
from numeric.expression import Number

System.digits = 4
#r = 3
h = Number(50, name='h')
Q0 = Number(50, name='Q_0')

q1expr = lambda Q : 0.75 - Q*(3/100)

_+= r'''
\[ Q' = %s  \]
''' % (q1expr(Number(nan, name=r'Q')))

q1a = h + q1expr(Q0)*h
_+= r'''
\subsection{Euler's Method}
\[ Q(50) = %s = %s \]''' % (q1a, q1a.simplify())

k = []
k.append(h*q1expr(Q0))
k.append(h*q1expr(Q0 + Number(k[0].value(), name='k_1')))
_+= r'''
\subsection{2nd order Runge-Kutta’s Method}
\[ \begin{cases}
k_1 = %s = %s \\
k_2 = %s = %s
\end{cases} \]''' % (k[0], k[0].simplify(), k[1], k[1].simplify())

ya = Q0 + (k[0].simplify() + k[1].simplify())/2

_+= r'''
\[ \rightarrow Q(50) = %s = %s \]
''' % (ya, ya.simplify())


kl = []
k = lambda x : Number(kl[x-1].value(), name='k_%d' % x)
kl.append(h*q1expr(Q0))
kl.append(h*q1expr(Q0 + k(1)/2))
kl.append(h*q1expr(Q0 + 2*k(2) - k(1)))

_+= (r'''
\subsection{3nd order Runge-Kutta’s Method}
\[ \begin{cases} ''' + r'\\'.join([('k_%d' % (i+1)) + ' = %s = %s' for i in range(0, len(kl))]) +
'''\end{cases} \]''') % tuple((kl[i//2].simplify() if i % 2 else kl[i//2] for i in range(0, 2*len(kl))))

yb = Q0 + (k(1) + 4*k(2) + k(3))/6
_+= r'''
\[ \rightarrow Q(50) = %s = %s \]
''' % (yb, yb.simplify())


kl = []
k = lambda x : Number(kl[x-1].value(), name='k_%d' % x)
kl.append(h*q1expr(Q0))
kl.append(h*q1expr(Q0 + k(1)/2))
kl.append(h*q1expr(Q0 + k(2)/2))
kl.append(h*q1expr(Q0 + k(3)))

_+= (r'''
\subsection{4nd order Runge-Kutta’s Method}
\[ \begin{cases} ''' + r'\\'.join([('k_%d' % (i+1)) + ' = %s = %s' for i in range(0, len(kl))]) +
'''\end{cases} \]''') % tuple((kl[i//2].simplify() if i % 2 else kl[i//2] for i in range(0, 2*len(kl))))

yc = Q0 + (k(1) + 2*k(2) + 2*k(3) + k(4))/6
_+= r'''
\[ \rightarrow Q(50) \simeq %s = %s \]
''' % (yc, yc.simplify())

from numeric.math import exp

q1s = lambda t : 25 + 25*exp(-(3*t)/100)

_+= r'''
\subsection{Exact value}
\[ Q(t) = %s \]
\[ \rightarrow Q(50) = %s = %s \]
''' % (q1s(Number(nan, name='t')), q1s(h.simplify()), q1s(h).simplify())

_+= r'''
error of Euler's Method
\[ \rightarrow \delta(Q(50)) = %s = %s \]
''' % (abs(q1s(h).simplify() - q1a.simplify())/q1s(h).simplify(),
    (abs(q1s(h).simplify() - q1a.simplify())/q1s(h).simplify()).simplify() )

_+= r'''
error of 2nd order Runge-Kutta’s Method
\[ \rightarrow \delta(Q(50)) = %s = %s \]
''' % (abs(q1s(h).simplify() - ya.simplify())/q1s(h).simplify(),
    (abs(q1s(h).simplify() - ya.simplify())/q1s(h).simplify()).simplify() )

_+= r'''
error of 3nd order Runge-Kutta’s Method
\[ \rightarrow \delta(Q(50)) = %s = %s \]
''' % (abs(q1s(h).simplify() - yb.simplify())/q1s(h).simplify(),
    (abs(q1s(h).simplify() - yb.simplify())/q1s(h).simplify()).simplify() )

_+= r'''
error of 4nd order Runge-Kutta’s Method
\[ \rightarrow \delta(Q(50)) = %s = %s \]
''' % (abs(q1s(h).simplify() - yc.simplify())/q1s(h).simplify(),
    (abs(q1s(h).simplify() - yc.simplify())/q1s(h).simplify()).simplify() )

## Q2

_+= r'''
\section{}
'''
h = Number(0.3, name='h')
q2expr = lambda v : 10 - v/4.5

_+= r'''
\[ v' = %s \]
\subsection{3rd Adams-Multon’s Method}
now calculating $v_i$s
''' % q2expr(Number(nan, name='v'))

v0 = Number(20, name='v_0')
_+= r'''
\[ v_0 = %s \]
\[ \rightarrow f_0 = %s = %s \]
''' % (v0.simplify(), q2expr(v0), q2expr(v0).simplify())

vl = [v0]
v = lambda i : Number(vl[i].value(), name='v_%d' % (i % len(vl)) )
f = lambda i : Number(q2expr(vl[i]).value(), name='f_%d'  % (i % len(vl)) )
for c in range(1, 3):
    _+= r'''
        for $v_%d$ we have
    ''' % c
    kl = []
    k = lambda x : Number(kl[x-1].value(), name='k_%d' % x)
    kl.append(h*q2expr(v(-1)))
    kl.append(h*q2expr(v(-1) + k(1)/2))
    kl.append(h*q2expr(v(-1) + k(2)/2))
    kl.append(h*q2expr(v(-1) + k(3)))

    _+= (r'''
    \[ \begin{cases} ''' + r'\\'.join([('k_%d' % (i+1)) + ' = %s = %s' for i in range(0, len(kl))]) +
    '''\end{cases} \]''') % tuple((kl[i//2].simplify() if i % 2 else kl[i//2] for i in range(0, 2*len(kl))))

    vl.append(v(-1) + (k(1) + 2*k(2) + 2*k(3) + k(4))/6)
    _+= r'''
    \[ \rightarrow %s = %s = %s \]
    ''' % (v(-1), vl[-1], v(-1).simplify())
    _+= r'''
    \[ \rightarrow f_%d = %s = %s \]
    ''' % (c, q2expr(v(-1)), q2expr(v(-1)).simplify())

v3s = v(-1) + h/12*(23*f(-1) - 16*f(-2) + 5*f(-3) )
f3s = q2expr(Number(v3s.value(), name='v_3*'))
_+= r'''
\[ v_3* = %s = %s \]
\[ \rightarrow f_3* = %s = %s \]
''' % (v3s, v3s.simplify(), f3s, f3s.simplify())

v3 = v(-1) + h/12*(5*f3s.simplify() + 8*f(-1) - f(-2))

_+= r'''
\[ v(%s) \simeq v_3 = %s = %s \]
''' % ((3*h).simplify(), v3, v3.simplify())

_+= r'''
\subsection{3rd Adams-Bashforth's Method}
we know that answer using Adams-Bashforth's Method is equal to $v_3*$
\[ v(%s) \simeq v_3* = %s \]
''' % ((3*h).simplify(), v3s.simplify())


_+= r'''
\subsection{4th Adams-Multon's Method}
as we calculated $v_2$ before, we just need to calcuate $v_3$
'''

c = 3

_+= r'''
    for $v_%d$ we have
''' % c
kl = []
k = lambda x : Number(kl[x-1].value(), name='k_%d' % x)
kl.append(h*q2expr(v(-1)))
kl.append(h*q2expr(v(-1) + k(1)/2))
kl.append(h*q2expr(v(-1) + k(2)/2))
kl.append(h*q2expr(v(-1) + k(3)))

_+= (r'''
\[ \begin{cases} ''' + r'\\'.join([('k_%d' % (i+1)) + ' = %s = %s' for i in range(0, len(kl))]) +
'''\end{cases} \]''') % tuple((kl[i//2].simplify() if i % 2 else kl[i//2] for i in range(0, 2*len(kl))))

vl.append(v(-1) + (k(1) + 2*k(2) + 2*k(3) + k(4))/6)
_+= r'''
\[ \rightarrow %s = %s = %s \]
''' % (v(-1), vl[-1], v(-1).simplify())
_+= r'''
\[ \rightarrow f_%d = %s = %s \]
''' % (c, q2expr(v(-1)), q2expr(v(-1)).simplify())


v4s = v(-1) + h/24*(55*f(-1) - 59*f(-2) + 37*f(-3) - 9*f(-4))
f4s = q2expr(Number(v3s.value(), name='v_4*'))
_+= r'''
\[ v_4* = %s = %s \]
\[ \rightarrow f_4* = %s = %s \]
''' % (v4s, v4s.simplify(), f4s, f4s.simplify())

v4 = v(-1) + h/24*(9*f4s.simplify() + 19*f(-1) - 5*f(-2) + f(-3))

_+= r'''
\[ v(%s) \simeq v_4 = %s = %s \]
''' % ((4*h).simplify(), v4, v4.simplify())

from numeric.math import exp, e

t = Number(nan, name='t')
q2dexpr = lambda t : (45 - (45 - v0)*exp(-t/4.5))
_+= r'''
\subsection{absolute value}
\[ v(t) = %s \]
\[ \rightarrow v(%s) = %s = %s \]
\[ E(v(%s)) = %s = %s \]
\[ \rightarrow v(%s) = %s = %s \]
\[ E(v(%s)) = %s = %s \]
''' %  ( q2dexpr(t),
    (3*h).simplify(),
    q2dexpr(3*h.simplify()),
    q2dexpr(3*h.simplify()).simplify(),
    (3*h).simplify(),
    abs(q2dexpr(3*h.simplify()).simplify() - v3.simplify()),
    abs(q2dexpr(3*h.simplify()).simplify() - v3.simplify()).simplify(),
    (4*h).simplify(),
    q2dexpr(4*h.simplify()),
    q2dexpr(4*h.simplify()).simplify(),
    (4*h).simplify(),
    abs(q2dexpr(4*h.simplify()).simplify() - v4.simplify()),
    abs(q2dexpr(4*h.simplify()).simplify() - v4.simplify()).simplify(), )

## Q3

System.digits = 4

_+= r'''
\section{}
\[ \begin{cases}
\dv{Q}{t} = i \\
\dv{i}{t} = \frac{1}{L} ( -iR - \frac{Q}{C} )
\end{cases}
\]
'''

h = Number(0.001, name='h')

R = Number(300, name='R')
L = Number(0.2, name='L')
C = Number(10*10**(-6), name='C')

x0 = [Number(3*10**-4, name='Q_0'), Number(0)]

_+= r'''
\[ Q_0 = %s, i_0 = %s \]
''' % (x0[0], x0[1])

fq = lambda Q, i : i
fi = lambda Q, i : Number(1, name='1')/L * (-i*R - Q/C)


k = lambda x : [Number(_x.value(), name='k_%d' % x) for _x in fl[x-1]]

f = [fq, fi]
fl = [tuple(_(*x0)*h for _ in f)]
fl.append(tuple(_(*[_x0 + ki/Number(2, name='2') for _x0, ki in zip(x0, k(1))])*h for _ in f))
fl.append(tuple(_(*[_x0 + ki/Number(2, name='2') for _x0, ki in zip(x0, k(2))])*h for _ in f))
fl.append(tuple(_(*[_x0 + ki for _x0, ki in zip(x0, k(3))])*h for _ in f))
_+= r'''
\[
\begin{array}{c|c|c}
i & k_{Q_i} & k_{i_i} \\ \hline
%s
\end{array} \]
''' % r' \\ '.join([' & '.join([str(i+1)] + ['%s = %s' % (_x, _x.simplify()) for _x in _f]) for i, _f in enumerate(fl)])

xn = [x0[i] + (k(0)[i] + 2*k(1)[i] + 2*k(2)[i] + k(3)[i])/6 for i in range(0, len(x0))]

_+= r'''
\[ \begin{cases}
Q(%s) = %s = %s \\
i(%s) = %s = %s
\end{cases}
\]
''' % (h.simplify(), xn[0], xn[0].simplify(),
    h.simplify(), xn[1], xn[1].simplify())

q3s = lambda t : 0.0006*exp(-500*t) - 0.0003*exp(-1000*t)

_+= r'''
now solving equation to calcuate exact value
\[ Q(t) = %s \]
\[ \rightarrow Q(%s) = %s = %s \]
''' % (q3s(Number(nan, name='t')), h.simplify(), q3s(h.simplify()), q3s(h.simplify()).simplify())



_+= r'''
\end{document}
'''

print(_)

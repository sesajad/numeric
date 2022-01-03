LANG = 'en'

inf = {
    'en': {
        'author': r'''Seyed Sajad Kahani'''
        }
}

title = r'''Numerical Methods - HW4'''

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

_+= r'''
\begin{document}
\maketitle
\section{}
'''
from math import nan
from numeric.math import sqrt
from numeric.expression import Number

q1expr = lambda x : Number(1,name='1')/sqrt(x)
h = 0.1

_+= r'''
\subsection{rectangular method}
\[ f(\rho) %s \]
''' % q1expr(Number(nan, name=r'\rho'))

_+= r'''
\[
\begin{array}{c|c|c}
\rho & f(\rho) & f(\rho) h
\\ \hline '''

i = 2.0
s = 0
while i < 2.7:
    x = Number(i)
    _+= r'''
 %s & %s & %s \\''' % (x, q1expr(x).simplify(), (q1expr(x)*h).simplify())
    s = s + (q1expr(x)*h).simplify()
    i += h

_+= r'''
\end{array}
\]
'''
_+= r'''
\[ \sum f(\rho) h = %s \]
''' %  s.simplify()

_+= r'''
\subsection{midpoint method}

\[
\begin{array}{c|c|c}
\rho & f(\rho) & f(\rho) h
\\ \hline '''

i = 2.0 + h/2
s = 0
while i < 2.7:
    x = Number(i)
    _+= r'''
 %s & %s & %s \\''' % (x, q1expr(x).simplify(), (q1expr(x)*h).simplify())
    s = s + (q1expr(x)*h).simplify()
    i += h

_+= r'''
\end{array}
\]
'''
_+= r'''
\[ \sum f(\rho) h = %s \]
''' %  s.simplify()


_+= r'''
\subsection{trapezoidal method}

\[
\begin{array}{c|c|c|c}
\rho & f(\rho) & f(\rho+h) & \frac{f(\rho)+f(\rho+h)}{2} h
\\ \hline '''

i = 2.0
s = 0
while i < 2.7:
    x = Number(i)
    _+= r'''
 %s & %s & %s & %s \\''' % (x, q1expr(x).simplify(), q1expr(x+h).simplify(), ((q1expr(x) + q1expr(x+h))/2*h).simplify())
    s = s + ((q1expr(x) + q1expr(x+h))/2*h).simplify()
    i += h

_+= r'''
\end{array}
\]
'''
_+= r'''
\[ \sum \frac{f(\rho)+f(\rho+h)}{2} h = %s \]
''' %  s.simplify()

_+= r'''
\subsection{simpson method}

\[ \int_2^{2.7} f(\rho) \dd{\rho} = \int_2^{2.4} f(\rho) \dd{\rho} + \int_{2.4}^{2.7} f(\rho) \dd{\rho} \]
'''

q1d1expr = (h*Number(1,name='1')/Number(3, name='3'))*(q1expr(Number(2.0)) + Number(4,name='4')*q1expr(Number(2.1))+ Number(2, name='2')*q1expr(Number(2.2)) + Number(4, name='4')*q1expr(Number(2.3))  + q1expr(Number(2.4)))
_+= r'''
\[ \int_2^{2.4} f(\rho) \dd{\rho} \simeq \]
\[ %s \]
\[ = %s \]

''' % ( q1d1expr, q1d1expr.simplify() )

q1d2expr = (h*Number(3,name='3')/Number(8, name='8'))*(q1expr(Number(2.4)) + Number(3,name='3')*q1expr(Number(2.5))+ Number(3, name='3')*q1expr(Number(2.6)) + Number(1, name='1')*q1expr(Number(2.7)))
_+= r'''
\begin{align*} \int_2^{2.4} f(\rho) \dd{\rho} &\simeq %s \\ &= %s
\end{align*}
''' % ( q1d2expr, q1d2expr.simplify() )

_+= r'''
\[ \int_2^{2.7} f(\rho) \dd{\rho} \simeq %s = %s \]
''' %  ((q1d1expr + q1d2expr).simplify(1), (q1d1expr + q1d2expr).simplify())

_+= r'''
\subsection{exact}
\[ \int_2^{2.7} f(\rho) \dd{\rho} = 2 (\sqrt{2.7} - \sqrt{2.0})  \simeq %s  \]''' % (2*(sqrt(Number(2.7)) - sqrt(Number(2.0)))).simplify()

_+= r'''
\section{}
'''

import sympy

x = sympy.var('x')
q2sexpr = x*sympy.sin(x)

_+= r'''
\[ f''(x) = (%s)'' = (%s)' = %s \]
''' % (sympy.latex(q2sexpr), sympy.latex(sympy.diff(q2sexpr)), sympy.latex(sympy.diff(sympy.diff(q2sexpr))))

from numeric.system import System
from numeric.math import sin, cos
System.digits = 9
x = Number(4)
_+= r'''
\subsection{}
\[ f''(4) = %s = %s \]
''' % ((-x*sin(x) + 2*cos(x)), (-x*sin(x) + 2*cos(x)).simplify())

anses = []
hs = [Number(0.02, name='h_1'), Number(0.01, name='h_2')]
for h in hs:
    _+= r'''
    \subsection{}
    \[ f''_i = \frac{-f_{i+2} + 16f_{i+1} - 30f_i + 16f_{i-1} - f_{i-2}}{12h^2} \]
    '''
    q2expr = lambda x : x*sin(x)
    fs = [q2expr(Number(4, name='4') + Number(i, name=str(i))*h) for i in [-2, -1, 0, 1, 2]]
    _+= r'''
    \[ \begin{cases}
    '''
    for i, f in enumerate(fs):
        _+= r'''
            f_{i%+d} = %s = %s \\
        ''' % (2-i, f, f.simplify())
    _+= r''' \end{cases} \]
    '''
    ans = (-fs[4].simplify() + Number(16, name='16')*fs[3].simplify() - Number(30, name='30')*fs[2].simplify() + Number(16, name='16')*fs[1].simplify() - fs[0].simplify())/(Number(12, name='12')*h*h)

    _+= r'''
    \[ f'(4) = %s = %s \]
    ''' % (ans.simplify(3), ans.simplify())
    anses.append(ans.simplify())

_+= r'''
\subsection{}
\[ G = \frac{(\frac{h_1}{h_2})^p g(h_2) - g(h_1)}{(\frac{h_1}{h_2})^p - 1} \]
\[ G = %s = %s \]
''' % ((16 * anses[1] - anses[0])/(15), ((16 * anses[1] - anses[0])/(15)).simplify())


System.digits = 5
_+= r'''
\section{}
\subsection{}
\[ \int_0^2 \sin(3x) \dd x = \int_{-1}^1 \sin(3x + 3) \dd x \]
'''
q3expr = lambda x : sin(Number(3, name='3')*x + Number(3, name='3'))
_+= r'''
as we know Gauss-Legendre for three points will have following weights
\footnote{brought from https://pomax.github.io/bezierinfo/legendre-gauss.html}
\[ \begin{array}{c|c} x_i & w_i \\ \hline
0.8888888888888888 & 0.0000000000000000 \\
0.5555555555555556 & -0.7745966692414834 \\
0.5555555555555556 & .7745966692414834
\end{array}
\]'''

_+= r'''
calculating
\[
\sum w_i f(x_i)
\]
\[ \begin{array}{c|c||c} x_i & w_i & w_i f(x_i) \\ \hline
'''

wx = [(0.8888888888888888, 0.0000000000000000), (0.5555555555555556, -0.7745966692414834), (0.5555555555555556, 0.7745966692414834)]
s = []
for w, x in wx:
    expr = w*q3expr(x)
    s += [expr.simplify()]
    _+= r''' %s & %s & %s = %s \\''' % (Number(x), Number(w), expr, expr.simplify())

_+= r'''
\end{array} \]
'''

_+= r'''
\[ \int_0^2 \sin(3x) \dd x \simeq \sum w_i f(x_i) = %s = %s \]
''' % ((s[0]+s[1]+s[2]), (s[0]+s[1]+s[2]).simplify())

_+= r'''
\subsection{}
\[ \int_0^2 xe^{-x} \dd x = \int_{-1}^1 (x+1)e^{-x-1} \dd x \]
'''

from numeric.math import exp

q3expr = lambda x : (x+Number(1, name='1'))*exp(-x-Number(1, name='1'))

_+= r'''
calculating
\[
\sum w_i f(x_i)
\]
\[ \begin{array}{c|c||c} x_i & w_i & w_i f(x_i) \\ \hline
'''

wx = [(0.8888888888888888, 0.0000000000000000), (0.5555555555555556, -0.7745966692414834), (0.5555555555555556, 0.7745966692414834)]
s = []
for w, x in wx:
    expr = w*q3expr(x)
    s += [expr.simplify()]
    _+= r''' %s & %s & %s = %s \\''' % (Number(x), Number(w), expr, expr.simplify())

_+= r'''
\end{array} \]
'''

_+= r'''
\[ \int_0^2 xe^{-x} \dd x  \simeq \sum w_i f(x_i) = %s = %s \]
''' % ((s[0]+s[1]+s[2]), (s[0]+s[1]+s[2]).simplify())

_+= r'''
\section{}
\[ \begin{array}{l|l|l|l}
h & T(h) &  & \\ \hline
'''

q4expr = lambda x : exp(-x)

hs = [1, 1/2, 1/4]
ts = []
last = []
for h in hs:
    t = q4expr(Number(0))
    x = h
    while x < 1:
        t = t + Number(2, name='2')*q4expr(Number(x))
        x += h
    t = t + q4expr(Number(1))
    t = h/Number(2, name='2')*t
    curr = [t.simplify()]
    for i, l in enumerate(last):
        curr.append((Number(4**(i+1), name='4^{%d}' % (i+1))*curr[-1].simplify() - l.simplify())/(Number(4**(i+1), name='4^{%d}' % (i+1)) - Number(1, name='1')))
    _+= r'''%s & %s %s \\''' % (Number(h), ' & '.join([str(_) for _ in curr]), '&' if h == 1 else '')
    last = curr
    ts.append(t)

_+= r'''
\end{array} \]
\[ T = %s = %s \]
''' % (curr[-1], curr[-1].simplify())

System.digits = 6

t = Number(4)
q5expr = lambda t : exp(-t)*cos(t)
_+= r'''
\section{}
'''
anses = []
h = Number(0.1, name='h')
_+= r'''
\subsection{}
\[ f''_i = \frac{-f_{i+2} + 8f_{i+1} - 8f_{i-1} + f_{i-2}}{12h} \]
'''
fs = [q5expr(Number(4, name='4') + Number(i, name=str(i))*h) for i in [-2, -1, 0, 1, 2]]
_+= r'''
\[ \begin{cases}
'''
for i, f in enumerate(fs):
    _+= r'''
        f_{i%+d} = %s = %s \\
    ''' % (2-i, f, f.simplify())
_+= r''' \end{cases} \]
'''
ans = (-fs[4].simplify() + Number(8, name='8')*fs[3].simplify() - Number(8, name='8')*fs[1].simplify() + fs[0].simplify())/(Number(12, name='12')*h)

_+= r'''
\[ V'(4) = %s = %s \]
''' % (ans.simplify(3), ans.simplify())


System.digits = 5

_+= r'''
\subsection{}
\[ \int_2^4 V(t) \dd t = \int_{-1}^{1} V(u+3) \dd u = \int_{-1}^{1} e^{-t-3} \cos(t+3) \dd u  \]
using Gauss-Legendre method weights
\[ \begin{array}{c|c} w_i & x_i \\ \hline
1.0000000000000000 & -0.5773502691896257 \\
1.0000000000000000 & 0.5773502691896257
\end{array} \]
'''


_+= r'''
calculating
\[
\sum w_i f(x_i)
\]
\[ \begin{array}{c|c||c} x_i & w_i & w_i f(x_i) \\ \hline
'''

wx = [(1.0000000000000000, -0.5773502691896257), (1.0000000000000000, 0.5773502691896257)]
s = []
for w, x in wx:
    expr = w*q5expr(x+3)
    s += [expr.simplify()]
    _+= r''' %s & %s & %s = %s \\''' % (Number(x), Number(w), expr, expr.simplify())

_+= r'''
\end{array} \]
'''

_+= r'''
\[ \int_2^4 V(t) \dd t \simeq \sum w_i f(x_i) = %s = %s \]
''' % ((s[0]+s[1]), (s[0]+s[1]).simplify())


t = sympy.var('t')
q5sexpr = sympy.exp(-t)*sympy.cos(t)


System.digits = 6

_+= r'''
\subsection{}
\[ V'(t) = %s \]
''' % sympy.latex(sympy.diff(q5sexpr))

t = Number(4, name='t')
q5cexpr = -exp(-t)*sin(t) - exp(-t)*cos(t)
_+= r'''
\[ V'(4) = %s = %s \]
\[ \rightarrow E = %s = %s \]
''' % (q5cexpr, q5cexpr.simplify(), q5cexpr.simplify() - ans.simplify(), (q5cexpr.simplify() - ans.simplify()).simplify())

_+= r'''
\[ \int V(t) \dd t = %s \]
''' % sympy.latex(sympy.integrate(q5sexpr))


System.digits = 5

q5ciexpr = lambda t : exp(-t)*sin(t)/Number(2, name='2') - exp(-t)*cos(t)/Number(2, name='2')
q5ciexpr = q5ciexpr(Number(4, name='4'))-q5ciexpr(Number(2, name='2'))

_+= r'''
\[ \int_2^4 V(t) \dd t = %s = %s \]
\[ \rightarrow E =  %s = %s \]
''' % (q5ciexpr, q5ciexpr.simplify(), q5ciexpr.simplify() - (s[0]+s[1]).simplify(), (q5ciexpr.simplify() - (s[0]+s[1]).simplify()).simplify() )

_+= r'''
\end{document}
'''

print(_)

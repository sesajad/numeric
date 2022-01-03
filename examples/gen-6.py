LANG = 'en'

inf = {
    'en': {
        'author': r'''Seyed Sajad Kahani'''
        }
}

title = r'''Numerical Methods - HW6'''

_= r'''
\documentclass[10pt]{article}
\usepackage{fullpage}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{graphicx}
\usepackage{breqn}
\renewcommand\thesubsection{\thesection.\alph{subsection}}
\newcommand{\sn}[2]{\ensuremath{{0.#1}{\times}10^{#2}}}

\DeclareMathSizes{9.8}{7}{5}{3}
\DeclareMathSizes{10.0}{7}{5}{3}
\DeclareMathSizes{10.95}{8}{6}{4}   % For size 10 text
\DeclareMathSizes{11}{9}{7}{5}      % For size 11 text
\DeclareMathSizes{12}{10}{8}{6}     % For size 12 text

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
\subsection{Inverse Matrix}
'''

from numeric.system import System
from numeric.matrix import Matrix
from math import nan
from numeric.math import sqrt
from numeric.expression import Number

System.digits = 6

m = [
[1, 0, 4, 2],
[3, 0, 0, 2],
[2, -4, 0, 1],
[-1, 1, -3, 3]
]
m = Matrix([[Number(v) for v in r] for r in m])

_+= r'''
\[ A = %s \]
''' % m

_+= r'''
\begin{dmath*}
 |A| = %s \\
 = %s
\end{dmath*}
''' % (abs(m).simplify(4), abs(m).simplify())


_+= r'''
\begin{dmath*}
 A^{-1} = %s%s \\
 = %s \\
 = %s
\end{dmath*}
''' % (1/abs(m).simplify(), m.adjugate().map(lambda x : x.simplify()), m.adjugate().map(lambda x : x.simplify()/abs(m).simplify()), m.adjugate().map(lambda x : (x/abs(m)).simplify()))

b = Matrix([[Number(10)], [Number(5)], [Number(20)], [Number(30)]])
_+= r'''
\begin{dmath*}
B = %s
\end{dmath*}
''' % b
_+= r'''
\begin{dmath*}
 X = A^{-1} B = %s %s
 = %s 
 = %s
 \end{dmath*}
''' % (m.adjugate().map(lambda x : (x/abs(m)).simplify()), b, m.adjugate().map(lambda x : (x/abs(m)).simplify()) * b, (m.adjugate().map(lambda x : (x/abs(m)).simplify()) * b).map(lambda x : x.simplify()))


_+= r'''
\subsection{Cramer's Method}
'''

for i in range(0, len(b._m)):
    ai = Matrix([r[:i] + [b[j][0]] + r[i+1:] for j, r in enumerate(m._m)])
    _+= r''' \begin{dmath*} x_%d = \frac{\left| %s \right|}{\left| %s \right|} \\ = %s \end{dmath*} 
    ''' % (i + 1, ai, m, (abs(ai)/abs(m)).simplify())

mt = m.map(lambda x : x)
bt = b.map(lambda x : x)

_+= r'''
\subsection{Gauss-Elimination Method}
\subsubsection{Forward Gauss-Elimination}
'''

_+= r'''
\begin{dmath*} %s %s \end{dmath*}
''' % (m, b)

for i in range(0, len(m._m)):
    if not m._m[i][i]:
        for j in range(i+1, len(m._m))  :
            if m._m[j][i]:
                m._m[i], m._m[j] = m._m[j], m._m[i]
                b._m[i], b._m[j] = b._m[j], b._m[i]
                _+= r''' 
                swapping rows %d and %d 
                ''' % (i + 1, j + 1)
                _+= r' \begin{dmath*} %s %s \end{dmath*} ' % (m, b)
                break
        #print("PANIC")
    _+= r'''
     devide row %d by %s
     ''' % (i + 1, m[i][i])
     
    b._m[i][0] = b._m[i][0]/m._m[i][i]        
    m._m[i] = [v/m._m[i][i] for v in m._m[i]]

     
    _+= r''' \begin{dmath*} %s %s \end{dmath*} ''' % (m, b)
    m = m.map(lambda x : x.simplify())
    b = b.map(lambda x : x.simplify())

    for j in range(i + 1, len(m._m)):
        _+= r''' 
        subtract row %d multiplied by %s from row %d \\ ''' % (i + 1, m[j][i], j + 1)
        b._m[j][0] = b._m[j][0] - m[j][i]*b[i][0]
        m._m[j] = [(v - m[j][i]*m[i][c]).simplify() for c, v in enumerate(m._m[j])]

    _+= r' \begin{dmath*} %s %s \end{dmath*} ' % (m, b)
    m = m.map(lambda x : x.simplify())
    b = b.map(lambda x : x.simplify())

_+= r' now solving backward'
for i in reversed(range(0, len(m._m) - 1)):
    for j in range(i + 1, len(m._m)):
        b._m[i][0] = (b._m[i][0] - m[i][j]*b[j][0]).simplify()
        m._m[i] = [(v - m._m[i][j]*m._m[j][c]).simplify() for c, v in enumerate(m._m[i])]

    _+= r''' \begin{dmath*} %s %s \end{dmath*}
     ''' % (m, b)
    
_+= r' \[ X = %s \] ' % b


m, b = mt, bt

_+= r'''
\subsection{Crout’s Method}
'''
mt = m.map(lambda x : x)
bt = b.map(lambda x : x)

m._m[1], m._m[2], m._m[3] = m._m[2], m._m[3], m._m[1]
b._m[1], b._m[2], b._m[3] = b._m[2], b._m[3], b._m[1]

_+= r'''
\[ A = LU = \begin{pmatrix} l_{11} & 0 & 0 & 0 \\ l_{21} & l_{22} & 0 & 0 \\ l_{31} & l_{32} & l_{33} & 0 \\ l_{41} & l_{42} & l_{43} & l_{44} \end{pmatrix} 
\begin{pmatrix} 1 & u_{12} & u_{13} & u_{14} \\ 0 & 1 & u_{23} & u_{24} \\ 0 & 0 & 1 & u{34} \\ 0 & 0 & 0 & 1 \end{pmatrix} \]

for easier decomposition we apply these swaps in $A$
\[ A = %s \]
''' % m


l = Matrix([[Number(0) for j in range(0, len(m._m[0]))] for i in range(0, len(m._m))])
u = Matrix([[Number(0) for j in range(0, len(m._m[0]))] for i in range(0, len(m._m))])

for k in range(0, len(m._m)):
	u._m[k][k] = Number(1, name='1')

for j in range(0, len(m._m)):
    for i in range(j, len(m._m)):
        s = None
        for k in range(1, j-1):
            if s:
                s = s + l._m[i][k]* u._m[k][j]
            else:
                s = l._m[i][k]* u._m[k][j]
        if s:
            l._m[i][j] = m._m[i][j] - s
        else:
            l._m[i][j] = m._m[i][j]
    for i in range(j, len(m._m)):
        s = None
        for k in range(1, j-1):
            if s:
                s = s + l._m[j][k]* u._m[k][i]
            else:
                s = l._m[j][k]* u._m[k][i]
                
        if not l._m[j][j]:
            print('shit')
    
        if s:
            u._m[j][i] = (m._m[j][i] - s) / l._m[j][j]
        else:
            u._m[j][i] = m._m[j][i] / l._m[j][j]

linverse = l.adjugate().map(lambda x : (x/abs(l)).simplify())
uinverse = u.adjugate().map(lambda x : (x/abs(u)).simplify())

_+= r'''
\[ L = %s \]
\[ U = %s \]
\[ \rightarrow y = L^{-1}b = %s \]
\[ \rightarrow x = U^{-1}y = %s \]
''' % (l.map(lambda x : x.simplify()), u.map(lambda x : x.simplify()), (linverse * b).map(lambda x : x.simplify()), (uinverse * linverse * b).map(lambda x : x.simplify()))

_+= r'''
\subsection{Jacobi Iterative Method}
'''

x = Matrix([[Number(30)], [Number(30)], [Number(30)], [Number(30)]])

_+= r'''
\[ x_{%d} = %s \]
''' % (0, x)

c = 1
while c < 5:
    for i in range(0, len(m._m)):
        s = b[i][0]
        for j in range(0, len(m._m)):
            if j != i:
                s = s - m[i][j]*(x[j][0]).simplify()
        x._m[i][0] = s / m[i][i]
        

    
    _+= r'''
        \[ x_{%d} = %s = %s \]
    ''' % (c, x, x.map(lambda x : x.simplify()))

    x = x.map(lambda x : x.simplify())
    c += 1

_+= r'''
it's completely shown that it diverges.
'''

_+= r'''
\end{document}
'''

print(_)

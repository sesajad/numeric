import math
from .expression import UnaryOperationExpression, Number
from .operations import UnaryOperator

class FunctionOperator(UnaryOperator):
    def __init__(self, func, str_format=None):
        super().__init__(1000)
        self.func = func
        self.str_format = str_format if str_format else lambda x : ((r'\text{%s}' % self.func.__name__) + '(%s)')

    def apply(self, val):
        return self.func(val)

    def str_format(self, precedence):
        return self.str_format(precedence)

import sys

special_functions = {
    'sqrt' : FunctionOperator(math.sqrt, str_format=lambda x : r'\sqrt{%s}'),
    'exp' : FunctionOperator(math.exp, str_format=lambda x : r'e^{%s}')
}

class MathWrapper:

    def __getattribute__(self, key):
        obj = math.__getattribute__(key)
        if key.startswith('__'):
            return obj
        if callable(obj):
            operator = special_functions[key] if key in special_functions else FunctionOperator(obj)
            return lambda x : UnaryOperationExpression(x, operator)
        else:
            return Number(obj, name='key')

sys.modules[__name__] = MathWrapper()
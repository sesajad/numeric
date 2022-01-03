class BinaryOperator():
    def __init__(self, precedence):
        self.precedence = precedence

    def apply(self, left, right):
        raise NotImplementedError

    def str_format(self, left_precedence, right_precedence):
        raise NotImplementedError

class StandardBinaryOperator(BinaryOperator):
    def __init__(self, name, precedence, str_format):
        super().__init__(precedence)
        self.name = name
        self.str_format = str_format

    def apply(self, left, right):
        val = left.__getattribute__('__%s__' % self.name)(right)
        if val == NotImplemented:
            return right.__getattribute__('__r%s__' % self.name)(left)
        else:
            return val

class UnaryOperator():
    def __init__(self, precedence):
        self.precedence = precedence

    def apply(self, val):
        raise NotImplementedError

    def str_format(self, precedence):
        raise NotImplementedError

class StardardUnaryOperator(UnaryOperator):
    def __init__(self, name, precedence, str_format):
        super().__init__(precedence)
        self.name = name
        self.str_format = str_format

    def apply(self, val):
        return val.__getattribute__('__%s__' % self.name)()

standard_binary_operators = [
    StandardBinaryOperator(name='add', precedence=1, str_format=lambda x, y : '%s + %s' if y > 2 else '%s + (%s)'),
    StandardBinaryOperator(name='sub', precedence=1, str_format=lambda x, y : '%s - %s' if y > 2 else '%s - (%s)'),
    StandardBinaryOperator(name='mul', precedence=3, str_format=lambda x, y : ('%s' if x >= 2 else '(%s)') + ' \\times ' + ('%s' if y > 3 else '(%s)')),
    StandardBinaryOperator(name='truediv', precedence=4, str_format=lambda x, y: '\\frac{%s}{%s}'),
    StandardBinaryOperator(name='pow', precedence=5, str_format=lambda x, y: ('{%s}' if x > 5 else '{(%s)}') + '^{%s}')
    # pow
]

standard_unary_operators = [
    StardardUnaryOperator(name='neg', precedence=2, str_format=lambda x : '-%s' if x > 2 else '-(%s)'),
    StardardUnaryOperator(name='pos', precedence=2, str_format=lambda x : '+%s' if x > 2 else '+(%s)'),
    StardardUnaryOperator(name='abs', precedence=1000, str_format=lambda x : '|%s|'),
]

from functools import partial

from .system import System
from .operations import standard_binary_operators, standard_unary_operators

class Expression():
    def __init__(self, precedence):
        self.precedence = precedence

    def depth(self):
        raise NotImplementedError()

    def value(self):
        raise NotImplementedError()

    def exact(self):
        raise NotImplementedError()

    def simplify(self, depth=None):
        if not depth:
            return Number(self.value(), self.exact())
        else:
            return self

    def __bool__(self):
        return self.value().__bool__()

class Number(Expression):
    def __init__(self, value, exact=None, name=None):
        super().__init__(1000)
        self._value = value
        self._exact = exact if exact else value
        self._name = name if name else System.str(value)

    def value(self):
        return self._value

    def exact(self):
        return self._exact

    def __str__(self):
        return self._name

class BinaryOperationExpression(Expression):
    def __init__(self, right, left, operator):
        super().__init__(operator.precedence)
        self.right = right if isinstance(right, Expression) else Number(right)
        self.left = left if isinstance(left, Expression) else Number(left)
        self.operator = operator

    def depth(self):
        return max(self.right.depth(), self.left.depth()) + 1

    def value(self):
        return System.roundoff(self.operator.apply(self.left.value(), self.right.value()))

    def exact(self):
        return self.operator.apply(self.left.exact(), self.right.exact())

    def simplify(self, depth=None):
        if depth:
            return BinaryOperationExpression(self.right.simplify(depth-1), self.left.simplify(depth-1), self.operator)
        else:
            return super().simplify(depth)

    def __str__(self):
        return self.operator.str_format(self.left.precedence, self.right.precedence) % (self.left, self.right)

class UnaryOperationExpression(Expression):
    def __init__(self, operand, operator):
        super().__init__(operator.precedence)
        self.operand = operand if isinstance(operand, Expression) else Number(operand)
        self.operator = operator

    def depth(self):
        return self.operand.depth() + 1

    def value(self):
        return System.roundoff(self.operator.apply(self.operand.value()))

    def exact(self):
        return self.operator.apply(self.operand.exact())

    def simplify(self, depth=None):
        if depth:
            return UnaryOperationExpression(self.operand.simplify(depth-1), self.operator)
        else:
            return super().simplify(depth)
    def __str__(self):
        return self.operator.str_format(self.operand.precedence) % (self.operand)


def register_operators():
    for op in standard_binary_operators:
        setattr(Expression, '__%s__' % op.name, (lambda op : lambda x, y : BinaryOperationExpression(y, x, op))(op) )
        setattr(Expression, '__r%s__' % op.name, (lambda op : lambda x, y : BinaryOperationExpression(x, y, op))(op) )

    for op in standard_unary_operators:
        setattr(Expression, '__%s__' % op.name, (lambda op : lambda x : UnaryOperationExpression(x, op))(op) )
register_operators()


def WrapperExpression(Expression):
    def __init__(self, name, expr):
        self.name = name
        self.expr = expr
        
    def depth(self):
        return self.expr.depth() + 1
        
    def value(self):
        return self.expr.value()
    
    def exact(self):
        return self.expr.exact()
        
    def simplify(self, depth=None):
        if depth > self.depth():
            return self
        else:
            return self.expr.simplify(depth)
            
    def __str__(self):
        self.name
            

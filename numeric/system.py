STORE_MANTISSA = 1
STORE_FLOATING = 2

from math import log10 as log, floor

class System():
    # TODO
    store = STORE_MANTISSA
    digits = 5
    
    
    @staticmethod
    def str(value):
        if value:
            d=floor(log(abs(value))) + 1
            return ('-' if value < 0 else '') + '\\sn{%s}{%d}' % (round(abs(value)*10**(System.digits - d)), d)
        else:
            return '0'

    @staticmethod
    def roundoff(value):
        if value:
            d=floor(log(abs(value))) + 1
            return round(value, System.digits - d)
        else:
            return 0

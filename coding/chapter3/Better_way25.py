def safe_division(number, divisor, 
                  ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:           # integer division result too large for a float
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:       # float division by zero
        if ignore_zero_division:
            return float('inf')
        else:
            raise
            
result = safe_division(1.0, 10**500, True, False)
print(result) # 0

result = safe_division(1.0, 0, False, True)
print(result) # inf


def safe_division_b(number, divisor, 
                  ignore_overflow = False,
                  ignore_zero_division = False):
    try:
        return number / divisor
    except OverflowError:           # integer division result too large for a float
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:       # float division by zero
        if ignore_zero_division:
            return float('inf')
        else:
            raise
            
result = safe_division_b(1.0, 10**500, ignore_overflow=True)
print(result) # 0

result = safe_division_b(1.0, 0, ignore_zero_division=True)
print(result) # inf

assert safe_division_b(1.0, 10**500, True, False) == 0


#-------------------------------------------------------#
def safe_division_c(number, divisor, *,
                  ignore_overflow = False,
                  ignore_zero_division = False):
    try:
        return number / divisor
    except OverflowError:           # integer division result too large for a float
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:       # float division by zero
        if ignore_zero_division:
            return float('inf')
        else:
            raise
            
# 위치 인자를 사용하면 프로그램이 제대로 작동하지 않음

# safe_division_c(1.0, 10**500, True, False)
# TypeError: safe_division_c() takes 2 positional arguments but 4 were given

result = safe_division_c(1.0, 0, ignore_zero_division=True)
assert result == float('inf')

try:
    result = safe_division_c(1.0, 0)
except ZeroDivisionError:
    pass # 예상대로 작동함

assert safe_division_c(number=2, divisor=5) == 0.4
assert safe_division_c(divisor=5, number=2) == 0.4
assert safe_division_c(2, divisor=5) == 0.4

# def safe_division_c(numerator, denominator, *,
#                   ignore_overflow = False,
#                   ignore_zero_division = False):

# ...


#-------------------------------------------------------#
def safe_division_d(number, divisor, /, *,
                  ignore_overflow = False,
                  ignore_zero_division = False):
    try:
        return number / divisor
    except OverflowError:           # integer division result too large for a float
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:       # float division by zero
        if ignore_zero_division:
            return float('inf')
        else:
            raise
            
assert safe_division_d(2, 5) == 0.4

# safe_division_d(numerator=2, denominator=5)
# TypeError: safe_division_d() got an unexpected keyword argument 'numerator'
# passed as keyword arguments: 'numerator, denominator'


#-------------------------------------------------------#
def safe_division_e(numerator, denominator, /,
                    ndigits=10, *,
                    ignore_overflow = False,
                    ignore_zero_division = False):
    try:
        fraction = numerator / denominator
        return round(fraction, ndigits)
    except OverflowError:           # integer division result too large for a float
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:       # float division by zero
        if ignore_zero_division:
            return float('inf')
        else:
            raise
            
result = safe_division_e(22, 7)
print(result) 

result = safe_division_e(22, 7, 5)
print(result) 

result = safe_division_e(22, 7, ndigits=2)
print(result)

# 3.1428571429
# 3.14286
# 3.14
import sys
print(sys.float_info.max)
print(sys.float_info.min)
from decimal import Decimal
print(Decimal.from_float(0.5))
print(Decimal.from_float(0.1))
print(Decimal.from_float(0.3))

print(12/55)
print(120//55)
print(120 % 55)
print(divmod(120,55))
print(divmod(100,55))
print(divmod(450,55))

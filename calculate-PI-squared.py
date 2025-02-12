import sys

sys.set_int_max_str_digits(2147483647)

from decimal import Decimal, getcontext
from fractions import Fraction

with open('denominator.txt', 'r') as f:  
  denominator = int(f.read().strip())

with open('numerator.txt', 'r') as f:
  numerator = int(f.read().strip())

getcontext().prec = 1000

fraction = Fraction(numerator * 6, denominator)

decimal_value = Decimal(fraction.numerator) / Decimal(fraction.denominator)

# print("============================= Happy BirthDay GitHub!!! =============================")
# print("============================= 오늘은 GitHub 출시 17주년입니다. =============================")
# print("============================= Happy BirthDay GitHub!!! =============================")

# print("\n\n")

print("==========================================================================================")
print("\n\n")

print(decimal_value)

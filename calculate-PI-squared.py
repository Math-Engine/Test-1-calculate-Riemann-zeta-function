import sys

sys.set_int_max_str_digits(2147483647)

from decimal import Decimal, getcontext
from fractions import Fraction

with open('denominator.txt', 'r') as f:  
  denominator = int(f.read().strip())

with open('numerator.txt', 'r') as f:
  numerator = int(f.read().strip())

getcontext().prec = denominator * numerator # 대충 충분히 큰 정수

fraction = Fraction(numerator * 6, denominator)

decimal_value = Decimal(fraction.numerator) / Decimal(fraction.denominator)

print("============================= Happy BirthDay GitHub!!! =============================")
print("============================= 오늘은 GitHub 출시 17주년입니다. =============================")
print("============================= Happy BirthDay GitHub!!! =============================")

print("\n\n")

print("==========================================================================================")

print(decimal_value)

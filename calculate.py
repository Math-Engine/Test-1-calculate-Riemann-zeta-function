import sys
import os

sys.set_int_max_str_digits(2147483647)

def isPrime(n):
  for i in range(2, n//2 + 1):
    if n % i == 0:
      return False
  return True

with open('max_prime_number.txt', 'r') as f:
  max_prime_number = int(f.read().strip())

with open('denominator.txt', 'r') as f:  
  denominator = int(f.read().strip())

with open('numerator.txt', 'r') as f:
  numerator = int(f.read().strip())

gap = -314
past_i = "none"
for i in range(max_prime_number + 1, max_prime_number + 101):
  gap = gap + 1
  if isPrime(i) == True:
    if gap < 0:
      gap = 0
      past_i = i
      i_square = i**2
      denominator = denominator * (i_square - 1)
      numerator = numerator * i_square
    else:
      i_square = i_square + (2 * gap * past_i) + gap**2
      gap = 0
      past_i = i
      denominator = denominator * (i_square - 1)
      numerator = numerator * i_square

console.log(numerator/denominator)

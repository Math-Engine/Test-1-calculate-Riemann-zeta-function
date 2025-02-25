import sys
import os

sys.set_int_max_str_digits(2147483647)

param = int(sys.argv[1])

# 짝수인 자연수만 연산 가능
def dividing_2(n):
  if (len(str(n)) < 16):
    return n//2
  return int(str((n * 5))[0:len(str(n * 5)) - 1])

# 3 이상의 자연수만 소수 판별 가능 
def isPrime(n):
  if (int(str(n)[-1])%2 == 1):
    for i in range(2, dividing_2(n + 1)):
      if n % i == 0:
        return False
    return True
  else:
    return False

with open('max_prime_number.txt', 'r') as f:
  max_prime_number = int(f.read().strip())

with open('denominator.txt', 'r') as f:  
  denominator = int(f.read().strip())

with open('numerator.txt', 'r') as f:
  numerator = int(f.read().strip())

gap = (param + 1) * (-1)
past_i = "none"
the_number_of_prime_numbers = 0
for i in range(max_prime_number + 1, max_prime_number + 1 + param):
  gap = gap + 1
  if isPrime(i) == True:
    the_number_of_prime_numbers = the_number_of_prime_numbers + 1
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

print(f"{numerator} / {denominator}")

with open('max_checked_number.txt', 'w') as file:
    file.write(str(max_prime_number + param))

with open('max_prime_number.txt', 'w') as file:
    file.write(str(past_i))

with open('denominator.txt', 'w') as file:
    file.write(str(denominator))

with open('numerator.txt', 'w') as file:
    file.write(str(numerator))

os.system(f'git config user.name "github-actions[bot]"')
os.system(f'git config user.email "github-actions[bot]@users.noreply.github.com"')
os.system(f'git add .')
commit_message = f"[{max_prime_number + 1} ~ {max_prime_number + param}] {the_number_of_prime_numbers}개의 소수에 대해 계산"
os.system(f'git commit --allow-empty -m "' + commit_message + '"')
os.system(f'git push')

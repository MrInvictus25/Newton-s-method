import statistics
import math
x = 3
guess = 1

while math.fabs(guess * guess - x) >= 10 ** -12:
  guess = statistics.mean([guess, x/guess])
  print(guess)
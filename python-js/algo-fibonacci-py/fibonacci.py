def fibonacci(n):
  sequence = [0, 1]
  sum = 0
  for i in range(n-1):
    sum = sequence[-1] + sequence[-2]
    sequence.append(sum)
  return sum



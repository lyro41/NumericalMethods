def P(a, x): 
  res = 0.0
  v = 1.0 
  for c in a:
    res += c * v  
    v *= x
  return res

def solve(a, x0, eps, c):
  if len(a) < 2:
    return None
  a_prime = a.copy()
  for i in range(1, len(a)):
    a_prime[i] *= i
  a_prime.pop(0)
  prev, now = x0, x0 - c * P(a, x0) / P(a_prime, x0)
  while abs(now - prev) >= eps:
    now, prev = now - c * P(a, now) / P(a_prime, now), now
  return now

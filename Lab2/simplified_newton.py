def P(a, x): 
  res = 0.0
  v = 1.0 
  for c in a:
    res += c * v  
    v *= x
  return res

def solve(a, x0, eps):
  if len(a) < 2:
    return None
  a_prime = a.copy()
  for i in range(1, len(a)):
    a_prime[i] *= i
  derivative = P(a_prime[1:], x0)
  prev, now = x0, x0 - P(a, x0) / derivative
  while abs(now - prev) >= eps:
    now, prev = now - P(a, now) / derivative, now
  return now

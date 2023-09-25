def P(a, x): 
  res = 0.0
  v = 1.0 
  for c in a:
    res += c * v  
    v *= x
  return res

def solve(a, x0, eps, delta):
  if len(a) < 2:
    return None
  derivative = (P(a, x0) - P(a, x0 - delta)) / delta
  prev, now = x0, x0 - P(a, x0) / derivative
  while abs(now - prev) >= eps:
    derivative = (P(a, now) - P(a, prev)) / (now - prev)
    now, prev = now - P(a, now) / derivative, now
  return now

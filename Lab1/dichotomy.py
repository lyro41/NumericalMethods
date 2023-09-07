def P(a, x): 
  res = 0.0
  v = 1.0 
  for c in a:
    res += c * v  
    v *= x
  return res

def solve(a, x0, x1, eps=1e-6):
  if P(a, x0) * P(a, x1) > 0:     
    return None
  L, R = x0, x1 
  if L > R:
    L, R = R, L 
  while abs(R - L) > eps:
    M = (L + R) / 2  
    if P(a, M) == 0:
      return M  
    if P(a, M) * P(a, L) < 0:
      R = M   
      continue
    L = M 
  return (L + R) / 2
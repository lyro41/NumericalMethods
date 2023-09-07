def phi(a, x):
  if x != 0:
    return 0.5 * (a / x + x)
  return 0

def sqrt(a, x0, eps=1e-6):
  x = x0
  while abs(x - phi(a, x)) > eps:
    x = phi(a, x)
  return phi(a, x)
import numpy as np

def iteration(matrix: np.array, eps):
  x0 = np.empty(matrix.shape[0]) 
  x0.fill(1)

  x1 = matrix @ x0
  lambda0 = x1[0] / x0[0]
  x1 = matrix @ x1
  lambda1 = x1[0] / x0[0]
  x0 = x1

  counter = 0
  while (abs(lambda0 - lambda1) > eps): 
    counter += 1

    x1 = matrix @ x0
    lambda0, lambda1 = lambda1, x1[0] / x0[0] 
    x0 = x1 
    if counter == 3: 
      x1 /= max([abs(elem) for elem in x1])
      counter = 0

  return lambda1

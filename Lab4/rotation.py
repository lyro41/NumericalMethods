import numpy as np

def rotation(matrix: np.array, eps):
  H = np.eye(len(matrix))
  mx = eps
  while mx >= eps:
    mx = 0
    i, j = 0, 0
    for k in range(matrix.shape[1]):
      for n in range(k):
        if n != k and abs(matrix[n][k]) >= mx:
          mx = abs(matrix[n][k])
          i, j = n, k
    
    if mx < eps:
      break

    tan = 2 * matrix[i][j] / (matrix[i][i] - matrix[j][j]) 
    sin = np.sin(np.arctan(tan) / 2)
    cos = np.cos(np.arctan(tan) / 2)

    H0 = np.eye(len(matrix))
    H0[i][i] = cos
    H0[j][j] = cos
    H0[j][i] = sin
    H0[i][j] = -sin
    H = H @ H0
    matrix = H0.T @ matrix @ H0
  return H, matrix

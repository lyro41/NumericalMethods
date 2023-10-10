import numpy as np

def gauss(matrix: np.array):
  if np.linalg.matrix_rank(matrix[:, :-1]) < np.linalg.matrix_rank(matrix):
    raise ValueError("system has no solutions")

  if np.linalg.matrix_rank(matrix) < matrix.shape[1] - 1:
    raise ValueError("system is undetermined")
  
  for i in range(matrix.shape[0]):
    matrix[i] /= matrix[i, i]
    for j in range(i + 1, matrix.shape[0], 1):
      matrix[j] -= matrix[j, i] * matrix[i]

  for i in range(matrix.shape[0] - 1, 0, -1):
    for j in range(i - 1, -1, -1):
      matrix[j] -= matrix[i] * matrix[j, i]

  return matrix[:, -1]

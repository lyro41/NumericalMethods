import numpy as np
import math
from copy import deepcopy

def simple_iteration(matrix: np.array, eps = 1e-6):
  if np.linalg.matrix_rank(matrix[:, :-1]) < np.linalg.matrix_rank(matrix):
    raise ValueError("system has no solutions")

  if np.linalg.matrix_rank(matrix) < matrix.shape[1] - 1:
    raise ValueError("system is undetermined")
  
  for k in range(matrix.shape[0]):
    max_elem = max([elem for elem in matrix[:, k]])
    max_index = np.where(matrix[:, k] == max_elem)[0][0]
    matrix[k], matrix[max_index] = matrix[max_index], matrix[k].copy()

  for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1] - 1):
      if i != j: 
        matrix[i, j] = -matrix[i, j] / matrix[i, i]
    matrix[i, matrix.shape[1] - 1] /= matrix[i, i]
    matrix[i, i] = 0

  beta = matrix[:, -1]
  x0 = np.array(beta)
  x1 = matrix[:, :-1] @ x0 + beta
  while np.max(np.abs(x1 - x0)) >= eps:
    x0 = x1
    if np.isnan(x0).any() or np.isinf(x0).any():
      raise ValueError("simple iteration diverges")
    x1 = matrix[:, :-1] @ x1 + beta
  return x1

def seidel(matrix: np.array, eps = 1e-6):
  if np.linalg.matrix_rank(matrix[:, :-1]) < np.linalg.matrix_rank(matrix):
    raise ValueError("system has no solutions")

  if np.linalg.matrix_rank(matrix) < matrix.shape[1] - 1:
    raise ValueError("system is undetermined")
  
  save = deepcopy(matrix)

  for k in range(matrix.shape[0]):
    max_elem = max([elem for elem in matrix[:, k]])
    max_index = np.where(matrix[:, k] == max_elem)[0][0]
    matrix[k], matrix[max_index] = matrix[max_index], matrix[k].copy()

  for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1] - 1):
        if i != j: 
          matrix[i, j] = -matrix[i, j] / matrix[i, i]
    matrix[i, matrix.shape[1] - 1] /= matrix[i, i]
    matrix[i, i] = 0

  beta = matrix[:, -1] 
  x1 = np.array(beta)
  x0 = x1 + 2 * eps
  while np.max(np.abs(x1 - x0)) >= eps:
    if np.isnan(x0).any() or np.isinf(x0).any():
      raise ValueError("simple iteration diverges")
    x0 = deepcopy(x1)
    for k in range(matrix.shape[0]):
      x1[k] = (matrix[k, :-1] @ x1) + beta[k]
  return x1

import unittest
import numpy as np

if __name__ == "__main__":
  import iteration as iter
  import rotation as rot
else:
  from . import iteration as iter
  from . import rotation as rot

def isSolution(solution, found, eps=1e-6):
  if len(solution) != len(found):
    return False
  for i in range(len(solution)):
    if abs(solution[i] - found[i]) > eps:
      return False
  return True

def eigenvaluesEqual(solution, found, eps=1e-6):
  for i in range(len(solution)):
    if abs(solution[i][i] - found[i][i]) > eps:
      return False
  return True

def eigenvectorsEqual(solution, found, eps=1e-6):
  for i in range(len(solution)):
    for j in range(len(solution)):
      if abs(solution[i][j] - found[i][j]) > eps:
        return False
  return True

def isEqual(solution, found, eps=1e-6):
  return abs(solution - found) <= eps

class TestIteration(unittest.TestCase):
  def test_correct(self):
    eps = 1e-3

    matrices = [
      np.array([
        [ 1,  2,  3,  4],
        [ 5,  6,  7,  8],
        [ 9, 10, 11, 12],
        [13, 14, 15, 16],
      ], dtype=float),
      np.array([
        [1, 2,  1],
        [3, 2,  1],
        [4, 3, -2]
      ], dtype=float),
      np.array([
        [3,  2, -5],
        [2, -1,  3],
        [1,  2, -1]
      ], dtype=float),
      np.array([
        [3]
      ], dtype=float),
    ]

    # solutions = [
    #   [36.2094, -2.20937, 0, 0],
    #   [4.97904, -3.06022, -0.918819],
    #   [-3.76762, None, None],
    #   [3]
    # ]

    solutions = [
      36.2094,
      4.97904,
      -3.76762,
      3
    ]

    for i in range(len(matrices)):
      result = iter.iteration(matrices[i], eps)
      self.assertTrue(isEqual(solutions[i], result, eps))

class TestRotation(unittest.TestCase):
  def test_correct(self):
    eps = 1e-3

    matrices = [
      np.array([
        [2.2,   1, 0.5,   2],
        [  1, 1.3,   2,   1],
        [0.5,   2, 0.5, 1.6],
        [  2,   1, 1.6,   2],
      ], dtype=float),
      np.array([
        [1, 2],
        [2, 3],
      ], dtype=np.float64),
      np.array([
        [3]
      ], dtype=float),
    ]

    eigenvalues = [
      [
        [5.65203,       0,        0,        0],
        [      0, 1.54542,        0,        0],
        [      0,       0, -1.42009,        0],
        [      0,       0,        0, 0.222636]
      ],
      [
        [2 - 5 ** 0.5,            0],
        [           0, 2 + 5 ** 0.5]
      ],
      [[3]]
    ]

    eigenvectors = [
      [
        [0.5317, -0.6289,  0.2220, -0.5219],
        [0.4462,  0.5726, -0.5159, -0.4549],
        [0.4088,  0.4856,  0.7573,  0.1534],
        [0.5925, -0.2018, -0.3333,  0.7051]
      ],
      [
        [0.85065,  0.5257],
        [-0.5257, 0.85065]
      ],
      [
        [1]
      ]
    ]

    for i in range(len(matrices)):
      vectors, values = rot.rotation(matrices[i], eps)
      self.assertTrue(eigenvaluesEqual(eigenvalues[i], values, eps))
      self.assertTrue(eigenvectorsEqual(eigenvectors[i], vectors, eps))


if __name__ == "__main__":
  unittest.main()

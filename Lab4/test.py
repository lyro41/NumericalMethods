import unittest
import numpy as np

import iteration as iter
import rotation as rot

def isSolution(solution, found, eps=1e-6):
  if len(solution) != len(found):
    return False
  for i in range(len(solution)):
    if abs(solution[i] - found[i]) > eps:
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


if __name__ == "__main__":
  unittest.main()

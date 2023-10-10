import unittest
import numpy as np

import gauss

def isSolution(solution, found, eps=1e-6):
  if len(solution) != len(found):
    return False
  for i in range(len(solution)):
    if abs(solution[i] - found[i]) > eps:
      return False
  return True

class TestGauss(unittest.TestCase):
  def test_correct(self):
    eps = 1e-6

    matrices = [
      np.array([
        [1, 2,  1,  8],
        [3, 2,  1, 10],
        [4, 3, -2,  4]
      ], dtype=float),
      np.array([
        [3,  2, -5, -1],
        [2, -1,  3, 13],
        [1,  2, -1,  9]
      ], dtype=float),
      np.array([
        [3, 0]
      ], dtype=float),
    ]

    solutions = [
      [1, 2, 3],
      [3, 5, 4],
      [0]
    ]

    for i in range(len(matrices)):
      self.assertTrue(isSolution(solutions[i], gauss.gauss(matrices[i]), eps))
  
  def test_undetermined(self):
    matrices = [
      np.array([
        [2, -1,  3,  -5, 1],
        [1, -1, -5,   0, 2],
        [3, -2, -2,  -5, 3],
        [7, -5, -9, -10, 8]
      ], dtype=float),
      np.array([
        [2, -1,  3,  -5, 1],
        [1, -1, -5,   0, 2]
      ], dtype=float),
      np.array([
        [2, 1, 1],
        [4, 2, 2]
      ], dtype=float),
      np.array([
        [0, 0],
      ], dtype=float),
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        gauss.gauss(matrix)
      self.assertTrue("system is undetermined" in str(context.exception))

  def test_no_solution(self):
    matrices = [
      np.array([
        [1, -1,  3],
        [1, -1, -5]
      ], dtype=float),
      np.array([
        [1, -1,  3],
        [2, -2, 7]
      ], dtype=float),
      np.array([
        [0, 1]
      ], dtype=float)
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        gauss.gauss(matrix)
      self.assertTrue("system has no solutions" in str(context.exception))

class TestGaussRectangle(unittest.TestCase):
  def test_correct(self):
    eps = 1e-6

    matrices = [
      np.array([
        [1, 2,  1,  8],
        [3, 2,  1, 10],
        [4, 3, -2,  4]
      ], dtype=float),
      np.array([
        [3,  2, -5, -1],
        [2, -1,  3, 13],
        [1,  2, -1,  9]
      ], dtype=float),
      np.array([
        [3, 0]
      ], dtype=float),
    ]

    solutions = [
      [1, 2, 3],
      [3, 5, 4],
      [0]
    ]

    for i in range(len(matrices)):
      self.assertTrue(isSolution(solutions[i], gauss.rectangle(matrices[i]), eps))
  
  def test_undetermined(self):
    matrices = [
      np.array([
        [2, -1,  3,  -5, 1],
        [1, -1, -5,   0, 2],
        [3, -2, -2,  -5, 3],
        [7, -5, -9, -10, 8]
      ], dtype=float),
      np.array([
        [2, -1,  3,  -5, 1],
        [1, -1, -5,   0, 2]
      ], dtype=float),
      np.array([
        [2, 1, 1],
        [4, 2, 2]
      ], dtype=float),
      np.array([
        [0, 0],
      ], dtype=float),
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        gauss.rectangle(matrix)
      self.assertTrue("system is undetermined" in str(context.exception))

  def test_no_solution(self):
    matrices = [
      np.array([
        [1, -1,  3],
        [1, -1, -5]
      ], dtype=float),
      np.array([
        [1, -1,  3],
        [2, -2, 7]
      ], dtype=float),
      np.array([
        [0, 1]
      ], dtype=float)
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        gauss.rectangle(matrix)
      self.assertTrue("system has no solutions" in str(context.exception))

class TestGaussMaxElem(unittest.TestCase):
  def test_correct(self):
    eps = 1e-6

    matrices = [
      np.array([
        [1, 2,  1,  8],
        [3, 2,  1, 10],
        [4, 3, -2,  4]
      ], dtype=float),
      np.array([
        [3,  2, -5, -1],
        [2, -1,  3, 13],
        [1,  2, -1,  9]
      ], dtype=float),
      np.array([
        [3, 0]
      ], dtype=float),
    ]

    solutions = [
      [1, 2, 3],
      [3, 5, 4],
      [0]
    ]

    for i in range(len(matrices)):
      self.assertTrue(isSolution(solutions[i], gauss.max_element(matrices[i]), eps))
  
  def test_undetermined(self):
    matrices = [
      np.array([
        [2, -1,  3,  -5, 1],
        [1, -1, -5,   0, 2],
        [3, -2, -2,  -5, 3],
        [7, -5, -9, -10, 8]
      ], dtype=float),
      np.array([
        [2, -1,  3,  -5, 1],
        [1, -1, -5,   0, 2]
      ], dtype=float),
      np.array([
        [2, 1, 1],
        [4, 2, 2]
      ], dtype=float),
      np.array([
        [0, 0],
      ], dtype=float),
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        gauss.max_element(matrix)
      self.assertTrue("system is undetermined" in str(context.exception))

  def test_no_solution(self):
    matrices = [
      np.array([
        [1, -1,  3],
        [1, -1, -5]
      ], dtype=float),
      np.array([
        [1, -1,  3],
        [2, -2, 7]
      ], dtype=float),
      np.array([
        [0, 1]
      ], dtype=float)
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        gauss.max_element(matrix)
      self.assertTrue("system has no solutions" in str(context.exception))


if __name__ == "__main__":
  unittest.main()

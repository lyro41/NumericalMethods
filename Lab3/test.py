import unittest
import numpy as np

if __name__ == "__main__":
  import gauss
  import simple_iteration as si
else:
  from . import gauss
  from . import simple_iteration as si

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

class TestSimpleIteration(unittest.TestCase):
  def test_correct(self):
    eps = 1e-6

    matrices = [
      np.array([
        [2, 2, 10, 14],
        [10, 2, 2, 12],
        [2, 10, 2, 13]
      ], dtype=np.float64),
      np.array([
        [1,  1, 7],
        [3, -1, 25]
      ], dtype=np.float64),
      np.array([
        [3, 0],
      ], dtype=np.float64),
    ]

    solutions = [
      [45/56, 13/14, 59/56],
      [8, -1],
      [0]
    ]

    for i in range(len(matrices)):
      result = si.simple_iteration(matrices[i], eps)
      self.assertTrue(isSolution(solutions[i], result, eps))
  
  def test_diverges(self):
    matrices = [
      np.array([
        [1, 2,  1,  8],
        [3, 2,  1, 10],
        [4, 3, -2,  4]
      ], dtype=np.float64),
      np.array([
        [3,  2, -5, -1],
        [2, -1,  3, 13],
        [1,  2, -1,  9]
      ], dtype=np.float64),
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        si.simple_iteration(matrix)
      self.assertTrue("simple iteration diverges" in str(context.exception))

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
        si.simple_iteration(matrix)
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
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        si.simple_iteration(matrix)
      self.assertTrue("system has no solutions" in str(context.exception))

class TestSeidel(unittest.TestCase):
  def test_correct(self):
    eps = 1e-3

    matrices = [
      np.array([
        [2, 2, 10, 14],
        [10, 2, 2, 12],
        [2, 10, 2, 13]
      ], dtype=np.float64),
      np.array([
        [1,  1, 7],
        [3, -1, 25]
      ], dtype=np.float64),
      np.array([
        [3, 0],
      ], dtype=np.float64),
    ]

    solutions = [
      [45/56, 13/14, 59/56],
      [8, -1],
      [0]
    ]

    for i in range(len(matrices)):
      result = si.seidel(matrices[i], eps)
      self.assertTrue(isSolution(solutions[i], result, eps))
  
  def test_diverges(self):
    matrices = [
      np.array([
        [1, 2,  1,  8],
        [3, 2,  1, 10],
        [4, 3, -2,  4]
      ], dtype=np.float64),
      np.array([
        [3,  2, -5, -1],
        [2, -1,  3, 13],
        [1,  2, -1,  9]
      ], dtype=np.float64),
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        si.simple_iteration(matrix)
      self.assertTrue("simple iteration diverges" in str(context.exception))

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
        si.seidel(matrix)
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
    ]

    for matrix in matrices:
      with self.assertRaises(ValueError) as context:
        si.seidel(matrix)
      self.assertTrue("system has no solutions" in str(context.exception))


if __name__ == "__main__":
  unittest.main()

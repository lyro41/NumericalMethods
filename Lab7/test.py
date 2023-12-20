import unittest
import numpy as np

import integral_smoothing as ism

def isEqual(solution, found, eps=1e-6):
  return abs(solution - found) <= eps

class TestRotation(unittest.TestCase):
  def test_correct(self):
    eps = 1e-3
    variables = [
      np.array([0, 1, 2, 4]),
      np.array([0, 1, 2, 3])
    ]
    values = [
      [0, 1, 4, 2],
      [0, 2, 5, 3]
    ]
    m = [
      1,
      1
    ]
    x = [
      1.5,
      1.5
    ]
    solution = [
      1.614,
      2.5
    ]
    for i in range(len(variables)):
      result = ism.integral_smoothing(vars=variables[i], vals=values[i], m=m[i], x=x[i])
      self.assertTrue(isEqual(solution[i], result, eps))


if __name__ == "__main__":
  unittest.main()

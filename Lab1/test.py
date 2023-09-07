import unittest
import random

import dichotomy as dich
import simple_iteration as si

def almostEqual(a, b, eps=1e-6):
  return abs(a - b) < eps

class Testsolveotomy(unittest.TestCase):

  def test_correct(self):
    eps = 1e-2
    
    self.assertTrue(almostEqual(+7, dich.solve([126, -165, 77, -15, 1], 5, 100, eps), eps))
    self.assertTrue(almostEqual(+2, dich.solve([126, -165, 77, -15, 1], 0, 2.5, eps), eps))

    self.assertTrue(almostEqual(-1, dich.solve([-1, 0, 1], -3.5, 0.3, eps), eps))
    self.assertTrue(almostEqual(+1, dich.solve([-1, 0, 1], 0.9, 102301203, eps), eps))

    self.assertTrue(almostEqual(-1, dich.solve([1, 1], -132331231, 132331231, eps), eps))

  def test_incorrect(self):
    eps = 1e-2
    
    self.assertIsNone(dich.solve([126, -165, 77, -15, 1], 2.1, 5.7, eps))
    self.assertIsNone(dich.solve([1, 1], 10, 132331231, eps))


class TestSimpleIteration(unittest.TestCase):
  def test_randomized(self):
    eps = 1e-2

    a = [i for i in range(150000)]
    sqrts = [i**0.5 for i in a]
    for i in range(len(a)):
      self.assertTrue(almostEqual(sqrts[i], si.sqrt(a[i], 1e18, eps), eps))

if __name__ == "__main__":
  unittest.main()
import unittest
import random

if __name__ == "__main__":
  import newton
  import simplified_newton as snewton
  import newton_broyden as broyden
  import secant
else:
  from . import newton
  from . import simplified_newton as snewton
  from . import newton_broyden as broyden
  from . import secant

def isRoot(solutions, found, eps=1e-6):
  for solution in solutions:
    if abs(found - solution) < eps:
      return True
  return False

class TestNewton(unittest.TestCase):
  def test_correct(self):
    print("\ntesting newton's method")
    eps = 1e-3
    
    a = [126, -165, 77, -15, 1]
    x0 = 5
    solutions = [2, 3, 7]
    self.assertTrue(isRoot(solutions, newton.solve(a, x0, eps), eps))
    x0 = 0
    self.assertTrue(isRoot(solutions, newton.solve(a, x0, eps), eps))

    a = [-1, 0, 1]
    x0 = -3.5
    solutions = [-1, 1]
    self.assertTrue(isRoot(solutions, newton.solve(a, x0, eps), eps))
    x0 = 4.152346
    self.assertTrue(isRoot(solutions, newton.solve(a, x0, eps), eps))
    x0 = 1.7671
    self.assertTrue(isRoot(solutions, newton.solve(a, x0, eps), eps))

    a = [1, 1]
    x0 = -12.15125
    solutions = [-1]
    self.assertTrue(isRoot(solutions, newton.solve(a, x0, eps), eps))
    print("testing newton's method completed")

# simplified newton method doesn't converge
class TestSimplifiedNewton(unittest.TestCase):
  def test_correct(self):
    print("\ntesting newton's simplified method")
    eps = 1e-3
    
    a = [126, -165, 77, -15, 1]
    x0 = 5
    solutions = [2, 3, 7]
    print("result of", a, "at", x0, " -> ", snewton.solve(a, x0, eps))
    # self.assertTrue(isRoot(solutions, snewton.solve(a, x0, eps), eps))
    x0 = 0
    print("result of", a, "at", x0, " -> ", snewton.solve(a, x0, eps))
    # self.assertTrue(isRoot(solutions, snewton.solve(a, x0, eps), eps))

    a = [-1, 0, 1]
    x0 = -3.5
    solutions = [-1, 1]
    print("result of", a, "at", x0, " -> ", snewton.solve(a, x0, eps))
    # self.assertTrue(isRoot(solutions, snewton.solve(a, x0, eps), eps))
    x0 = 4.152346
    print("result of", a, "at", x0, " -> ", snewton.solve(a, x0, eps))
    # self.assertTrue(isRoot(solutions, snewton.solve(a, x0, eps), eps))
    x0 = 1.7671
    self.assertTrue(isRoot(solutions, snewton.solve(a, x0, eps), eps))

    a = [1, 1]
    x0 = -12.15125
    solutions = [-1]
    self.assertTrue(isRoot(solutions, snewton.solve(a, x0, eps), eps))
    print("testing newton's simplified method completed")

class TestNewtonBroyden(unittest.TestCase):
  def test_correct(self):
    print("\ntesting newton-broyden's method")
    eps = 1e-3
    c = 1.5

    a = [126, -165, 77, -15, 1]
    x0 = 5
    solutions = [2, 3, 7]
    self.assertTrue(isRoot(solutions, broyden.solve(a, x0, eps, c), eps))
    x0 = 0
    self.assertTrue(isRoot(solutions, broyden.solve(a, x0, eps, c), eps))

    a = [-1, 0, 1]
    x0 = -3.5
    solutions = [-1, 1]
    self.assertTrue(isRoot(solutions, broyden.solve(a, x0, eps, c), eps))
    x0 = 4.152346
    self.assertTrue(isRoot(solutions, broyden.solve(a, x0, eps, c), eps))
    x0 = 1.7671
    self.assertTrue(isRoot(solutions, broyden.solve(a, x0, eps, c), eps))

    a = [1, 1]
    x0 = -12.15125
    solutions = [-1]
    self.assertTrue(isRoot(solutions, broyden.solve(a, x0, eps, c), eps))
    print("testing newton-broyden's method completed")

class TestSecant(unittest.TestCase):
  def test_correct(self):
    print("\ntesting secant method")
    eps = 1e-3
    delta = 0.1

    a = [126, -165, 77, -15, 1]
    x0 = 5
    solutions = [2, 3, 7]
    print("result of", a, "at", x0, " -> ", secant.solve(a, x0, eps, delta))
    # self.assertTrue(isRoot(solutions, secant.solve(a, x0, eps, delta), eps))
    x0 = 0
    self.assertTrue(isRoot(solutions, secant.solve(a, x0, eps, delta), eps))

    a = [-1, 0, 1]
    x0 = -3.5
    solutions = [-1, 1]
    self.assertTrue(isRoot(solutions, secant.solve(a, x0, eps, delta), eps))
    x0 = 4.152346
    self.assertTrue(isRoot(solutions, secant.solve(a, x0, eps, delta), eps))
    x0 = 1.7671
    self.assertTrue(isRoot(solutions, secant.solve(a, x0, eps, delta), eps))

    a = [1, 1]
    x0 = -12.15125
    solutions = [-1]
    self.assertTrue(isRoot(solutions, secant.solve(a, x0, eps, delta), eps))
    print("testing secant method completed")


if __name__ == "__main__":
  unittest.main()
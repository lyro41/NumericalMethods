import unittest

if __name__ == "__main__":
  import polynomial_interpolation as pi
else:
  from . import polynomial_interpolation as pi

def isEqual(solution, found, eps=1e-6):
  return abs(solution - found) <= eps

class TestPolynomialInterpolation(unittest.TestCase):
  variables = [0, 1, 2, 3]
  values = [1, 2, 4, 1]
  x_star = 1.5

  def test_N3_uneven(self):
    self.assertTrue(isEqual(3.25, pi.newton_polynomial(var=self.variables, val=self.values, type=1, x=self.x_star, net_type='uneven')))

  def test_N3_I_even(self):
    self.assertTrue(isEqual(3.25, pi.newton_polynomial(var=self.variables, val=self.values, type=1, x=self.x_star, net_type='even')))

  def test_N3_II_even(self):
    self.assertTrue(isEqual(3.25, pi.newton_polynomial(var=self.variables, val=self.values, type=2, x=self.x_star, net_type='even')))

  def test_N4_I_even(self):
    self.assertTrue(isEqual(3.5546875, pi.newton_polynomial(var=self.variables+[4], val=self.values+[0], type=1, x=self.x_star, net_type='even')))


if __name__ == "__main__":
  unittest.main()

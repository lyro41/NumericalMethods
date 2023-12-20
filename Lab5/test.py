import unittest

if __name__ == "__main__":
  import general_case as gc
else:
  from . import general_case as gc

def isEqual(solution, found, eps=1e-6):
  return abs(solution - found) <= eps

class TestGeneralCase(unittest.TestCase):
  variable_list = [3, 4, 5, 6]
  values_list = [1, 0, 4, 2]
  x_star = 4.5

  def test_global(self):
    self.assertTrue(isEqual(2.0625, gc.general_case(self.variable_list, self.values_list, self.x_star)))

  def test_linear_interpolation(self):
    self.assertTrue(isEqual(2.0, gc.general_case(self.variable_list[1:3], self.values_list[1:3], self.x_star)))

  def test_linear_interpolation(self):
    L1 = gc.general_case(self.variable_list[0: -1], self.values_list[0: -1], self.x_star)
    L2 = gc.general_case(self.variable_list[1:], self.values_list[1:], self.x_star)
    self.assertTrue(isEqual(2.0625, (L1 + L2) / 2))


if __name__ == "__main__":
  unittest.main()

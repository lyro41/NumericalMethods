import sys
if sys.version_info[0:2] < (3, 9):
  raise Exception("Requires python 3.9 or newer")

if __name__ == "__main__":
  import unittest
  from Lab1.test import TestDichotomy, TestSimpleIteration
  from Lab2.test import TestNewton, TestSimplifiedNewton, TestNewtonBroyden, TestSecant
  from Lab3.test import TestGauss, TestGaussRectangle, TestGaussMaxElem, TestSimpleIteration, TestSeidel
  from Lab4.test import TestIteration, TestRotation
  from Lab5.test import TestGeneralCase
  from Lab6.test import TestPolynomialInterpolation
  from Lab7.test import TestIntegralSmoothing
  unittest.main()

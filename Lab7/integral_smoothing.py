import numpy as np
import sys
from pathlib import Path

sys.path.insert(1, str(Path(__file__).resolve().parent.parent))
from Lab3.gauss import gauss

def integral_smoothing(vars: np.array, vals: np.array, m: int, x: float):
  matrix = np.zeros((m + 1, m + 2))
  for i in range(m + 1):
    row = [sum(vars ** j) for j in range(i, i + 2)]
    row.append(sum(vals * vars ** i))
    matrix[i] = np.array(row)
  
  c = gauss(matrix)
  result = 0
  for i in range(len(c)):
    result += c[i] * (x ** i)
  return result

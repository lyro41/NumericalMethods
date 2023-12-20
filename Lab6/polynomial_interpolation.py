from math import factorial

def partitioned_difference(var: list, val: list): 
  if len(var) == 2:
    return (val[1] - val[0]) / (var[1] - var[0])
  else:
    return (partitioned_difference(var = var[1:], val = val[1:]) - partitioned_difference(var = var[:-1], val = val[:-1])) / (var[-1] - var[0])
    
def finite_difference(index: int, val: list, power: int):
  if power == 1:
    return val[index+1] - val[index]
  else:
    return finite_difference(index + 1, val, power-1) - finite_difference(index, val, power - 1)

def newton_polynomial(var: list, val: list, type=None, x=None, net_type="even"):
  if net_type.lower() != "even" and net_type.lower() != "uneven":
    raise ValueError("net_type should be either even or uneven")
  
  if type != 1 and type != 2:
    raise ValueError("type should be either 1 or 2")
  elif type == 2:
    var = list(reversed(var))
    val = list(reversed(val))
  
  final_answer = val[0]
  if net_type.lower() == "uneven":
    for i in range(1, len(var)):
      x_brackets = 1
      for j in range(i):
          x_brackets *= (x - var[j])
      final_answer += partitioned_difference(var=var[:i+1], val=val[:i+1]) * x_brackets
  elif net_type.lower() == "even":
    h = var[1] - var[0]
    q0 = (x - var[0]) / h
    q = q0
    for i in range(1, len(var)):
      if i != 1:
        q *= (q0 - (i - 1))
      final_answer += finite_difference(index = 0, val=val, power=i) * q / factorial(i)

  return final_answer

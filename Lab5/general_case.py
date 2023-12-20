def general_case(x_list: list, f_list: list, x_star: float):
  diagonal_elem_mul = 1
  f_to_D_relation = 0

  for i in range(len(x_list)):
    diagonal_elem_mul *= (x_star - x_list[i])
    D = 1

    for j in range(len(x_list)):
      D *= (x_star - x_list[j]) if i == j else (x_list[i] - x_list[j])
    f_to_D_relation += f_list[i] / D

  return f_to_D_relation * diagonal_elem_mul
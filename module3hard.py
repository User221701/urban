def calculate_structure_sum(*args):
    s = 0
    for i in args:
        if isinstance(i,(int, float)):
            s = s + i
        elif isinstance(i, (list, tuple, set)):
            s = s + calculate_structure_sum(*i)
        elif isinstance(i, str):
            s = s + len(i)
        else:
            s = s + calculate_structure_sum(*i)
            s = s + calculate_structure_sum(*i.values())
    return s


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
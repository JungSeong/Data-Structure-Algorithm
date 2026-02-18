original = [[1,2], [3,4]]
shallow = original[:]
print(id(original[0]) == id(shallow[0]))

original = [[1,2], [3,4]]
deep = [[row[:] for row in shallow] for _ in range(2)]
print(deep)
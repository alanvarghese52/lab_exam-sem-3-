import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 5, 1], [2, 8, 3]])
c = np.array([[5, 2, 7], [4, 9, 5]])

d = np.multiply(a, b)
e = np.multiply(4, (np.square(b)))
f = np.divide(c, 4)

g = np.add(d, e)
h = np.subtract(g, f)

print(d)
print('-----------------')
print(e)
print('-----------------')
print(f)
print('-----------------')
print(g)
print('\n')
print('*****************')
print(h)


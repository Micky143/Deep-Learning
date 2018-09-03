import numpy as np

a = np.arange(20)
print(a)

a = np.arange(15).reshape(3,5)
print(a)

print('Shape :-',a.shape)

print('ndim :-',a.ndim)

print('dtype :-',a.dtype.name)

print('itemsize :-',a.itemsize)

print('size :-',a.size)

print(type(a))


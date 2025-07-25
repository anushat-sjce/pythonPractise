#Numpy is a python library stands for numerical python. It is open source
#Array object is : ndarray

import numpy as np

a = np.array([0,1,2,3,4])
a
print(a[0])
a[0] = 100
print(a)
print(np.__version__)
print(type(a))
a.dtype


b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
print(b[0])
print(type(b))
b.dtype

c = b
print(c, "\n")

c = np.array([20, 1, 2, 3, 4])
print(c)
c[0] = 100
c[4] = 0
print(c)

d = c[:2]
print(d)



#print even elements in the array
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr[0:10:2])

select = [0,2,3,4]
print(select)
d = c[select]
print(d)
c[select] = 10000
print(c)
c.size
c.dtype
c.ndim
c.shape



#numpy statistical functions
a = np.array([-1,1,1,-1,1])
m= a.mean()
s= a.std()
print(m, s)

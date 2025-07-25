#Vectore addition using numpy

import numpy as np
v = np.array([1,0])
u = np.array([0,1])

z = v+u
z1 = u-v
print(z)
print(z1)

# multiply by 2 or any number
x = [8,9]
xa = np.array([8,9])
product = xa * 2
print(product)


#dot product
a = np.array([5,6])
b = np.array([3,4])
c = np.dot(a,b)
print(c)


#broadcasting the array
f = [2,4,6,8,10]
g = np.array([2,4,6,8,10])
broad = g + 1
print(broad)

#universal functions
h = np.array([34,656,342,76647,2345,75767,4562])
maxi = h.max()
print(maxi)

#pi function
np.pi
i = np.array([0,np.pi/2, np.pi/4, np.pi/8])
print(i)
print(np.sin(i))

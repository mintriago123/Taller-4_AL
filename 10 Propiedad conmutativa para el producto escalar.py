#Propiedad conmutativa para el producto escalar
import numpy as np 

u = np.array ([1,2,3])
v = np.array([2,0,1])
w = np.array([-1,3,0])
k = (4)


a=  u*v
b = v*u

print (a, b)
print (a==b)
print ('La propiedad se cumple')
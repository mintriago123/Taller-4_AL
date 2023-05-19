#Propiedad distributiva para la suma escalar
import numpy as np 

u = np.array ([1,2,3])
v = np.array([2,0,1])
w = np.array([-1,3,0])
k1 = (4)
k2 = (-4)


a=  (k1 + k2) * v
b = k1 * v + k2 * v

print (a, b)
print (a==b)
print ('La propiedad se cumple')
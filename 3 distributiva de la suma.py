
#Propiedad distributiva para la suma
import numpy as np 

u = np.array ([1,2,3])
v = np.array([2,0,1])
w = np.array([-1,3,0])
k = (4)

a= k * (u + v)
b = k * u + k * v

print (a, b)
print (a==b)
print ('La propiedad se cumple')
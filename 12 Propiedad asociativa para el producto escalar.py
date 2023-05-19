# -*- coding: utf-8 -*-

#Propiedad asociativa para el producto escalar
import numpy as np 

u = np.array ([1,2,3])
v = np.array([2,0,1])
w = np.array([-1,3,0])
k = (4)



a=   k * np.dot(u, v)
b = np.dot(k * u, v)
c = np.dot(u, k * v)

print (a, b)
print (a==b==c)
print ('La propiedad se cumple')




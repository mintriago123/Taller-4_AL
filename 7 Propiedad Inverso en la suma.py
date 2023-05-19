# -*- coding: utf-8 -*-

#Propiedad Inverso en la suma

import numpy as np 

u = np.array ([1,2,3])
v = np.array([2,0,1])
w = np.array([-1,3,0])
k = (4)
neg_v = -1 * v

a= v+neg_v
b = np.array ([0,0,0])

print (a, b)
print (a==b)
print ('La propiedad se cumple')
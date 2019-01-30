import matplotlib.pyplot as plt
import numpy as np
a=int(input('Enter no of rows in a matrix:'))
b=int(input('Enter no of columns in a matrix:'))
m=[]
for i in range(a):
	l = []
	for j in range(b):
		l.append(int(input()))
	m.append(l)
print (m) 
y = np.linalg.inv(m) 
print("inverse of a entered matrix is:")
print (y)

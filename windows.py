import numpy as np
import matplotlib.pyplot as plt
def sinc(m):
	k1=[]
	for n in range(-m,m):
		x=np.sin(np.pi/4*n)/(np.pi*n)
		k1=np.append(k1,x)
	k1[m]=1/4
	return k1
def rect(m):
	k2=[]
	for n in range(0,m-1):
		x=1
		k2=np.append(k2,x)
	return k2
def tri(m):
	k3=[]
	for n in range(0,m-1):
		x1=np.abs(n-(m-1)/2)
		x=1-((2*x1)/(m-1))
		k3=np.append(k3,x)
	return k3
def ham(m):
	k4=[]
	for n in range(0,m-1):
		x=0.5-0.5*np.cos(2*np.pi*n/(m-1))
		k4=np.append(k4,x)
	return k4
def ham1(m):
	k5=[]
	for n in range(0,m-1):
		x=0.54-0.46*np.cos(2*np.pi*n/(m-1))
		k5=np.append(k5,x)
	return k5
		


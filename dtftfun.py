from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def dtft(x):
	j=cm.sqrt(-1)
	N=1000
	X=[]
	w=np.linspace(-np.pi,np.pi,N)
	for i in range(0,N):
		s=0
		for n in range(0,len(x)):
			s=s+(x[n]*np.exp(-n*w[i]*j))
		X.append(s)
	return X

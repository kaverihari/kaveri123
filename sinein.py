import numpy as np
import matplotlib.pyplot as plt
fs=int(input("enter sample frequency"))
f1=int(input("enter first frequency"))
n=int(input("enter number of samples"))
x=np.arange(n)
a=np.sin(2*np.pi*f1/fs*x)
plt.plot(x,a)
plt.xlabel("------->samples")
plt.ylabel("-------->amplitude")
plt.show()

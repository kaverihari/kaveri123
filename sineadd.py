import numpy as np
import matplotlib.pyplot as p
fs=int(input("enter sample frequency"))
f1=int(input("enter first sine wave frequency"))
f2=int(input("enter second sine wave frequency"))
n=int(input("enter number of samples"))
g=np.arange(n)
x=np.sin(2*np.pi*f1/fs*g)
p.subplot(311)
p.plot(g,x)
p.xlabel("samples")
p.ylabel("amplitude")
y=np.sin(2*nppi*f2/fs*g)
p.subplot(312)
p.plot(g,y)
p.xlabel("samples")
p.ylabel("amplitude")
c=x+y
p.subplot(313)
p.plot(g,c)
p.xlabel("samples")
p.ylabel("amplitude")
p.show()

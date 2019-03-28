from pylab import *
import numpy as np
import matplotlib.pyplot as plt
from dtftfun import dtft
from windows import sinc
from windows import rect
from windows import tri
from windows import ham
from windows import ham1
k=int(input("enter n value:"))
m=int(input("enter m value:"))
k1=sinc(k)
k2=rect(m)
k3=tri(m)
k4=ham(m)
k5=ham1(m)
k6=dtft(k1)
plt.subplot(611)
plt.stem(k1)
plt.title("sinc function")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(612)
plt.stem(k2)
plt.title("rectangular window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(613)
plt.stem(k3)
plt.title("triangular window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(614)
plt.stem(k4)
plt.title("h4")
plt.title("hamming window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(615)
plt.stem(k5)
plt.title("hamming window")
plt.xlabel("------>n")
plt.ylabel("------>w")
plt.subplot(616)
plt.stem(np.abs(k6))
plt.title("output")
plt.show()




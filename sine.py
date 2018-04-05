import matplotlib.pyplot as plt
import numpy as np
import time

Fs=8000
f =5
sample=8000
x=np.arange(sample)
y=np.sin(2*np.pi*f*x/Fs)
plt.plot(x,y)
plt.xlabel('sample(n)')
plt.xlabel('Amplitude(A)')
plt.plot(x,y)
plt.show()
	

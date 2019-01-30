import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
y1=np.sin(2*np.pi*x)
y2=np.tan(2*np.pi*x)
plt.figure(1)
plt.plot(x,y1)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.figure(2)
plt.plot(x,y2)
plt.xlabel('time')
plt.ylabel('amplitude')
y3=y1+y2
plt.figure(3)
plt.plot(x,y3)
plt.show()

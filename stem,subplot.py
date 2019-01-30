import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
y1=np.sin(2*np.pi*x)
y2=np.tan(2*np.pi*x)
plt.subplot(2,2,1)
plt.stem(x,y1)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.subplot(2,2,4)
plt.stem(x,y2)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

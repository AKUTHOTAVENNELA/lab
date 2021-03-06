import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,10,0.1)
y1=np.sin(2*np.pi*x)
y2=np.tan(2*np.pi*x)
plt.subplot(2,2,1)
plt.title('sin signal')
plt.plot(x,y1)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.subplot(2,2,4)
plt.title('tan signal')
plt.plot(x,y2)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

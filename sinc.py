import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,5,0.01)
y=np.sinc(2*np.pi*x)
plt.plot(x,y)
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()

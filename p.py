import matplotlib.pyplot as plt
import numpy as np

from collections import deque

l=float(input("Enter the inductance value: "))
c=float(input("Enter the capacitor value: "))
v=float(input("Enter the initial voltage of the capacitor: "))

w = np.sqrt(1/(l*c))
p=(2*np.pi)/w
t = np.arange(0,(3*p),p/100)
d= (v/(w*l)) * np.sin(w*t)
vc= v * np.cos(w*t)

plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.plot(t, d , label = "current in the circuit")
plt.plot(t, vc , label = "voltage across inductor")
plt.legend()
plt.show()
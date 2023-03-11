# A = B + C.
import numpy as np
import matplotlib.pyplot as plt
A0 = 2 # initial concentration of substance A
k1 = 300 # rate constant of B formation
k2 = 100 # rate constant of C formation
t=np.linspace(0,0.02,40)
B = k1/(k1+k2)*A0*(1-np.exp(t*(-k1-k2)))
C = k2/(k1+k2)*A0*(1-np.exp(t*(-k1-k2)))
A = A0*np.exp(t*(-k1-k2))
plt.plot(t,B, color = 'b')
plt.plot(t,C, color = 'r')
plt.plot(t, A, color ='g')
plt.show()
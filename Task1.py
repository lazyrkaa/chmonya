# A = B + C.
import numpy as np
import matplotlib.pyplot as plt
A0 = 2 # initial concentration of substance A
k1 = 300 # rate constant of B formation
k2 = 100 # rate constant of C formation
t=np.linspace(0,0.03,50)
B = k1/(k1+k2)*A0*(1-np.exp(t*(-k1-k2)))
C = k2/(k1+k2)*A0*(1-np.exp(t*(-k1-k2)))
A = A0*np.exp(t*(-k1-k2))
plt.title('Concentration of substances A, B and C')
plt.ylabel('Concentration')
plt.xlabel('time')
plt.plot(t, B, color = 'b', label = 'substance B')
plt.plot(t, C, color = 'r', label = 'substance C')
plt.plot(t, A, color ='g', label = 'substance A')
plt.legend(fontsize=10)

plt.show()
import numpy as np
import matplotlib.pyplot as plt

fc=100
fm=10
Am=1
Ac=2
t= np.linspace(1,1,1000)

modulating_signal= Am*np.sin(2*np.pi*fm*t)
carrrie_signal=Ac*np.sin(2*np.pi*fc*t)

am_signal= (1+modulating_signal)*carrrie_signal

plt.figure(figsize=(10,6))
plt.subplot(3,1,1)
plt.plot(t,modulating_signal)
plt.title("Modulating signal for the messaege")

plt.subplot(3,1,2)
plt.plot(t,carrrie_signal)
plt.title("Carrie signal for the wave")

plt.subplot(3,1,3)
plt.plot(t, am_signal)
plt.title("For the am signal")

plt.tight_layout()
plt.show()
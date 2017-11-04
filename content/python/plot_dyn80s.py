import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const

t, T1,T2,T5,T6 = np.genfromtxt('content/values/messungdyn80s_val.txt',unpack=True)

t *= 2
T1 = const.convert_temperature(T1,'c','K')
T2 = const.convert_temperature(T2,'c','K')
T5 = const.convert_temperature(T5,'c','K')
T6 = const.convert_temperature(T6,'c','K')


plt.subplot(1, 2, 1)
plt.plot(t, T2, 'r-', label="Messing anfang")
plt.plot(t, T1, 'b-', label="Messing ende")
plt.xlabel('t/s')
plt.ylabel('T/K')
plt.legend(loc='best')

plt.subplot(1, 2, 2)
plt.plot(t, T6, 'r-', label="Aluminium anfang")
plt.plot(t, T5, 'b-', label="Aluminium ende")
plt.xlabel('t/s')
plt.ylabel('T/K')
plt.legend(loc="best")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# in matplotlibrc leider (noch) nicht möglich
plt.savefig('build/dyn80.pdf')
# plt.savefig('build/plot.pdf')

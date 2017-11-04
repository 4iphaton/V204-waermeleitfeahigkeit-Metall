import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const

t, T1,T2,T3,T4,T5,T6,T7,T8 = np.genfromtxt('content/values/messungstatisch_val.txt',unpack=True)

t /= 2
T1 = const.convert_temperature(T1,'c','K')
T2 = const.convert_temperature(T2,'c','K')
T3 = const.convert_temperature(T3,'c','K')
T4 = const.convert_temperature(T4,'c','K')
T5 = const.convert_temperature(T5,'c','K')
T6 = const.convert_temperature(T6,'c','K')
T7 = const.convert_temperature(T7,'c','K')
T8 = const.convert_temperature(T8,'c','K')


plt.subplot(1, 2, 1)
plt.plot(t, T2, 'y-', label="T2")
plt.plot(t, T3, 'r-', label="T3")
plt.plot(t, T6, 'g-', label="T6")
plt.plot(t, T7, 'b-', label="T7")
plt.xlabel('t/s')
plt.ylabel('T/K')
plt.legend(loc='best')

plt.subplot(1, 2, 2)
plt.plot(t, T1, 'y-', label="T1")
plt.plot(t, T4, 'r-', label="T4")
plt.plot(t, T5, 'g-', label="T5")
plt.plot(t, T8, 'b-', label="T8")
plt.xlabel('t/s')
plt.ylabel('T/K')
plt.legend(loc="best")
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
# in matplotlibrc leider (noch) nicht möglich
plt.savefig('build/stat.pdf')
# plt.savefig('build/plot.pdf')

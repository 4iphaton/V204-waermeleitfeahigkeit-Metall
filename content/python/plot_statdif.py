import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const

t, T1,T2,T3,T4,T5,T6,T7,T8 = np.genfromtxt('content/values/messungstatisch_val.txt',unpack=True)

t /= 2
T1 = const.convert_temperature(T1,'c','K')
T2 = const.convert_temperature(T2,'c','K')
T7 = const.convert_temperature(T7,'c','K')
T8 = const.convert_temperature(T8,'c','K')

plt.plot(t, T2-T1, 'r-', label="T2-T1")
plt.plot(t, T7-T8, 'b-', label="T7-T8")
plt.xlabel('t/s')
plt.ylabel('T/K')
plt.legend(loc="best")
# in matplotlibrc leider (noch) nicht möglich
plt.savefig('build/statdif.pdf')
# plt.savefig('build/plot.pdf')

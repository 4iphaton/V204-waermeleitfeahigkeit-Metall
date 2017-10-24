import matplotlib.pyplot as plt
import numpy as np
import scipy.constants as const

t,T7,T8 = np.genfromtxt('../values/messungdyn200s_val.txt',unpack=True)

t *= 2
T7 = const.convert_temperature(T7,'c','K')
T8 = const.convert_temperature(T8,'c','K')

plt.plot(t, T7, 'r-', label="Edelstahl anfang")
plt.plot(t, T8, 'b-', label="Edelstahl ende")
plt.xlabel('t/s')
plt.ylabel('T/K')
plt.legend(loc="best")
# in matplotlibrc leider (noch) nicht möglich
plt.show()
# plt.savefig('build/plot.pdf')

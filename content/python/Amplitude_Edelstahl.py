# Nur lokal ausführen. Datei ist nicht in der Makefile

import numpy as np
import scipy.constants as const
from uncertainties import ufloat
import math

t,T7,T8 = np.genfromtxt('../../content/values/messungdyn200s_val.txt',unpack=True)

t *= 2
T7 = const.convert_temperature(T7,'c','K')
T8 = const.convert_temperature(T8,'c','K')

n = len(T7) # Alle Arrays haben dieselbe laenge

T1 = T8
T2 = T7
#berechnen der Minima bzw Maxima

T1max = []
T1min = []
t1max = []

i = 10
searchmax = True
T1max = []
T1min = []

while (i < (n-1)):
    while (i < (n-1)) and searchmax:
        if T1[i] >= T1[i-1] and T1[i] > T1[i+1]:
            searchmax = False
            T1max.append(T1[i])
            t1max.append(t[i])                      #merke Zeiten für periodendauer/phase
        i+=1
    while (i < (n-1)) and not searchmax:
        if T1[i] <= T1[i-1] and T1[i] < T1[i+1]:
            searchmax = True
            T1min.append(T1[i])
        i+=1

i = 10
searchmax = True
T2max = []
T2min = []
t2max = []

while (i < (n-1)):
    while (i < (n-1)) and searchmax:
        if T2[i] >= T2[i-1] and T2[i] >= T2[i+1]:
            searchmax = False
            T2max.append(T2[i])
            t2max.append(t[i])                      #merke Zeiten für periodendauer/phase
        i+=1
    while (i < (n-1)) and not searchmax:
        if T2[i] <= T2[i-1] and T2[i] <= T2[i+1]:
            searchmax = True
            T2min.append(T2[i])
        i+=1

#berechnen der Amplituden

amp1 = []
amp2 = []

n = min(len(T1max),len(T2max))

i = 1
while (i < n):
    amp1.append((T1max[i]+T1max[i-1])/2-T1min[i-1])
    i+=1

i = 1
while (i < n):
    amp2.append((T2max[i]+T2max[i-1])/2-T2min[i-1])
    i+=1

#berechnen der Mittelwerte mit Fehlern

amp1 = ufloat(np.mean(amp1),np.std(amp1))
amp2 = ufloat(np.mean(amp2),np.std(amp2))

print('Die gemittelte Amplitude für Edelstahl unbeheitzt beträgt: ',amp1,'K')
print('Die gemittelte Amplitude für Edelstahl beheitzt beträgt: ',amp2,'K')

#berechne Periodendauer delta t und der Phasenverschiebung

dt1 = []
dt2 = []
pht = []

n = min(len(t1max),len(t2max))
i=1
pht.append(t1max[0]-t2max[0])
while i < n:
    dt1.append(t1max[i]-t1max[i-1])
    dt2.append(t2max[i]-t2max[i-1])
    pht.append(t1max[i]-t2max[i])
    i+=1
dt1 = ufloat(np.mean(dt1),np.std(dt1))
dt2 = ufloat(np.mean(dt2),np.std(dt2))
pht = ufloat(np.mean(pht),np.std(pht))

print('Periodendauer der unbeheitzten Kurve: {0:.2f}'.format(dt1),'s')
print('Periodendauer der beheitzten Kurve: {0:.2f}'.format(dt2),'s')
print('Phase der Kurven: {0:.2f}'.format(pht),'s')

# Nur lokal ausführen. Datei ist nicht in der Makefile

import numpy as np
import scipy.constants as const
from uncertainties import ufloat
from uncertainties import unumpy as unp
import math

t, T1,T2,T5,T6 = np.genfromtxt('../../content/values/messungdyn80s_val.txt',unpack=True)

t *= 2
T1 = const.convert_temperature(T1,'c','K')
T2 = const.convert_temperature(T2,'c','K')
T5 = const.convert_temperature(T5,'c','K')
T6 = const.convert_temperature(T6,'c','K')

n = len(T1) # Alle Arrays haben dieselbe laenge

#berechnen der Minima bzw Maxima
i = 10
searchmax = True
T1max = []
T1min = []
t1max = []

while (i < (n-1)):
    while (i < (n-1)) and searchmax:
        if T1[i] >= T1[i-1] and T1[i] >= T1[i+1]:
            searchmax = False
            T1max.append(T1[i])
            t1max.append(t[i])
        i+=1
    while (i < (n-1)) and not searchmax:
        if T1[i] <= T1[i-1] and T1[i] <= T1[i+1]:
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
            t2max.append(t[i])
        i+=1
    while (i < (n-1)) and not searchmax:
        if T2[i] <= T2[i-1] and T2[i] <= T2[i+1]:
            searchmax = True
            T2min.append(T2[i])
        i+=1

#berechnen der Amplituden

amp1 = []
amp2 = []

n = len(T1max)

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

print('Die gemittelte Amplitude für Messing unbeheitzt beträgt: ',amp1,'K')
print('Die gemittelte Amplitude für Messing beheitzt beträgt: ',amp2,'K')

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

#berechnung der Wärmeleitfähigkeit
def kappa(roh,c,dx,dt,Ab,Aub):
    return roh*c*(dx**2)/(2*dt*(unp.log(Ab)-unp.log(Aub)))
print('Die Wärmeleitfähigkeit beträgt: {0:.2f}'.format(kappa(8520,385,0.0303,pht,amp2,amp1)),'W/(mK)')
print('Frequenz: {0:.4}'.format(1/(dt2)),'Hz Wellenlänge: {0:.4f}'.format(0.0303*dt2/(pht)),'m')

print(T2max, T2min,T1max,T1min, t1max, t2max)

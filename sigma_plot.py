# для каждого изотопа нужно изменять параметры p,M,ishare,T

import numpy
import matplotlib.pyplot as plt
import copy


f = open('27Al(n,p).txt', 'r')
V = 2.5*10**(-6)
Na = 6.022*10**23
M = 26.98*10**(-3)
p = 2698.9
ishare = 1
T=9.435
decconst = numpy.log(2)/(T*60)         #подставить период полураспада в знаменатель
r = 0.0015
t = numpy.arange(0,18001,1)
fi = 4*10**5/(4*numpy.pi*r**2)
print('decay constant:', decconst)
mas = []
x = []
y = []
for line in f:
    mas = line.split()
    for e in range(mas.__len__()):
        mas[e] = mas[e][:8] + 'e' + mas[e][8:]
        # print(mas[e])
        if e % 2 == 0:
            x.append(float(mas[e]))
        else:
            y.append(float(mas[e]))

# print(x, end="\n\n")
# print(y)
plt.figure(1)
plt.plot(x[:-2],  y[:-2])
plt.xlabel('E, eV')
plt.ylabel('barns')
plt.title('sigma')


Nya = V*p*Na*ishare/M
print('Number of nucleus:', Nya)
Sigma = []
for e in range(y.__len__()):
    Sigma.append(y[e]*Nya)
    # print(Sigma[e])
xint = numpy.arange(0, 20000000, 500000)


yint = numpy.interp(xint, x, y)
plt.figure(2)
plt.plot(xint,yint)
plt.xlabel('E, eV')
plt.ylabel('barns')
plt.title('sigma INTERPOLATED')


sigact = (yint[numpy.where(xint == 14000000)])
print('Activation cross-section at 14 MeV:', sigact)


def a(z):
    t = copy.deepcopy(z)
    A = []
    for i in range(t.__len__()):
        A.append(fi*sigact*V*(1-numpy.exp(-decconst*t[i])))
    return A


A = a(t)
plt.figure(3)
plt.plot(t, A)
plt.xlabel('t, s')
plt.ylabel('becquerel')
plt.title('Activity')
plt.show()










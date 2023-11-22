from pylab import linspace, pi
from numpy import sqrt
T=1
RT=6.38E6
G=6.67E-11
M=5.98E24
RaI= int(500000)
RpI= int(500000)
alfa1= (RaI+RpI)/2
print (alfa1)
T1=sqrt((4*pi**2*(RT+alfa1)**3)/(G*M))/60
print (T1)
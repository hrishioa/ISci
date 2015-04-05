from numpy import *
import matplotlib.pyplot as plt

#Constants
k = float(2) #Hooke's constant
startY = -2 #starting Y(X in equations) value, measured from the center
timestep = 0.001 #timestep in seconds
duration = 2 #duration in seconds
m = 2.5 #mass of whatever's moving

getForce = lambda x: -1*k*float(x)
getAccel = lambda x: getForce(x)/m

def getDistance(x,time,speed):
	return ((speed*time)+(0.5*getAccel(x)*(time**2)))

def getdeltaV(x,time):
	return (getAccel(x)*time)

print "Program running..."

x = .25
v = 0

xVal = []
yVal = []
vVal = []
aVal = []

for i in range(1,10000):
	a = getAccel(x)

	xVal.append(i*timestep)

	yVal.append(x)
	vVal.append(v)
	aVal.append(a)
	print "X: "+str(x)+", v: "+str(v)+", F: "+str(getForce(x))+", Accel: "+str(getAccel(x))+", Distance: "+str(getDistance(x,timestep,v))
	x+=getDistance(x,timestep,v)
	v+=getdeltaV(x,timestep)

plt.plot(xVal,yVal,vVal,aVal)
plt.show()
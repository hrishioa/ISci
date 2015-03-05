from pylab import *
from numpy import *

##############################################################################################
print("Program Running...")

mass = 1 
K = 1
omegaD = 0.1
vDamp = 0.0

#basic status operations

calcForce = lambda x: (-(2/pi)) if (x>0) else ((2/pi) if (x<0) else 0)

calcDamping = lambda vNow: vNow*vDamp

old_calcForce = lambda x: (-1)*K*x

calcAccel = lambda F: F/mass

calcDeltaV = lambda aNow,delT: aNow*delT

calcDeltaX = lambda vNow,aNow,delT: vNow*delT + 0.5*aNow*delT**2

calcZ = lambda T: sin(omegaD*T)

##### Initial conditions #####
initX = 0
initV = 1

vNow = initV
xNow = initX
timeNow = 0


##### Time handling ##### 
totalTime = 5*2*pi #Total time to simulate
N = 10000 # Number of simulation steps (more = more accuracy)
delT = totalTime/N  #Time for each time step

##### Arrays to store time points and associated x values #####
tSteps = []
xSteps = []
vSteps = []

old_vNow = initV
old_xNow = initX    

old_xSteps = []
old_vSteps = []

fSteps = []
old_fSteps = []

vError = []
xError = []


##### main "for" loop - do N steps if simulation #####
for step in range(1,N): 

    fSteps.append(calcForce(xNow))
    old_fSteps.append(old_calcForce(old_xNow))

    aNow = calcAccel(calcForce(xNow)-calcDamping(vNow))   # calculate acceleration at point x        
    old_aNow = calcAccel(old_calcForce(old_xNow)-calcDamping(old_vNow))

    old_xNow = old_xNow + calcDeltaX(old_vNow,old_aNow,delT)
    old_vNow = old_vNow + calcDeltaV(old_aNow,delT)

    xNow = xNow + calcDeltaX(vNow,aNow,delT)   # update x (location)
    vNow = vNow + calcDeltaV(aNow,delT)   # update velocity
    timeNow = timeNow+delT    # update time
    
    tSteps.append(timeNow)    # store current time for plotting
    xSteps.append(xNow)       # store current location for plotting
    vSteps.append(vNow)
    old_xSteps.append(old_xNow)
    old_vSteps.append(old_vNow)

    vError.append(abs(vNow-old_vNow))
    xError.append(abs(xNow-old_xNow))


##### See what you have done here ######
plot(tSteps,xSteps)
plot(tSteps,vSteps)
show()    

plot(tSteps,vError)
plot(tSteps,xError)
show()

plot(tSteps,vSteps)
plot(tSteps,old_vSteps)
show()

plot(tSteps,fSteps)
plot(tSteps,old_fSteps)
show()
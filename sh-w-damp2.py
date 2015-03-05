from pylab import *
from numpy import *

##############################################################################################
print("Program Running...")

###Program Constants
mass = 1
K = 1
omegaD = 0.1 
omegaD_0 = 0 #when this value is not zero, omegaD will be the multiple of omega0 by this amount - only valid if showOldPlot==1
vDamp = 0.000 #Dampening coeff
showOldPlot=1 #Value of 1 will simulate and display the oscillator without driving it 
totalTime = 10*2*pi #Total time to simulate
N = 10000 # Number of simulation steps (more = more accuracy)

#basic status operations

calcForce = lambda x: (-1)*K*x

calcAccel = lambda F: F/mass    

calcDeltaV = lambda aNow,delT: aNow*delT

calcDeltaX = lambda vNow,aNow,delT: vNow*delT + 0.5*aNow*delT**2

calcZ = lambda T: sin(omegaD*T)

calcDamp = lambda vNow: vNow*vDamp

##### Initial conditions #####
initX = 0
initV = 1

vNow = initV
xNow = initX

vzNow = initV
xzNow = initX

timeNow = 0
    
##### Time handling ##### 
delT = totalTime/N  #Time for each time step

##### Arrays to store time points and associated x values #####
tSteps = []
xSteps = []
vSteps = []
zSteps = []
xzSteps = []
vzSteps = []

period = 0

minmax = 0 #lowest value in the graph, we need this to display the label out of the way but close enough

##### main "for" loop - do N steps if simulation #####
for step in range(1,N*showOldPlot): 
    aNow = calcAccel(calcForce(xNow)-calcDamp(vNow))   # calculate acceleration at point x        

    #xNow is relative to Z position, once the system starts moving. 

    xNow = xNow + calcDeltaX(vNow,aNow,delT)    # update x (location)

    vNow = vNow + calcDeltaV(aNow,delT)         # update velocity
    
    timeNow = timeNow+delT                      # update time
    
    tSteps.append(timeNow)
    xSteps.append(xNow)       # store current location for plotting
    vSteps.append(vNow)

    if(len(tSteps)>1):
        #list not empty
        if(abs(xSteps[0]-xSteps[step-1])<(10**(-3))):
            if(period==0):
                #The current value repeats and a period hasn't been set
                period = -1
            elif(period==-1):
                #The third repetition is the value - one off, not universal solution
                period = timeNow

#if the multiple value is enabled for omegaD set it now
if(omegaD_0!=0 and showOldPlot==1 and period>0):
    omegaD = omegaD_0*((2*pi)/period)

timeNow=0
###second for loop 
###just for the sake of clarity  - this one evaluates the actual system with a moving Z value
for step in range(1,N): 
    #xNow is relative to Z position, once the system starts moving. 

    zNow = calcZ(timeNow)

    azNow = calcAccel(calcForce(xzNow-zNow)-calcDamp(vzNow)) #Calculate Acceleration with Damping

    xzNow = xzNow+calcDeltaX(vzNow,azNow,delT) #calculate the actual position of X

    vzNow = vzNow + calcDeltaV(azNow,delT)
    
    timeNow = timeNow+delT                      # update time
    
    if(showOldPlot!=1): 
        tSteps.append(timeNow)    # store current time for plotting here since the first loop is not active
    zSteps.append(zNow)
    xzSteps.append(xzNow)
    vzSteps.append(vzNow)

    minmax = xzNow if xzNow<minmax else minmax
    minmax = vzNow if vzNow<minmax else minmax
    minmax = zNow if zNow<minmax else minmax

##### What is done here is to numerically calculate period and frequency ######
if(showOldPlot==1):
    print "Period: "+str(period)
    print "Frequency: "+str(1/period)

    plot(tSteps,xSteps)
    plot(tSteps,vSteps)

    show()    

plot(tSteps,zSteps,label="Z(t)")
plot(tSteps,xzSteps,label="X(t)")
plot(tSteps,vzSteps,label="V(t)")
xlabel('Time/s')
text(1,minmax*(110/100),'Damping Coefficient: '+str(vDamp)+', m: '+str(mass)+', k: '+str(K)+', '+r'$\omega_d$: '+str(omegaD),fontsize=14)
legend()
show()
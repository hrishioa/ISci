from pylab import *
from numpy import *


def calcForce(x,vNow):

    # Take current x coordinate and return force acting on mass
    K = 1 # K is the spring constant
    M = 0.5

    # calculate the force 
    F = (-1)*K*x-M*vNow
    return F

def calcForceNoDamp(x,vNow):

    # Take current x coordinate and return force acting on mass
    K = 1 # K is the spring constant
    M = 0.5
    
    # calculate the force 
    F = (-1)*K*x
    return F


def calcAccel(F):
    
    # Take force and mass and return acceleration based Newtons second law
    mass = 1  # mass of oscillator    



    aNow = F/mass
    return aNow

def calcAccelAdv(vNow,x):
    mass = float(1)
    M = float(0.5)
    K = float(1)

    aNow = float(((-(K/mass))*x)+(M/mass)*vNow)
    return aNow


def calcDeltaV(aNow,delT):

    # Take force and current velocity and calculate difference in speed deltaT
    delV = aNow*delT
    return delV


def calcDeltaX(vNow,aNow,delT):

    # Take acceleration and deltaT and return change in x
    delX = vNow*delT + 0.5*aNow*delT**2
    return delX
    

def main():

    ##### Initial conditions #####
    initX = 0
    initV = 1

    vNow = initV
    xNow = initX
    nd_xNow = initX
    nd_vNow = initV

    timeNow = 0


    ##### Time handling ##### 
    totalTime = 5*2*pi #Total time to simulate
    N = 1000000 # Number of simulation steps (more = more accuracy)
    delT = totalTime/N  #Time for each time step

    ##### Arrays to store time points and associated x values #####
    tSteps = []
    xSteps = []
    nd_xSteps = []
    
    
    ##### main "for" loop - do N steps if simulation #####
    for step in range(1,N): 

        fNow = calcForce(xNow,vNow)   # calculate force at point x
        aNow = calcAccel(fNow)   # calculate acceleration at point x
        
        aNow = calcAccelAdv(vNow,xNow)
        
        xNow = xNow + calcDeltaX(vNow,aNow,delT)   # update x (location)
        vNow = vNow + calcDeltaV(aNow,delT)   # update velocity
        timeNow = timeNow+delT    # update time
        
        tSteps.append(timeNow)    # store current time for plotting
        xSteps.append(xNow/1000)       # store current location for plotting

    timeNow = 0

    for step in range(1,N): 

        nd_fNow = calcForceNoDamp(nd_xNow,nd_vNow)   # calculate force at point x
        nd_aNow = calcAccel(nd_fNow)   # calculate acceleration at point x
        
        nd_xNow = nd_xNow + calcDeltaX(nd_vNow,nd_aNow,delT)   # update x (location)
        nd_vNow = nd_vNow + calcDeltaV(nd_aNow,delT)   # update velocity
        timeNow = timeNow+delT    # update time

        nd_xSteps.append(nd_xNow)       # store current location for plotting

    ##### See what you have done here ######
    plot(tSteps,xSteps,label='Damped')
    plot(tSteps,nd_xSteps,label='Undamped')
    legend()
    show()    
 
main()
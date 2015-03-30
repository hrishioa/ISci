from random import *
import numpy
import matplotlib.pyplot as plt
import math

def throwDie(times):
	mean = float(0)

	for i in range(0,times):
		mean += randint(1,6)

	mean/=times
	return mean

def throwSquareDie(times):
	mean = float(0)

	for i in range(0,times):
		mean += randint(1,6)**2

	mean/=times

	return mean

def singleTurn():
	return randint(1,6)+randint(1,6)+randint(1,6)

def plotHist(times):
	Y = []
	for i in range(0,times):
		Y.append(singleTurn())

	mean = numpy.mean(Y)
	sd = numpy.std(Y)

	Y2 = numpy.random.normal(mean,sd,times)

	plt.hist(Y,label="singleTurn",bins=10,histtype='stepfilled')
	plt.hist(Y2,alpha=0.6,label="Normal - mean: %f, sd: %f" % (mean,sd),bins=10,histtype='stepfilled')
	plt.legend()
	plt.show()

	print "Mean: %f, SD: %f" % (mean,sd)

def flipIt(N):
	pos = 0;
	for i in range(0,N):
		flip = randrange(2)
		if(flip==0):
			pos-=2
		else:
			pos+=1
		if pos<0:
			pos=0
	return pos

def flipMany(M,N):
	data = [0]*(N+1)
	for j in range(0,M):
		data[flipIt(N)] += 1

	return data

def boltzMann(kbT,e):
	return ((float(1)/float(kbT))*(math.e**(-e/kbT)))

def histFlipMany(M,N):
	Y = numpy.array(flipMany(M,N))
	print len(Y)
	OrigY = []

	mean = float(0)
	for i in range(0,len(Y)):
		for j in range(0,Y[i]):
			OrigY.append(i)
	mean=numpy.mean(OrigY)
	sd = numpy.std(OrigY)

	YNorm = (OrigY-mean)/sd

	print "Mean: %f" % mean

	X=numpy.linspace(0,N,N)
	Y3 = boltzMann(mean,X+1)

	plt.plot(X,Y3,label="Boltzmann")

	plt.hist(OrigY,alpha=0.5,normed=1,label="Steps")
	plt.legend()
	plt.show()

def main():
	print "Program Running..."

	print "ThrowDie: %f,ThrowSquareDie: %f, ThrowDieSquare: %f" % (throwDie(100),throwSquareDie(100),throwDie(100)**2);

	#plotHist(1000)

	histFlipMany(1000,100)

if __name__ == "__main__":
	main()
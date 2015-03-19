import matplotlib.pyplot as plt
import numpy

rangemin = -1
rangemax = 1
step = 0.1

X = []
Y = []

def y(X):
	return numpy.sin(X)

def main():
	print "Program Running..."

	for i in range(0,int(abs(rangemax-rangemin)/step)):
		X.append(rangemin+(i*step))
		Y.append(y(rangemin+(i*step)))

	plt.plot(X,Y)
	plt.show()

	inp = 'q'

	while True:
		if(inp.lower()[0]=='q'):
			break

if(__name__ == "__main__"):
	main()
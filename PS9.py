import numpy
import matplotlib.pyplot as plt
import csv
from scipy.fftpack import fft

files = {}
files['1-77'] = 'Bead1-.77XY.csv'
files['2-45'] = 'Bead2-.45A.csv'
files['2-77'] = 'Bead2-.77A.csv'
files['none'] = 'Bead2-None.csv'

#xmldoc = minidom.parse(filename)
print "Program Running..."

data = {}

data['1-77'] = []
data['2-45'] = []
data['2-77'] = []
data['2-none'] = []

def main():
	print "Main Running..."

	for key,value in data.items():
		if(key=='1-77'): #TODO: Remove
			with open(files[key],'r') as csvfile:
				reader = csv.reader(csvfile,delimiter=',')
				split=0
				data[key] = [[],[],[]]
				for row in reader:
					if(row[0]=='split'):
						split=1
						continue
					if(split==0):
						data[key][0].append(float(row[0]))
						data[key][1].append(float(row[1]))
					else:
						data[key][2].append(float(row[1]))
				data[key] = [numpy.array(data[key][0]),numpy.array(data[key][1]),numpy.array(data[key][2])]

			print "[%d,%d,%d]" % (len(data[key][0]),len(data[key][1]),len(data[key][1]))

			data[key][1] = data[key][1]-numpy.mean(data[key][1])
			data[key][2] = data[key][2]-numpy.mean(data[key][2])

			plt.plot(data[key][0],data[key][1],label="X")
			plt.plot(data[key][0],data[key][2],label="Y")
			plt.legend()
			plt.show()

			'''
			N = 600
			T = 1.0/800.0
			fftx = numpy.linspace(0.0, 1.0/(2.0*T), N/2)
			ffty = fft(data[key][1])
			ffty = ffty[1:]
			plt.plot(fftx, 2.0/N * numpy.abs(ffty[0:N/2]))
			plt.show()
			'''

if __name__=="__main__":
	main()
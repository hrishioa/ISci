import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.fftpack import fft
import scipy.signal as signal

files = {}
files['1-77'] = 'Bead1-.77XY.csv'
files['2-45'] = 'Bead2-.45AXY.csv'
files['2-77'] = 'Bead2-.77AXY.csv'
files['2-none'] = 'Bead2-NoneXY.csv'

#xmldoc = minidom.parse(filename)
print "Program Running..."

data = {}
ffts = {}

data['1-77'] = []
data['2-45'] = []
data['2-77'] = []
data['2-none'] = []

allDelta = {}

def main():
	print "Main Running..."

	for key,value in data.items():
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
			data[key] = [np.array(data[key][0]),np.array(data[key][1]),np.array(data[key][2])]

			#data sanitation
			data[key][2] = data[key][2][0:len(data[key][1])]

		print "[%d,%d,%d]" % (len(data[key][0]),len(data[key][1]),len(data[key][1]))

		#find Distance
		dist = (data[key][1])+(data[key][2][0:len(data[key][1])])

		#remove offset from both axes (for plotting)
		data[key][1] = data[key][1]-np.mean(data[key][1])
		data[key][2] = data[key][2]-np.mean(data[key][2])

		#plot X and Y and save the graph
		plt.plot(data[key][0],data[key][1],label="X")
		plt.plot(data[key][0],data[key][2],label="Y")
		plt.legend()
		plt.savefig('PS9-'+str(key)+'.png',bbox_inches='tight')
		plt.show()

		#calculate discrete fourier transform for distance and display,save
		N = len(dist)
		T = 1.0/800.0
		fftx = np.linspace(0.0, 1.0/(2.0*T), N/2)
		ffty = fft(dist)
		ffty = ffty[1:]
		ffty = 2.0/N * np.abs(ffty[0:N/2])
		plt.plot(fftx, ffty)
		plt.savefig('PS9-'+str(key)+'-fft.png',bbox_inches='tight')
		plt.show()

		ffts[key] = [fftx,ffty]

		#find maxdelta and the average delta along with the sd
		deltaD = []

		for i in range(1,len(dist)):
			deltaD.append(dist[i]-dist[i-1])

		allDelta[key] = deltaD

		#create a low pass filter and run the location values through it
		length = 101
		F_high=.25 #sample value, needs to be experimentally optimized
		filt = signal.firwin(length,cutoff=.25,window='hann')
		filt = -filt
		filt[length/2] = filt[length/2]+1

		out = signal.lfilter(filt, 1, deltaD)

		deltaD = out

	for key,value in allDelta.items():
		plt.plot(value,label=key)
		print "Experiment %s: Average Delta: %f with SD %f. Max Delta: %f" % (key,np.mean(value),np.std(value),np.amax(value))

	plt.legend()	
	plt.savefig('PS9-deltaVal.png',bbox_inches='tight')			
	plt.show()


	for key,value in ffts.items():
		plt.plot(value[0],value[1],label=key)

	plt.legend()
	plt.savefig('PS9-fft.png',bbox_inches='tight')
	plt.show()

if __name__=="__main__":
	main()
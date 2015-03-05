from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def part1():
	delta = 0.05
	x = arange(-3,3,delta)
	y = arange(-3,3,delta)
	X,Y = meshgrid(x,y)

	F = (X*X)+(2*X*Y)+(Y*Y)
	C = 100*(e**(-(((X**2)+(Y**2))/25)))

	F2 = 1/(sqrt(X**2+Y**2))
	G = (-1)/(sqrt(((X-1)**2)+(Y**2)))

	plt.figure()

	#CS = plt.pcolormesh(X,Y,,shading='gouraud')

	CS = plt.contour(X,Y,F,max=1.05,min=-0.95)
	plt.clabel(CS, inline=1, fontsize=10)
	plt.show()

	part3(X,Y,F)

def part2():
	delta = 0.05
	x = arange(-2,2,delta)
	y = arange(-2,2,delta)
	X,Y = meshgrid(x,y)

	F = 1/(sqrt(X**2+Y**2))
	G = -2 / (sqrt((X-1)*(X-1)+(Y*Y)))
	H = 1 / sqrt((X*X)+(Y-1)*(Y-1))

	plt.figure()

	CS = plt.pcolormesh(X, Y, F+G+H, vmax=5, vmin=-5, shading='gouraud')

	plt.colorbar()
	plt.show()

	part3(X,Y,F+G+H)

def part0():
	t = [1,1,1]
	u = [1,-1,-1]
	tlength = sqrt(t[0]*t[0]+t[1]*t[1]+t[2]*t[2])
	ulength = sqrt(u[0]*u[0]+u[1]*u[1]+u[2]*u[2])
	dprod = dot(t,u)
	angle = arccos(dprod / (tlength * ulength))
	angledegrees = angle * 180 / pi

	print angledegrees

def part3(X,Y,Z,surface=True,contour=False):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	if(surface==True):
		ax.plot_surface(X, Y, Z, rstride=5, cstride=5,cmap=plt.cm.jet)

	if(contour==True):
		GX,GY = gradient(Z)
		ax.quiver(X,Y,Z,GX,GY,Z,length=0.5)

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')



	plt.show()

def part4():
	delta = 0.5
	x = arange(-3,3,delta)
	y = arange(-3,3,delta)
	X,Y = meshgrid(x,y)

	GX = 2*X
	GY = -2*Y

	plt.figure()
	plt.quiver(X,Y,GX,GY,units='width')
	plt.show()

def part5():
	delta = 0.4
	x = arange(-3,3.1,delta)
	y = arange(-3,3.1,delta)

	X,Y = meshgrid(x,y)

	F = (X*X)+(2*X*Y)+(Y*Y)
	C = sin(X)+cos(Y)+tan(X*Y)
	F2 = (1/sqrt((X*X)+(Y*Y)))
	Q5 = -X*Y

	Z=Q5
	
	#FX = FY = 2*X+2*Y
	#FX,FY = gradient(F)
	FX = Y
	FY = -X

	plt.figure()
	CS = plt.pcolormesh(X,Y,Z,vmax=5,vmin=-5,shading='gouraud')
	plt.colorbar()
	Q = plt.quiver(X,Y,FX,FY,units='width')

	plt.show()

	part3(X,Y,Z,contour=True)

###################################################################33
print "Program running..."

part5()
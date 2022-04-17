import sys
print(sys.version)
import pylab

x = [x for x in range(0,10)]
y = [y**2 for y in range(0,10)]
pylab.plot(x,y)
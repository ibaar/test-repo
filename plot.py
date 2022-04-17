import sys
print(sys.version)
import pylab

x = [x for x in range(0,10)]
y = [y**2 for y in range(0,10)]

pylab.figure('lin')
pylab.plot(x,y,label='quad')
pylab.xlabel('input')
pylab.ylabel('time')
pylab.title('quad function')
pylab.legend('upper left')
pylab.savefig('hello.png')



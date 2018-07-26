
''' 
Observe the change of the sloop of
the activation function by changing the 
bias for a constant weight '''

import numpy as np
import matplotlib.pylab as plt

w = 5 
b1 = -8.0
b2 = 0.0
b3 = 8.0

l1 = 'b = -8.0'
l2 = 'b = 0.0'
l3 = 'b = 8.0'

x = np.arange( -10, 10, 0.1)

for b, l in [ (b1, l1) , (b2, l2) , (b3, l3) ]:
	f = 1 / (1 + np.exp(-(x*w+b)))
	plt.plot(x, f, label=l)

plt.xlabel('x')
plt.ylabel('h_wb(x)')
plt.legend(loc=2)
plt.show()

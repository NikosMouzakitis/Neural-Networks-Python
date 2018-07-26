'''
Observe the differences in the sigmoid function(activation function)
for different values for weights, in this case the bias does not exist.
'''

import numpy as np
import matplotlib.pylab as plt
w1 = 0.5
w2 = 1.0
w3 = 2.0
l1 = 'w2 = 0.5'
l2 = 'w2 = 1.0'
l3 = 'w3 = 2.0'

x = np.arange(-8, 8 , 0.1)
f = 1/(1 + np.exp(-x))

for w, l in [ (w1, l1) , (w2, l2), (w3, l3)]:
	f = 1/(1+np.exp(-x*w))
	plt.plot(x,f,label=l)

plt.xlabel('x')
plt.ylabel('h_w(x)')
plt.legend(loc=2)
plt.show()


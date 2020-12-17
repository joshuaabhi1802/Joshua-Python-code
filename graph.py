import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w') 
import numpy as np
import matplotlib.pyplot as plt
x=np.array([-1,2, -3,4, -7,9])
y=x**2
plt.plot(x,y)
plt.show()
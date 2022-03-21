# Author Sadie Concannon
# Weekly task 8: Plot  the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0,4]
# use the one set of axes

#import numpy and matplotlib
from turtle import color
import numpy as np
import matplotlib.pyplot as plt

#create numpy range for x where f(x) = x
x = np.linspace(0,5)
ax = x

#create list of g(x) = x^2 rename g(x) as y
y = [i**2 for i in x]

#create list for h(x) = x^3 rename function h(x) as z
z = [i**3 for i in x]

#plot
plt.plot (x,ax, label='Line f(x)')

plt.plot (x,y, label='Line g(x)')

plt.plot (x,z, label='Line h(x)')
#add title
plt.title('Week 8 Task')
plt.legend()
plt.show()

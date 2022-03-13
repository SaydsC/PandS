# Author Sadie Concannon
# Weekly task 8: Plot  the functions f(x)=x, g(x)=x^2 and h(x)=x^3 in the range [0,4]
# use the one set of axes

#import numpy and matplotlib
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#create numpy range for x where f(x) = x
x = np.linspace(0,4)

#create list of g(x) = x^2 rename g(x) as y
y = [i**2 for i in x]

#create list for h(x) = x^3 rename function h(x) as z
z = [i**3 for i in x]

#try to improve appearance of graph by adding labels and title
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x,y,z, color='white', edgecolors='grey', alpha=0.5)
ax.scatter(x,y,z, c='red')
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("z Axis")
ax.set_title("Week 8 Task")
# make title bold
ttl = ax.title
ttl.set_weight("bold")

#plot
plt.show()

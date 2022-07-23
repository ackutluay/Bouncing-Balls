# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 12:40:10 2022

@author: ackut
"""

from numpy.random import default_rng       # numpy random value generator
import matplotlib.pyplot as plt            # plotting library matpotlib
import matplotlib.animation as animation   # matplotlib animations library
from IPython.display import HTML, Image    # to convert our animation to HTML for display

n= 12 #number of balls
rng= default_rng() #random number generator
pos= (20* rng.random(n*2)-10).reshape(n,2) #positions, this is a 2D array because we need x & y positions
vel=(0.3 * rng.random(size=n*2)).reshape(n,2) #velocities, again in 2D in x & y directions.
sizes= 100* rng.random(n) + 240 #balls with random sizes #multiply by 100 and add 100 to make them decent sizes.

colors= rng.random([n,3]) #random colors for balls
dt=0.01
g=9.81


fig= plt.figure(num=1,figsize=(6,6))
ax= plt.axes(xlim=(-n,n),ylim=(-n,n))
plt.xlabel('x axis')
plt.ylabel('y axis')
circles= plt.scatter(pos[:,0],pos[:,1],marker='h',s=sizes,c=colors)

def animate(i):
    global pos
    global vel
    vel[:,1] = vel[:,1] - g*dt
    pos= pos + vel
    
    bounce= abs(pos) > n
   
    vel[bounce] = -vel[bounce]
    
    circles.set_offsets(pos)
    
    return circles

anim = animation.FuncAnimation(fig, animate, frames=100, interval=400) #making the animation

plt.show()

anim.save('bouncing balls introducing gravity.gif',writer='imagemagick',fps=60)

#NOW THE CHALLENGE PART


   # Change the markers to Hexagons """DONE"""
    #Destroy balls which hit the edges """DONE"""
    #If balls hit the edges move them to the opposite side (wrap the walls) """DONE"""
    #Introduce gravity """DONE"""


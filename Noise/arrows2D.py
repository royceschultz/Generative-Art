import numpy as np
import matplotlib.pyplot as plt
from opensimplex import OpenSimplex
import gif

def plot_arrow(x,y,dir):
    plt.plot([x,x+dir[0]],[y,y+dir[1]],c='b')

simp = OpenSimplex()
n = 16
T_MAX = 2*np.pi
NUM_FRAMES = 180
x = np.linspace(0,1,n)
y = np.linspace(0,1,n)
z = np.linspace(0,T_MAX,NUM_FRAMES)
t = np.linspace(0,T_MAX,NUM_FRAMES)
canvas = np.zeros((len(x),len(y)))
for k in range(len(t)):
    print(k)
    for i in range(len(x)):
        for j in range(len(y)):
            dirX = simp.noise4d(x[i],y[j],np.cos(t[k]),np.sin(z[k]))
            dirY = simp.noise4d(x[i],y[j],np.cos(t[k])+3,np.sin(z[k])+3)
            plot_arrow(10*x[i],10*y[j],[dirX,dirY])
    plt.axis('equal')
    plt.axis('off')
    plt.xlim(-1,11)
    plt.ylim(-1,11)
    #plt.show(block=False)
    #plt.pause(0.1)
    plt.savefig('ADFrames/'+str(k)+'.png')
    plt.clf()

gif.gifFolder('ADFrames','arrows2D.gif')

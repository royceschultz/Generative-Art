import numpy as np
import matplotlib.pyplot as plt

import gif

def plot_ray(x,y,angle,r=1):
    dx = r * np.sin(angle)
    dy = r * np.cos(angle)
    plt.plot([x,x + dx],[y,y + dy], c=(0,.7-r/20,0))
    return (x+dx,y+dy)

offset = 0.7
def fibTree(root,angle,n):
    if n <= 0:
        return
    x,y = root
    x,y = plot_ray(x,y,angle,n)
    fibTree((x,y),angle + offset, n-1)
    fibTree((x,y),angle - offset, n-1)

i = 0
fig = plt.figure()
for offset in np.linspace(0,1,50):
    fig.clf()
    fibTree((0,0),0,10)
    plt.axis('off')
    plt.savefig('Output/'+str(i)+'.png')
    i += 1

gif.gifFolder('Output','output.gif')

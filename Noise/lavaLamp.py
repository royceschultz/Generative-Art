import numpy as np
from opensimplex import OpenSimplex
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import io
import imageio

def plot_arrow(x,y,dir):
    plt.plot([x,x+np.cos(dir)],[y,y+np.sin(dir)],c='b')

simp = OpenSimplex()
n = 512
D_MAX = 2
T_MAX = 2*np.pi
NUM_FRAMES = 150
x = np.linspace(0,D_MAX,n)
y = np.linspace(0,D_MAX,n)
z = .5*np.cos(np.linspace(0,T_MAX,NUM_FRAMES))
t = .5*np.sin(np.linspace(0,T_MAX,NUM_FRAMES))
NUM_LAYERS = 3
canvas = np.zeros((len(x),len(y), NUM_LAYERS)).astype(int)
NUM_SAMPLE_LAYERS = 2
samples = np.zeros((len(x),len(y), NUM_SAMPLE_LAYERS))
palette = { 0:[73,89,103], 1:[189,213,234], 2:[87,115,153], 3:[255,79,121]}

frames = []
fig = plt.Figure(figsize=(5, 4), dpi=100)
imData = io.BytesIO()
for k in range(len(t)):
    print(k,end='\r')
    for i in range(len(x)):
        for j in range(len(y)):
            for h in range(NUM_SAMPLE_LAYERS):
                samples[i][j][h] = int(simp.noise4d(x[i],y[j],t[k]+2*h,z[k]) + 1)
            canvas[i][j] = palette[samples[i][j][0] + 2*samples[i][j][1]]
    plt.axis('off')
    plt.imshow(canvas, interpolation="bicubic")
    # plt.show(block=False)
    # plt.pause(0.001)
    plt.savefig(imData, format='png')
    plt.clf()
    imData.seek(0)
    frames.append((255*mpimg.imread(imData)).astype(np.uint8))
    imData.seek(0)

print('Done, Saving gif...')
imageio.mimsave('lamp.gif', frames, duration = 0.05)

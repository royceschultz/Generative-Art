import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

n = 300
canvas = 999*np.ones((n,n))
for i in range(n):
    for j in range(n):
        canvas[i][j] = min(i,j,n-i,n-j)
num_seed_circles = 3
num_fill_circles = 30
xs,ys,ss = [],[],[]
patches = []
for q in range(num_seed_circles):
    print(q)
    x,y = np.random.randint(0,n,2)
    while canvas[x][y] == 0:
        x,y = np.random.randint(0,n,2)
    radius = min(50,canvas[x][y])
    patches.append(mpl.patches.Circle([x,y], radius=radius))
    for i in range(n):
        for j in range(n):
            dis = ((x-i)**2 + (y-j)**2)**.5
            if dis-radius < canvas[i][j]:
                canvas[i][j] = max( dis-radius ,0)

for q in range(num_fill_circles):
    print(q)
    x,y = np.unravel_index(np.argmax(canvas, axis=None), canvas.shape)
    radius = canvas[x][y]
    patches.append(mpl.patches.Circle([x,y], radius=radius))
    for i in range(n):
        for j in range(n):
            dis = ((x-i)**2 + (y-j)**2)**.5
            if dis-radius < canvas[i][j]:
                canvas[i][j] = max( dis-radius ,0)


p = mpl.collections.PatchCollection(patches, alpha=0.4)
colors = 100*np.random.rand(len(patches))
p.set_array(np.array(colors))
plt.figure()
ax = plt.gca()
ax.add_collection(p)
plt.axis('equal')
plt.axis('off')
plt.savefig('pack.png')

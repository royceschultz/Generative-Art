import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

def dist(x,y):
    d = 0
    for i in range(len(x)):
        d += abs(x[i] - y[i])
    return d

def pixelSort(imageName, tol, numCycles):
    image = mpimg.imread(imageName)
    (m, n, l) = image.shape
    print(m,n,l)
    mpimg.imsave('SortImageFrames/'+str(0)+'.png',image,format='png',dpi=100)

    for cycle in range(numCycles):
        print('Frame '+str(cycle)+' of '+str(numCycles))
        for row in range(m):
            randCol = random.randint(0,n-1)
            j, k = randCol, randCol
            while j > 1 and dist(image[row][j-1], image[row][randCol]) < tol:
                j -= 1
            while k+1 < n and dist(image[row][k+1], image[row][randCol]) < tol and sum(image[row][k]) < 2:
                k += 1
            if j != k:
                x = image[row][j:k]
                image[row][j:k] =  x[np.sum(x, axis=1).argsort()]

        mpimg.imsave('SortImageFrames/'+str(cycle+1)+'.png',image,format='png',dpi=100)

pixelSort('image.png',0.42,100)

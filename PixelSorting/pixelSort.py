import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

import gif # gif.py

def dist(x,y): # Manhatten Distance
    d = 0
    for i in range(len(x)):
        d += abs(x[i] - y[i])
    return d

def pixelSort(imageName, tol, numCycles):
    image = mpimg.imread(imageName) # Open Image
    (m, n, l) = image.shape
    print(m,n,l)
    mpimg.imsave('SortImageFrames/'+str(0)+'.png',image,format='png',dpi=100) # First Frame

    for cycle in range(numCycles):
        print('Frame '+str(cycle)+' of '+str(numCycles)) # Console log
        for row in range(m):
            randCol = random.randint(0,n-1) # Select seed pixel
            j, k = randCol, randCol
            while j > 1 and dist(image[row][j-1], image[row][randCol]) < tol:
                j -= 1 # Increase range to the left
            while k+1 < n and dist(image[row][k+1], image[row][randCol]) < tol and sum(image[row][k]) < 2:
                k += 1 # Increase range to the right
            if j != k:
                x = image[row][j:k]
                image[row][j:k] =  x[np.sum(x, axis=1).argsort()] # Sort range

        mpimg.imsave('SortImageFrames/'+str(cycle+1)+'.png',image,format='png',dpi=100) # Save frame

pixelSort('image.png',0.42,100) # Run script
gif.gifFolder('SortImageFrames')

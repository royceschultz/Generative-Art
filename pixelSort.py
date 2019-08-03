import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

def value(pixel):
    return sum(pixel)

def sortBySum(x):
    x = list(x)
    for i in range(len(x)):
        for j in range(i):
            if sum(x[i]) < sum(x[j]):
                y = x.pop(i)
                x.insert(j, y)
                break
    return np.array(x)

def dist(x,y):
    d = 0
    for i in range(len(x)):
        d += abs(x[i] - y[i])
    return d

def pixelSort(imageName, tol, numCycles):
    image = mpimg.imread(imageName)

    plt.imshow(image)
    plt.show(block=False)
    plt.pause(0.001)
    (m, n, l) = image.shape
    print(m,n,l)
    fig = plt.figure()
    plt.imshow(image)
    fig.savefig('testSaveFig/'+str(0))
    image = image.tolist()

    for cycle in range(numCycles):
        print(cycle)
        for row in range(m):
            randCol = random.randint(0,n-1)

            j = randCol
            while j > 1 and dist(image[row][j-1], image[row][randCol]) < tol:
                j -= 1
            k = randCol
            while k+1 < n and dist(image[row][k+1], image[row][randCol]) < tol and sum(image[row][k]) < 2:
                k += 1
            image[row][j:k] = sortBySum(image[row][j:k])

        plt.imshow(image)
        fig.savefig('testSaveFig/'+str(cycle+1))


pixelSort('image.png',0.4,50)

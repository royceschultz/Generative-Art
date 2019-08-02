import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import random

def value(pixel):
    return sum(pixel)

def pixelSort(imageName, verticalBias, horizontalBias, numFrames, numCycles):
    image = mpimg.imread(imageName)
    plt.imshow(image)
    plt.show()
    fig = plt.figure()
    (m, n, l) = image.shape
    print(m,n,l)

    for frame in range(numFrames):
        print(frame)
        for cycle in range(numCycles):
            x = random.randint(0,m-1)
            y = random.randint(0,n-1)

            probVert = abs(verticalBias)/(verticalBias+horizontalBias)

            if random.random()< probVert: #pick vertical direction
                if y > 0:
                    if value(image[x][y]) < value(image[x][y-1]):
                        here = list(image[x][y])
                        there = list(image[x][y-1])
                        image[x][y] = there
                        image[x][y-1] = here
                else:
                    if value(image[x][y]) < value(image[x][y+1]):
                        here = list(image[x][y])
                        there = list(image[x][y+1])
                        image[x][y] = there
                        image[x][y+1] = here
            else: #pick horizontal direction
                if x > 0:
                    if value(image[x][y]) < value(image[x-1][y]):
                        here = list(image[x][y])
                        there = list(image[x-1][y])
                        image[x][y] = there
                        image[x-1][y] = here
                else:
                    if value(image[x][y]) < value(image[x+1][y]):
                        here = list(image[x][y])
                        there = list(image[x+1][y])
                        image[x][y] = there
                        image[x+1][y] = here
        plt.imshow(image)
        fig.savefig('testSaveFig/'+str(frame))
        print(sum(sum(sum(image))))


pixelSort('image.png',1,0,50,1000000)

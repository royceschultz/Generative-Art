from PIL import Image
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

im = Image.open('image.png')
plt.imshow(im)

im = np.array(im).astype('int')
height,width,depth = im.shape

pixels = im.reshape(-1,4)

def select_pixels(px,n):
    return px[sorted(np.random.randint(0,len(px),n))]

def ham_score(px1, px2):
    return sum(abs(px1-px2)**2)

def frame(img,width=1): # Adds a white boarder
    m,n,o = img.shape
    canvas = 255*np.ones((m+2*width,n+2*width,o))
    canvas[width:-width,width:-width] = img
    return canvas.astype(int)

def generate_image(filename):
    numCycles = 100
    numPixels = 12
    palette = select_pixels(pixels,12).astype(float) # Randomly select starting pixels

    for i in range(numCycles):
        choice = select_pixels(pixels,100*numPixels) # Select training data
        direction = np.zeros((numPixels,4)) # Initialize cost vector
        counts = np.ones(numPixels) # Record counts for normalization
        max_dist = 0 # Record max distance to monitor convergence
        for j,x in enumerate(choice): # For each training point
            min_dist = 999
            min_idx = -1
            for k,y in enumerate(palette): # For each palette point
                dist = ham_score(x,y)
                if dist < min_dist: # Find the minimum distance
                    min_dist = dist
                    min_idx = k
            if min_dist > max_dist: # Convergence monitoring
                max_dist = min_dist
            direction[min_idx] += x-palette[min_idx] # Add the cost to the log
            counts[min_idx] += 1

        counts = np.tile(counts,(4,1)).transpose() # reshape for division
        direction = np.divide(direction,counts) # Normalize
        palette += direction.max()*0.001*direction # Train
    canvas = frame(palette.reshape(4,3,4))
    cw,ch,cd = canvas.shape
    ow,oh,od = 600,500,4
    output = np.zeros((ow,oh,od))
    for x in range(ow):
        for y in range(oh):
            output[x][y] = canvas[int(cw*x/ow),int(ch*y/oh)]

    plt.imshow(output.astype('uint8'))
    matplotlib.image.imsave(filename,output.astype('uint8'))

for i in range(50):
    print(i)
    generate_image('output'+str(i+1)+'.png')

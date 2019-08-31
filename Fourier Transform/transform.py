import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

image = np.array(mpimg.imread('image.jpg'))
(m, n, l) = image.shape
print(m,n,l)

plt.imshow(image)
plt.show(block=False)

red = image[:,:,0]
print(red.shape)
redList = red.reshape(-1)
print(redList.shape)
buffer = 50
fig = plt.figure()
for i in range(len(redList)-buffer):
    print(100*i/(len(redList)-buffer))
    x = redList[i:i+50]
    f = np.fft.fft(x)
    f += max(f)/100*np.random.rand(buffer)*np.complex(1,1)
    finv = np.fft.ifft(f)
    redList[i] = finv[0]

plt.imshow(image)
plt.show()
print('done')

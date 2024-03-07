from matplotlib import pyplot as plt
import numpy as np
import time
import cv2

# section set up
im = plt.imread('rainbow.jpg')
fig, ax = plt.subplots(1,2)
(row,col,channel) = im.shape

im_gray = np.zeros((row,col,1))

#section 2 - Grayscale
# R* 0.299 + G* 0.587 + B*0.114
start_time = time.time()
im_gray = cv2.cvtColor(im,cv2.COLOR_RGB2GRAY)
#for r in range(row):
 #   for c in range(col):
  #      R= im[r,c,0]
   #     G= im[r,c,1]
    #    B= im[r,c,2]

     #   gray_val = R*0.299 + G*0.587 + B*0.114
      #  im_gray[r,c] = gray_val

end_time = time.time()
elapsed_time = end_time - start_time

print("Elapsed Time is " +  str(elapsed_time) + " seconds")
#Section 3 - Displaying images
ax[0].imshow(im)
ax[0].axis('off')
ax[0].set_title('RGB')

ax[1].imshow(im_gray, cmap='gray')
ax[1].axis('off')
ax[1].set_title('GRAY')

plt.show()

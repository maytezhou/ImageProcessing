import cv2
from matplotlib import pyplot as plt


im_cv2 = cv2.imread('brickley.jpg')
im_mat = plt.imread('brickley.jpg')

print(type(im_cv2))
print(type(im_mat))
# OpenCV imports as BGR
#Matplotlib imports as RGB
fig, ax = plt.subplots(1,2)
                               
im_mat2BGR = cv2.cvtColor(im_mat, cv2.COLOR_RGB2BGR)
im_cv2RGB = cv2.cvtColor(im_cv2, cv2.COLOR_BGR2RGB)


 #displaying in opencv
cv2.imshow("Brickley",im_mat2BGR) # opencv expects BGR

# displaying using matplotlib
ax[0].imshow(im_cv2RGB)
ax[1].imshow(im_cv2)

#plt.imshow(im_cv2RGB) # matplotlib expects RGB

plt.show()
cv2.waitKey(0)
import cv2
import matplotlib.pyplot as plt

# Reading the image and converting into B/W
image = cv2.imread('01.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image.shape)  
  
# Applying the function
fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)
fast.setThreshold(5)
  
# Drawing the keypoints
kp = fast.detect(gray_image, None)


#Second method
orb = cv2.ORB_create(nfeatures=2000)
kp, des = orb.detectAndCompute(gray_image, None)

kp_image = cv2.drawKeypoints(image, kp, None, color=(0, 255, 0))







kp_image = cv2.cvtColor(kp_image, cv2.COLOR_BGR2RGB)

plt.imshow(kp_image)
plt.show()
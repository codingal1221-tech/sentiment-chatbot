import cv2
import matplotlib.pyplot as plt
image = cv2.imread('cat.avif')
image_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
plt.imshow(image,cv2.COLOR_BGR2GRAY)
plt.title"RGB Image")
plt.show ()
cropped_image = image[100:300,200:400]
cropped_rgb = cv2.cvtColor(cropped_image,cv2.COLOR_BGR2GRAY)
plt.iCOLOR_BGR2GRAshow(cropped_rgb)
plt.title("Cropped Region")
plt.show()
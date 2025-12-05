import cv2
ivage= cv2.imread('cat.avif')
cv2.namedWindow('Loaded Ivage',cv2.WINDOw_NORMAL)
cv2.resizeWindow("Load Image",800,500)
c2.imshow("Load Image",image)
cv2.destroyAllWindows()
print(f"Image Dimensons:{image.shape})")
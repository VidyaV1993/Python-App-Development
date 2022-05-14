import cv2
import glob

img=cv2.imread("galaxy.jpg", 0) # read rgb image - pass 1
print(type(img))
print(img)
print(img.shape)
print(img.ndim)

resized_img = cv2.resize(img,(int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_img)
cv2.imwrite("Galaxy_resized.jpg", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

images=glob.glob("*.jpg")

for image in images:
    img1=cv2.imread(image,0)
    re=cv2.resize(img1,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)

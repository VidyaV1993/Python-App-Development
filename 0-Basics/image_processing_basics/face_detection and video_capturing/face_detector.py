import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread("photo.jpg")   # Read an image named "photo"
img = cv2.imread("news.jpg")   # Read an image named "news"

gray_img=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # RGB to Grayscale

faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.1,   # scaleFactor decreases the search size of the image by x%, here 1.05 for "photo.jpg" therefore 5%; 1.1 for "news.jpg"
minNeighbors=5)     # minNeighbors is how many neighbors to search around in the window

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

print(type(faces))
print(faces)
# cv2.imshow("Gray", img) # Displays the image with face highlighted inside a rectangle

resized=cv2.resize(img, (int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

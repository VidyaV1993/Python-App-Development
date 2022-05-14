import cv2, time

video=cv2.VideoCapture(1)   # 1 means default camera is used

a=0 

while True:
    a=a+1
    check, frame = video.read()

    print(check)
    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # time.sleep(3)
    cv2.imshow("Capturing", frame)
    key=cv2.waitKey(1)  #wait for 1 millisecond

    if key==ord('q'):
        break

print(a) 
video.release()
cv2.destroyAllWindows()

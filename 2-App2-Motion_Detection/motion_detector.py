from datetime import datetime
import cv2, time, pandas

first_frame = None                  # Variable initialized to None
status_list = [None, None]          # List to store the object detection status
times = []                          # List to store the date time info
video=cv2.VideoCapture(1)           # 1 means default camera is used for video capture
df = pandas.DataFrame(columns=["Start", "End"]) # Data Frame to store the timestamp info of object detection

while True:
    check, frame = video.read()                         # Video input
    status = 0                                          # Variable to denote object detection. 0 means no object detected
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # Convert to grayscale
    gray = cv2.GaussianBlur(gray, (21,21),0)            # Blur the image

    if first_frame is None:
        first_frame=gray        # store the background without the object in the frame
        continue

    delta_frame = cv2.absdiff(first_frame,gray)                                 # Store the delta or difference frame
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]    # This method returns a tuple and we need the second element
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)                 # Smoothen the thresh_frame

    # Find contours and highlight object in rectangles
    (cnts,_) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1      # Variable to denote object detection. 1 means object detected
        (x,y,w,h)=cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)

    # Record the current timestamp when a change in object detection status occurs
    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    # Display all the output video frames in different windows
    cv2.imshow("Gray frame", frame)
    cv2.imshow("Delta frame", delta_frame)
    cv2.imshow("Threshold frame", thresh_frame)
    cv2.imshow("Color frame", frame)

    key=cv2.waitKey(1)  #wait for 1 millisecond

    # Print the frames in matrix
    # print(gray)
    # print(delta_frame)

    # Quit the app on keyboard command 'q'
    if key==ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

print(status_list)       # Print the list which denotes object detected or not
print(times)             # Print the timestamp info of object detection

# Store the timestamp info of object detection in to an excel file
for i in range(0, len(times), 2):
    df = df.append({"Start":times[i], "End":times[i+1]}, ignore_index=True)
df.to_csv("Times.csv")

video.release()
cv2.destroyAllWindows()

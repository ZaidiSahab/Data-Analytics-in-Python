
import cv2

# Capture video from the default webcam (usually device 0)
video_capture = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()


    # Convert the frame to grayscale
   # gray_frame = cv2.cvtColor(frame, cv2.color())
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the frame in a window
    cv2.imshow("Video Frame", frame)


    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()

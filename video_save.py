import cv2

# Set the video file save path and name
output_path = r"C:\Users\Lenovo\Documents\output_video.mp4"

# Capture video from the default webcam (usually device 0)
video_capture = cv2.VideoCapture(0)

# Get the default width and height of the video frames
frame_width = int(video_capture.get(3))  # Width
frame_height = int(video_capture.get(4))  # Height

# Define the codec and create a VideoWriter object to save the video
# The codec used here is 'X264' and the file format is .mp4
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (frame_width, frame_height), isColor=False)

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()

    if not ret:
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Write the grayscale frame to the video file
    out.write(gray_frame)

    # Display the grayscale frame in a window
    cv2.imshow("Grayscale Video Frame", gray_frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and writer objects and close all windows
video_capture.release()
out.release()
cv2.destroyAllWindows()

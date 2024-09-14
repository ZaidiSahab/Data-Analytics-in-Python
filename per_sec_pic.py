import cv2
import os

# Set the video file save path for captured frames
output_folder = r"C:\Users\Lenovo\Documents\frames"
os.makedirs(output_folder, exist_ok=True)

# Capture video from the default webcam (usually device 0)
video_capture = cv2.VideoCapture(0)

# Get the frame rate of the video (frames per second)
fps = int(video_capture.get(cv2.CAP_PROP_FPS))

frame_count = 0
saved_frame_count = 0

while True:
    # Read a frame from the video capture
    ret, frame = video_capture.read()

    if not ret:
        break

    # Check if it's time to save the frame (every second)
    if frame_count % fps == 0:
        # Save the frame as an image file
        frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        saved_frame_count += 1
        print(f"Saved: {frame_filename}")

    # Display the current frame in a window
    cv2.imshow("Video Frame", frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_count += 1

# Release the video capture object and close all windows
video_capture.release()
cv2.destroyAllWindows()

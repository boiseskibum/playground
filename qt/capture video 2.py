import cv2
import time

def stopwatch(start_time, msg):
    current_time = time.time()  # Get the current time in seconds
    elapsed_time = current_time - start_time  # Calculate the elapsed time
    ft = "{:.2f}".format(elapsed_time)
    print(f"    Elapsed: {ft} sec, msg: {msg}")

    return current_time

def capture_video():
    print("started program")
    # Open the default webcam
    begin_time = time.time()
    cap = cv2.VideoCapture(0)

    begin_time = stopwatch(begin_time, "point A")

    # Define the video codec (H.264)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')

    begin_time = stopwatch(begin_time, "point B")


    # Create a VideoWriter object to save the video
    out = cv2.VideoWriter('captured_video.mp4', fourcc, 60.0, (640, 480))

    begin_time = stopwatch(begin_time, "point C")


    # Record video for 4 seconds
    start_time = cv2.getTickCount()
    while True:
        ret, frame = cap.read()
        out.write(frame)
        cv2.imshow('Video Capture', frame)
        if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() >= 4:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    begin_time = stopwatch(begin_time, "point D")


    # Release the video capture and writer objects
    cap.release()
    out.release()

    begin_time = stopwatch(begin_time, "point E")


    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Start capturing video
capture_video()

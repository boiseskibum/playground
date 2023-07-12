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
    begin_time = time.time()
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fcnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f"cap properties - w: {w}, h: {h}, fps: {fps}, fcnt: {fcnt}")

    begin_time = stopwatch(begin_time, "point A")

    # Define the video codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    begin_time = stopwatch(begin_time, "point B")

    # Create a VideoWriter object to save the video
    video_writer = cv2.VideoWriter('captured video 4.mp4', fourcc, 20.0, (640, 480))


    # Record video for 4 seconds
    start_time = cv2.getTickCount()
    while True:
        ret, frame = cap.read()

        cv2.imshow('Video Capture', frame)
        video_writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and writer objects
    cap.release()
    video_writer.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


# Start capturing video
capture_video()

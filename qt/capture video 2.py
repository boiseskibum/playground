# capture and save video
import cv2

def capture_video():
    print("started program")
    # Open the default webcam

    cam_index = 0
    cap = cv2.VideoCapture(cam_index)

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fcnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f"PRE cap properties - w: {w}, h: {h}, fps: {fps} cam_index: {cam_index}")
    # Define the video codec (H.264)
    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    filename = 'captured video 2.mp4'

    # Create a VideoWriter object to save the video
    out = cv2.VideoWriter(filename, fourcc, fps, (w, h))

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

    # Release the video capture and writer objects
    cap.release()
    out.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

# Start capturing video
capture_video()

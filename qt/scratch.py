import cv2

def set_camera_fps():
    # Open the default webcam
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Failed to open camera")
        return

    # Set the desired frame rate (FPS)
    desired_fps = 30  # Set your desired FPS here
    cap.set(cv2.CAP_PROP_FPS, desired_fps)

    # Define the video codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    filename = "capture video 1.mp4"
#    out = cv2.VideoWriter(filename, fourcc, fps, (w, h))

    # Read and display frames from the webcam
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fcnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f"POST cap properties - w: {w}, h: {h}, fps: {fps}, fcnt: {fcnt}, filename: {filename}")

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

# Start capturing video with the desired FPS
set_camera_fps()
import psutil

video_devices = psutil.video_devices()

for device in video_devices:
    print(device)
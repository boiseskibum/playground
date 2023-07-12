# Import opencv for computer vision stuff
import cv2
# Import matplotlib so we can visualize an image
from matplotlib import pyplot as plt

#### photo
def take_photo():

    ret, frame = cap.read()

    # display photo
#    plt.imshow(frame)

    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))   # color reordering is matplotlib
    plt.show()

    #write photo to file
    cv2.imwrite('webcamphoto.jpg', frame)

#### video
def take_video():

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)
    fcnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f"cap properties - w: {w}, h: {h}, fps: {fps}, fcnt: {fcnt}")

    # Define the video codec
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Video Writer
    file_path = 'captured format mp4v.mp4v'
    #    video_writer = cv2.VideoWriter(file_path, cv2.VideoWriter_fourcc('H','2','6','4'), fps, (w, h))
    video_writer = cv2.VideoWriter(file_path, fourcc, fps, (w, h))

    while cap.isOpened():
        ret, frame = cap.read()

        # Show image
#        cv2.imshow('Webcam', frame)
        video_writer.write(frame)

        # Checks whether q has been hit and stops the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    file_path = 'my_video.mp4v'
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cap.get(cv2.CAP_PROP_FOURCC)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fcnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f"cap properties - w: {w}, h: {h}, fourcc: {fourcc}, fps: {fps}, fcnt: {fcnt}")


    # Release video writer
    video_writer.release()

#--- start main stuff ---

# Connect to webcam
cap = cv2.VideoCapture(0)

#set resolution of camera
w = 1920    # 640
h = 1080    # 480

cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
cap.set(cv2.CAP_PROP_FPS, 60)
#qtake_photo()

print("Video Starting-------------------------------")
take_video()

# Releases the webcam
cap.release()
# Closes the frame
cv2.destroyAllWindows()

# capture and save video
import cv2
import os

# expects arguements
#   cam_index = 1 or 2
#   wh tuple like (w, h) or (640, 480)
#   fps   15, 30, 60
def capture_video(cam_index, wh, fps, fourcc, filename ):

    # Open the default webcam
    cam_index = 0
    cap = cv2.VideoCapture(0)

    cam_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cam_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cam_fps = cap.get(cv2.CAP_PROP_FPS)

    w, h = wh # unpack the tupple wh into it two compoents

    print(f"            PRE cap properties - cam_w: {w}, cam_h: {h}, fourcc: {fourcc}, cam_fps: {cam_fps}, cam_index: {cam_index}")

    #set the camaera to what we want
    cap.set(cv2.CAP_PROP_FPS, fps)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

    fps_after_set = int(cap.get(cv2.CAP_PROP_FPS))
    print(f"            PRE BUT AFTER SET - cam_w: {w}, cam_h: {h}, fps_after_set: {fps_after_set}")

    # Define the video codec
    fourcc = cv2.VideoWriter_fourcc(*fourcc)

    # Create a VideoWriter object to save the video
    video_writer_tuple = (h, w)   #flips height and width
    video_writer = cv2.VideoWriter(filename, fourcc, fps_after_set, video_writer_tuple)

    start_time = cv2.getTickCount()
    while True:
        ret, frame = cap.read()

#        frame = cv2.flip(frame, 0)

        rotated = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        cv2.imshow('Video Capture', rotated)

        video_writer.write(rotated)
        if (cv2.getTickCount() - start_time) / cv2.getTickFrequency() >= 4:
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fcnt = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    print(f"       POST cap properties - w: {w}, h: {h}, fps: {fps}, fcnt: {fcnt}, fourcc: {fourcc}, filename: {filename}")

    # Release the video capture and writer objects
    cap.release()
    video_writer.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


# Start capturing video
def wh_to_str(wh):
    w, h = wh
    wh_str = str(w) + "x" + str(h)
    return (wh_str)

def get_scratch_files_dir():
    cwd = os.getcwd()
    target_dir = 'pycharm code'
    while not os.path.isdir(target_dir):
        target_dir = '../' + target_dir
#        print(f"   temp: {target_dir}")

    target_dir = os.path.abspath(os.path.join(target_dir, 'scratch_files'))
#    print(target_dir)

    scratch_files_directory = target_dir +"/"
    return scratch_files_directory

###################   Main  ##################
cam_indexes_list = [0]
#cam_indexes_list = [0,1]

#wh_list = [(1920, 1080), (640, 480)]
wh_list = [(1920, 1080)]
#wh_list = [(1280, 720)]
#wh_list = [(640, 480)]

#fps_list = [30, 60]
fps_list = [60]
#fps_list = [30]


video_codecs = {
#    'MJPG': {'fourcc': 'MJPG', 'ext': 'avi', 'name': 'Motion-JPEG'},    # 3.9mb
#    'MPEG': {'fourcc': 'MPEG', 'ext': 'avi', 'name': 'MPEG-1'},         # 2.5mb  couldn't open
#    'X264': {'fourcc': 'X264', 'ext': 'mp4', 'name': 'H.264'}           # .9mb  but fell back with error message to avc1
#    'MP4V': {'fourcc': 'MP4V', 'ext': 'mp4', 'name': 'MPG Vertical'},           # didn't help at all so skipping it
    'AVC1': {'fourcc': 'avc1', 'ext': 'mp4', 'name': 'AVC1'}  # .9mb
#    'XVID': {'fourcc': 'XVID', 'ext': 'avi', 'name': 'Xvid'}            # 1.6mb  couldn't open
#    'XVIX': {'fourcc': 'XVIX', 'ext': 'avi', 'name': 'Xvix'},
#    'FLV1': {'fourcc': 'FLV1', 'ext': 'flv', 'name': 'Flash Video'},
#    'MP42': {'fourcc': 'MP42', 'ext': 'mp4', 'name': 'MPEG-4'},
#    'DIVX': {'fourcc': 'DIVX', 'ext': 'avi', 'name': 'DivX'},
#    'WMV1': {'fourcc': 'WMV1', 'ext': 'wmv', 'name': 'Windows Media Video'},
#    'WMV2': {'fourcc': 'WMV2', 'ext': 'wmv', 'name': 'Windows Media Video 9'}
}

scratch_dir = get_scratch_files_dir()
# Print the path for "scratch_files" directory
print("Path for 'scratch_files' directory:", scratch_dir)

for i in cam_indexes_list:
    print(f"\nCamera or Index: {i}")

    for key, value in video_codecs.items():
        print(f"   Video_codecs:  {key}")
        fourcc = value['fourcc']
        ext = value['ext']
        name = value['name']

        for fps in fps_list:

            str_fps = str(fps)

            for wh in wh_list:

                #get WxH string
                wh_str = wh_to_str(wh) # get string of 640x480
                filename = name + "_" + str(fps) + "_"  + fourcc + "_"  + wh_str + "." + ext

                print(f"        cam_index: {i}, Video_codecs: {key}, fource: {fourcc}, ext: {ext}, codec_name: {name}, wh: {wh}, fps {fps}, filename: {filename}")

                filename = scratch_dir + filename   # get it so that it goes in the directory
                #def capture_video(cam_index, wh, fps, fourcc, filename ):
                capture_video(i, wh, fps, fourcc, filename)



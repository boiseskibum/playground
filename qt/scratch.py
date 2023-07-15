import psutil

video_devices = psutil.video_devices()

for device in video_devices:
    print(device)
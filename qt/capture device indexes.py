import cv2

index = 0
arr = []

while True:
    print(f"checking device index: {index}")
    cap = cv2.VideoCapture(index)
    if not cap.read():
        print(f"    failed to read: {index}")
        break
    else:
        print(f"    successfully read {index}")
        arr.append(index)
    cap.release()
    index += 1

print(arr)

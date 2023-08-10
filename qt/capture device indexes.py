import cv2

index = 0
arr = []

while index < 5:
    print(f"checking device index: {index}")
    try:
        cap = cv2.VideoCapture(index)
    except:
        print(f"     exception on index {index}")

    if not cap.read():
        print(f"    failed to read: {index}")
        break
    else:
        print(f"    successfully read {index}")
        arr.append(index)
    cap.release()
    index += 1

print(arr)

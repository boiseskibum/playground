import sys
import cv2
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from threading import Thread

class VideoCaptureThread(Thread):
    def __init__(self, video_capture):
        super().__init__()
        self.video_capture = video_capture
        self.is_running = True

    def run(self):
        start_time = cv2.getTickCount()

        while self.is_running:
            ret, frame = self.video_capture.read()
            if ret:
                # Perform any processing on the frame here (if needed)

                # Convert the frame to RGB format
                rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Create QImage from RGB image
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)

                # Emit the captured frame to be displayed
                video_display.emit(q_image)

            # Check if the time limit has reached
            elapsed_time = (cv2.getTickCount() - start_time) / cv2.getTickFrequency()
            if elapsed_time >= 5.0:
                self.stop()

    def stop(self):
        self.is_running = False


class VideoDisplayWidget(QLabel):
    def __init__(self):
        super().__init__()

    def set_image(self, image):
        self.setPixmap(QPixmap.fromImage(image))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Video Capture and Display")
        self.setGeometry(100, 100, 640, 480)

        # Video display widget
        self.video_display_widget = VideoDisplayWidget()

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.video_display_widget)

        # Widget setup
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def display_video(self, image):
        self.video_display_widget.set_image(image)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create the main window
    window = MainWindow()
    window.show()

    # Create the video capture
    video_capture = cv2.VideoCapture(0)  # Change the index to the appropriate camera device (0, 1, 2, etc.)

    # Create the video capture thread
    video_capture_thread = VideoCaptureThread(video_capture)
    video_capture_thread.start()

    # Connect the video capture thread to update the video display in the GUI
    video_display = window.display_video

    # Schedule the video capture thread to stop after 5 seconds
    QTimer.singleShot(5000, video_capture_thread.stop)

    # Start the Qt event loop
    sys.exit(app.exec())

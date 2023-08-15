import sys
import cv2
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class VideoPlayerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        self.play_button = QPushButton("Play")
        self.stop_button = QPushButton("Stop")
        self.restart_button = QPushButton("Restart")
        self.next_frame_button = QPushButton("Next Frame")

        self.play_button.clicked.connect(self.play_video)
        self.stop_button.clicked.connect(self.stop_video)
        self.restart_button.clicked.connect(self.restart_video)
        self.next_frame_button.clicked.connect(self.next_frame)

        self.layout.addWidget(self.play_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.restart_button)
        self.layout.addWidget(self.next_frame_button)

        self.video_capture = cv2.VideoCapture("test_video_mp4.mp4")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.current_frame = 0

    def play_video(self):
        self.timer.start(33)  # 30 FPS

    def stop_video(self):
        self.timer.stop()

    def restart_video(self):
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.current_frame = 0

    def next_frame(self):
        self.current_frame += 1
        self.update_frame()

    def update_frame(self):
        ret, frame = self.video_capture.read()
        if ret:
            if self.current_frame > 0:
                self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
            self.current_frame += 1

            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            bytes_per_line = 3 * width

            resized_frame = cv2.resize(rgb_frame, (640, 480))
            # Display the frame in the video widget
            image = QImage(
                resized_frame,
                resized_frame.shape[1],
                resized_frame.shape[0],
                QImage.Format.Format_RGB888,
            )

#            q_image = QImage(rgb_frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

            q_pixmap = QPixmap.fromImage(image)
            self.label.setPixmap(q_pixmap)

app = QApplication(sys.argv)
window = VideoPlayerApp()
window.show()
result = app.exec()
sys.exit(result)

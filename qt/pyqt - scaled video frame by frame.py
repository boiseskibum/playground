import cv2
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.video_label1 = QLabel()
        self.video_label1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.restart_button = QPushButton("Restart")
        self.restart_button.clicked.connect(self.restart_video)

        central_layout = QVBoxLayout(self.central_widget)
        central_layout.addWidget(self.video_label1)
        central_layout.addWidget(self.restart_button)

        self.cap = cv2.VideoCapture("AVC1_30fps_vertical_sample.mp4")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_video_frame)
        self.timer.start(33)

    def update_video_frame(self):
        ret, frame = self.cap.read()

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            q_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            scaled_pixmap = QPixmap.fromImage(q_image).scaled(self.video_label1.size(), Qt.AspectRatioMode.KeepAspectRatio)
            self.video_label1.setPixmap(scaled_pixmap)
        else:
            self.timer.stop()

    def restart_video(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.timer.start()

if __name__ == "__main__":
    app = QApplication([])
    window = VideoPlayer()
    window.show()
    app.exec()

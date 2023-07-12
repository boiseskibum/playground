import sys
import cv2
from PyQt6.QtCore import Qt, QThread
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class VideoThread(QThread):
    def __init__(self, video_widget):
        super().__init__()
        self.video_widget = video_widget
        self.is_running = False

    def run(self):
        self.is_running = True
        cap = cv2.VideoCapture(0)

        # Define the video codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

        while cap.isOpened() and self.is_running:
            ret, frame = cap.read()
            if ret:
                # Convert the frame to RGB format and resize it
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                resized_frame = cv2.resize(rgb_frame, (640, 480))

                # Display the frame in the video widget
                image = QImage(
                    resized_frame,
                    resized_frame.shape[1],
                    resized_frame.shape[0],
                    QImage.Format.Format_RGB888,
                )
                pixmap = QPixmap.fromImage(image)
                self.video_widget.setPixmap(pixmap)

                # Write the frame to the video file
                out.write(frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()

    def stop(self):
        self.is_running = False


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.video_label = QLabel()

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        self.setLayout(layout)

        self.video_thread = VideoThread(self.video_label)
        self.start_button.clicked.connect(self.start_video)
        self.stop_button.clicked.connect(self.stop_video)

    def start_video(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.video_thread.start()

    def stop_video(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.video_thread.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

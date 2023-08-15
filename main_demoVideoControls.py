from demoVideoControls import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtCore import Qt, QTimer
import sys, cv2

class myWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # calls the setup methon instead of the python class created from the UI
        self.setupUi(self)

        # set up callbacks
        self.pushButton_play.clicked.connect(self.play)
        self.pushButton_forward_1.clicked.connect(self.forward_1)
        self.pushButton_forward_chunk.clicked.connect(self.forward_chunk)
        self.pushButton_stop.clicked.connect(self.stop)
        self.pushButton_rewind_1.clicked.connect(self.rewind_1)
        self.pushButton_rewind_chunk.clicked.connect(self.rewind_chunk)
        self.pushButton_rewind_to_start.clicked.connect(self.rewind_to_start)
        self.videoSlider.valueChanged.connect(self.slider_value_changed)

        #connect to video
        self.video_capture = cv2.VideoCapture("test_video.mp4")
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.current_frame = 0
        self.total_frames = int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        self.video_speed = 30   #frames per second

        self.videoSlider.setMinimum(0)
        self.videoSlider.setMaximum(self.total_frames)

        self.chunk = 10

    def play(self):
        print(f"pressed play: {self.current_frame}")
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(self.video_speed)  #FPS

    def stop(self):
        print(f"pressed stop; {self.current_frame}")
        self.timer.stop()

    def rewind_1(self):
        print(f"pressed rewind: {self.current_frame}")

        self.timer.stop()
        self.current_frame -= 2
        if self.current_frame < 0:
            self.current_frame = -1     # this is to take into account that update frame will add one to it automatically
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
        self.update_frame()

    def rewind_chunk(self):
        print(f"pressed rewind chunk: {self.current_frame}")

        self.timer.stop()
        self.current_frame -= self.chunk
        if self.current_frame < 0:
            self.current_frame = -1     # this is to take into account that update frame will add one to it automatically
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame)
        self.update_frame()

    def rewind_to_start(self):
        print(f"pressed rewind to start: {self.current_frame}")
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.current_frame = -1     #update frame will move it to frame zero
        self.update_frame()

    def forward_1(self):
        print(f"pressed forward: {self.current_frame}")
        self.timer.stop()
        self.update_frame()   #this automatically moves one step forward

    def forward_chunk(self):
        print(f"pressed forward chunk: {self.current_frame}")
        self.timer.stop()
        self.current_frame += self.chunk - 1
        if self.current_frame > self.total_frames:
            self.current_frame = self.total_frames
        self.update_frame()   #this automatically moves one step forward

    def slider_value_changed(self, value):
        print(f"slider value changed: {value}")
        self.timer.stop()
        self.current_frame = value
        self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, value)
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
            self.label_video.setPixmap(q_pixmap)


            #update the slider position
            self.videoSlider.valueChanged.disconnect(self.slider_value_changed) # disconnect the signla
            self.videoSlider.setValue(self.current_frame)
            self.videoSlider.valueChanged.connect(self.slider_value_changed)  # Reconnect the signal

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = myWindow()
    window.show()

    result = app.exec()
    sys.exit(result)

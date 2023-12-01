import cv2
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QImage, QPixmap, QPainter, QPen
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

        self.counter = 0

    def update_video_frame(self):
        ret, frame = self.cap.read()

        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame_rgb.shape
            bytes_per_line = ch * w
            q_image = QImage(frame_rgb.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
            scaled_pixmap = QPixmap.fromImage(q_image).scaled(self.video_label1.size(), Qt.AspectRatioMode.KeepAspectRatio)

            pixmap_size = scaled_pixmap.size()
            w = pixmap_size.width()
            h = pixmap_size.height()
#            print (f"h: {h}, w:{w}")

            # Create a QPainter object to draw on the QPixmap
            painter = QPainter(scaled_pixmap)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # Optional: Enable anti-aliasing for smoother lines

            # Set the line properties (e.g., color and width)

            linew = 10
            Lvalue = self.counter * 1
            Rvalue  = self.counter * -1

            penL = QPen(Qt.GlobalColor.darkGreen)  # Red color
            penL.setWidth(linew)  # Line width
            penR = QPen(Qt.GlobalColor.blue)  # Red color
            penR.setWidth(linew)  # Line width
            penH = QPen(Qt.GlobalColor.black)  # Red color
            penH.setWidth(1)  # Line width

            force_max = h/2   # this is for testing only.  will be real force when used

            def y_value_calc (pixmap_h, force_max, force):
                ratio = abs(force/force_max)   # Use absolute value as the +/- is accounted for below
                value = int(pixmap_h / 2 + force * ratio)
                return value

            l_scaled = y_value_calc(h, force_max, Lvalue)
            r_scaled = y_value_calc(h, force_max, Rvalue)

            # Draw lines on the QPixmap
            painter.setPen(penL)
            lxpos = int(linew/2)
            painter.drawLine( lxpos, int(h/2), lxpos, l_scaled )

            painter.setPen(penR)
            rxpos = w - int(linew/2)
            painter.drawLine( rxpos, int(h/2), rxpos, r_scaled )

            # horizontal lilne
            penH.setWidth(2)
            painter.setPen(penH)
            painter.drawLine( lxpos, l_scaled, rxpos, r_scaled )

            # End painting
            painter.end()


            self.video_label1.setPixmap(scaled_pixmap)
        else:
            self.timer.stop()

        self.counter += 1
    def restart_video(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.timer.start()
        self.counter = 0

if __name__ == "__main__":
    app = QApplication([])
    window = VideoPlayer()
    window.show()
    app.exec()

# pyqt6 example code to display a video, both avi and mpeg4. add a slider bar to the bottom of the window to set the
# location with the video.   Also add a start and stop button for the video
import os
import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSlider, QPushButton
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget

class VideoPlayerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 800, 600)  # (x, y, width, height)

        # Create the slider bar
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_media_position)

        # Create the start and stop buttons
        self.start_button = QPushButton('Start')
        self.stop_button = QPushButton('Stop')
        self.start_button.clicked.connect(self.start_video)
        self.stop_button.clicked.connect(self.stop_video)

        # Create the video widget
        self.video_widget = QVideoWidget()


        # Create the layout and add the widgets
        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.stop_button)
        layout.addWidget(self.slider)
        layout.addWidget(self.video_widget)

        # Create the media player
        self.media_player = QMediaPlayer(self)
        self.media_player.setVideoOutput(self.video_widget)

#        self.setLayout(layout)

        # Create a container widget and set the layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

#        container.setLayout(layout)
#        self.setCentralWidget(container)
#        self.setCentralWidget(self.video_widget)

    def start_video(self):
        print("start_video function")
        video_file = 'AVC1_30fps_vertical_sample.mp4'  # Replace with the path to your video file
        if os.path.isfile('file.txt'):
            print(f"file exists:  {video_file}")
        else:
            print(f"file doesn't exist:  {video_file}")
        # video_file = 'path/to/video/file.mp4'  # Replace with the path to your video file
        content = QUrl(video_file)
        self.media_player.setSource(content)
        self.media_player.play()

    def stop_video(self):
        self.media_player.stop()

    def set_media_position(self, position):
        self.media_player.setPosition(position)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoPlayerWindow()
    window.show()
    app.exec()
    sys.exit()

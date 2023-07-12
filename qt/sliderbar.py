import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget


class SliderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Slider Example")
        self.setGeometry(100, 100, 400, 100)

        # Slider widget
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)  # Set orientation to horizontal
        self.slider.setRange(0, 99)  # Set the range from 0 to 99

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.slider)

        # Widget setup
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SliderWindow()
    window.show()

    sys.exit(app.exec())

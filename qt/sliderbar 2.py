import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QSlider, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class SliderWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Window setup
        self.setWindowTitle("Slider Example")
        self.setGeometry(100, 100, 400, 200)

        # Slider widget
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(99)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.valueChanged.connect(self.slider_value_changed)

        # Value label
        self.value_label = QLabel("0")
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.value_label)

        # Widget setup
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def slider_value_changed(self, value):
        self.value_label.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SliderWindow()
    window.show()

    sys.exit(app.exec())

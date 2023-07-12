import sys
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QSlider
from PyQt6.QtWidgets import QLabel

class SpeedometerWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 200)
        self.value = 0

    def setValue(self, value):
        self.value = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        width = self.width()
        height = self.height()

        # Draw background circle
        painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
        painter.drawEllipse(10, 10, width - 20, height - 20)

        # Calculate angle for current value
        angle = (270 - (self.value / 75) * 270) * 16

        # Draw speedometer dial
        painter.setPen(QPen(Qt.GlobalColor.green, 12, Qt.PenStyle.SolidLine))
        painter.drawArc(20, 20, width - 40, height - 40, 30 * 16, 120 * 16)

        # Draw needle
        painter.setPen(QPen(QColor(255, 0, 0), 5, Qt.PenStyle.SolidLine))
        painter.save()
        painter.translate(width / 2, height / 2)
        painter.rotate(angle / 16)
        painter.drawLine(0, 0, (width - 40) / 2, 0)
        painter.restore()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Speedometer Widget")

        self.speedometer_widget = SpeedometerWidget()

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 75)
        self.slider.valueChanged.connect(self.speedometer_widget.setValue)

        layout = QVBoxLayout()
        layout.addWidget(self.speedometer_widget)
        layout.addWidget(self.slider)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

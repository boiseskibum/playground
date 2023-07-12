import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtGui import QPixmap, QImage

class ImageViewerWindow(QMainWindow):
    def __init__(self, image_path):
        super().__init__()

        # Window setup
        self.setWindowTitle("Image Viewer")
        self.setGeometry(100, 100, 400, 300)

        # Image widget
        self.image_label = QLabel()
        self.load_image(image_path)

        # Calculate image ratio from the file
        image = QImage(image_path)
        ratio = image.width() / image.height()

        # Set fixed size with ratio
        desired_height = 400
        desired_width = int(desired_height * ratio)
        self.image_label.setFixedSize(desired_width, desired_height)


        # Close button
        self.close_button = QPushButton("Close")
        self.close_button.clicked.connect(self.close)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.close_button)

        # Widget setup
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def load_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Provide the path to the JPEG file
    image_path = "KallieAndSteve.jpg"
    image_path = 'duck hunt steve.jpg'
    image_path = 'zebra.jpg'

    window = ImageViewerWindow(image_path)
    window.show()

    sys.exit(app.exec())

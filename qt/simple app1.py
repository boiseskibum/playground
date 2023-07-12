from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.setWindowTitle('PyQt6 Image Example')

        # Create a label widget to display the image
        label = QLabel(self)

        # Load the image into a QPixmap object
        # pixmap = QPixmap('zebra.jpg')
        # pixmap = QPixmap('duck hunt steve.jpg')
        pixmap = QPixmap('KallieAndSteve.jpg')

        # Set the pixmap onto the label widget
        label.setPixmap(pixmap)

        # Resize the window to fit the image size
        self.resize(pixmap.width(), pixmap.height())

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


import os
from PyQt6.QtPdf import QPdfDocument
from PyQt6.QtPdfWidgets import QPdfView
from PyQt6.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "example.pdf"))
        document = QPdfDocument(self)
        document.load(file_path)
        view = QPdfView(None)
        view.setPageMode(QPdfView.PageMode.MultiPage)
        view.setDocument(document)

        layout = QVBoxLayout()
        layout.addWidget(view)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


app = QApplication([])
window = MainWindow()
app.exec()
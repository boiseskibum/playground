import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextBrowser, QVBoxLayout, QWidget, QPushButton
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices

import subprocess
import os

class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # Create a QTextBrowser widget
        self.text_browser = QTextBrowser()

        # Load the PDF file when the button is clicked
        self.load_button = QPushButton("Load PDF")
        self.load_button.clicked.connect(self.loadPDF)

        layout.addWidget(self.load_button)
        layout.addWidget(self.text_browser)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(100, 100, 800, 600)

    def loadPDF(self):
        # Path to the PDF file
        pdf_file_path = "example.pdf"
        pdf_file_path = "zebra.jpg"

        if os.path.exists(pdf_file_path):
            print(f"The file {pdf_file_path} exists.")
        else:
            print(f"The file {pdf_file_path} does not exist.")

        # Open the PDF file using the default PDF viewer
#        QDesktopServices.openUrl(QUrl.fromLocalFile(file_path))

        # Make sure the file path is absolute
        absolute_pdf_path = os.path.abspath(pdf_file_path)
        print(f'Absolute path is: {absolute_pdf_path}')

        # Use the 'open' command to open the file with its default application
        subprocess.run(["open", absolute_pdf_path])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDFViewer()
    window.show()
    sys.exit(app.exec())

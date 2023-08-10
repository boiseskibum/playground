from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QFrame
from PyQt6.QtGui import QPainter, QPen, QFont
from PyQt6.QtCore import Qt, QRect


class GraphCanvas(QFrame):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Example code for drawing a graph on the canvas
        rect = self.contentsRect()
        x = rect.left()
        y = rect.top()
        width = rect.width()
        height = rect.height()

        painter.setPen(QPen(Qt.GlobalColor.blue, 2.0))
        painter.setBrush(Qt.GlobalColor.lightBlue)
        painter.drawRect(x, y, width, height)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Grid Layout Example")
        self.setGeometry(300, 300, 400, 300)

        # Create the central widget and grid layout
        central_widget = QWidget()
        grid_layout = QGridLayout(central_widget)
        self.setCentralWidget(central_widget)

        # Create buttons and input fields
        for row in range(3):
            for col in range(3):
                button = QPushButton(f"Button {row + 1}-{col + 1}")
                line_edit = QLineEdit()

                grid_layout.addWidget(button, row, col)
                grid_layout.addWidget(line_edit, row, col)

        # Create a graph canvas that spans all 3 columns
        graph_canvas = GraphCanvas()
        grid_layout.addWidget(graph_canvas, 0, 0, 3, 3)

        # Set the grid layout as the central layout
        central_widget.setLayout(grid_layout)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()

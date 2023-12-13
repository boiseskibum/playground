from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QSize
import sys

# Initialize the application
app = QApplication(sys.argv)

# Create main window
window = QWidget()
layout = QVBoxLayout()

# Create a button
button = QPushButton("Click Me")
# Set an icon
button.setIcon(QIcon("jt.png"))
# Optionally set the icon size
button.setIconSize(QPixmap("jt.png").size())

# Add the button to the layout
layout.addWidget(button)

# Set the layout for the main window
window.setLayout(layout)
window.show()

# Run the application
sys.exit(app.exec())

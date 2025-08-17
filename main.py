import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        self.button = QPushButton("Press Me!")
        self.button.setFixedWidth(200)
        self.button.setFixedHeight(100)
        self.button.setStyleSheet("font-size: 20px;")
        self.setMinimumSize(QSize(400, 300))
        self.ticket_desc_box = QTextEdit(self)
        self.ticket_desc_box.setPlaceholderText("Enter ticket description here...")
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()





app.exec()

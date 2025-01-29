# main_window.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set it as the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout and add widgets
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Button to open the child window
        self.open_child_button = QPushButton("Open Child Window")
        layout.addWidget(self.open_child_button)
        self.open_child_button.clicked.connect(self.open_child_window)

    def set_child_window(self, child_window):
        self.child_window = child_window

    def open_child_window(self):
        self.child_window.show()
        self.hide()
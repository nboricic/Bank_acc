# child_window.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout

class ChildWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Child Window")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set it as the central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a layout and add widgets
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Button to return to the main window
        self.return_button = QPushButton("Return to Main Window")
        layout.addWidget(self.return_button)
        self.return_button.clicked.connect(self.return_to_main)

    def set_main_window(self, main_window):
        self.main_window = main_window

    def return_to_main(self):
        self.main_window.show()
        self.hide()
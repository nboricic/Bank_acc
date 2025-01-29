# main.py
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow
from child_window import ChildWindow
import sys

class App:
    def __init__(self):
        self.app = QApplication(sys.argv)
        
        # Create instances of the windows
        self.main_window = MainWindow()
        self.child_window = ChildWindow()

        # Set up parent-child relationships
        self.main_window.set_child_window(self.child_window)
        self.child_window.set_main_window(self.main_window)

        # Show the main window
        self.main_window.show()
        sys.exit(self.app.exec_())

if __name__ == "__main__":
    app = App()
import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = False

        self.setWindowTitle("My App")

        self.setMinimumSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")

        self.button.setChecked = True
        self.button.setEnabled = False

        print("Lock")


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

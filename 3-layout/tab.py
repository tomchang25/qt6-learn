import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedLayout,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.West)
        tabs.setMovable(True)

        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(Color("red"))
        tab2_layout.addWidget(Color("yellow"))
        tab2_layout.addWidget(Color("purple"))
        tab2.setLayout(tab2_layout)

        tab1 = QWidget()

        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        main_layout = QHBoxLayout()

        layout2 = QVBoxLayout()
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("yellow"))
        layout2.addWidget(Color("purple"))
        main_layout.addLayout(layout2)

        # layout_s = QStackedLayout()
        # layout_s.addWidget(Color("red"))
        # layout_s.addWidget(Color("green"))
        # layout_s.addWidget(Color("blue"))
        # layout_s.addWidget(Color("yellow"))
        # # layout_s.setCurrentIndex(3)
        # layout_s.setCurrentWidget(layout_s.widget(2))
        # main_layout.addLayout(layout_s)

        layout3 = QVBoxLayout()
        layout3.addWidget(Color("red"))
        layout3.addWidget(Color("purple"))
        main_layout.addLayout(layout3)

        layout4 = QGridLayout()
        layout4.addWidget(Color("red"), 0, 0)
        layout4.addWidget(Color("green"), 1, 0)
        layout4.addWidget(Color("blue"), 1, 1)
        layout4.addWidget(Color("purple"), 2, 1)
        main_layout.addLayout(layout4)

        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(20)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        self.setMinimumSize(1280, 720)
        self.setWindowTitle("My App")


class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

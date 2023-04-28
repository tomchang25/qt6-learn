import sys

from PyQt6.QtCore import QSize, Qt, QPoint
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu
from PyQt6 import QtWidgets


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")

        self.setMinimumSize(QSize(400, 300))

        # Set the central widget of the Window.
        self.label = QtWidgets.QLabel("TEst")
        self.text_input = QtWidgets.QLineEdit()
        self.text_input.textChanged.connect(self.label.setText)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)

        container = QtWidgets.QWidget()
        container.setLayout(layout)
        self.setMouseTracking(True)

        self.text_input.mouseReleaseEvent = self.on_mouse_release

        self.text_input.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.text_input.customContextMenuRequested.connect(self.on_context_menu)

        self.setCentralWidget(container)

    def on_mouse_release(self, e):
        if e.button() == Qt.MouseButton.MiddleButton:
            self.text_input.customContextMenuRequested.emit(e.pos())

    def on_context_menu(self, pos):
        context = QMenu(self)
        context.addAction(QAction("test A", self))
        context.addAction(QAction("test B", self))
        context.addAction(QAction("test C", self))

        # Convert the global mouse position to a local position relative to the parent widget
        local_pos = self.text_input.mapToGlobal(pos)
        print(pos, self.text_input.mapToGlobal(pos), local_pos)

        # Position the context menu next to the text input widget
        # context_pos = self.text_input.mapToGlobal(QPoint(0, 0)) + local_pos
        context.exec(local_pos)

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            # handle the left-button press in here
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            # handle the middle-button press in here.
            self.label.setText("mousePressEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            # handle the right-button press in here.
            self.label.setText("mousePressEvent RIGHT")

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseReleaseEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseReleaseEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseReleaseEvent RIGHT")

    def mouseDoubleClickEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText("mouseDoubleClickEvent LEFT")

        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText("mouseDoubleClickEvent MIDDLE")

        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText("mouseDoubleClickEvent RIGHT")

    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

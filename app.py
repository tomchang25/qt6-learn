from PyQt6 import QtCore, QtGui, QtWidgets
from utils.color import Color
from vertical_tab.v1 import TabWidget


class Template(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        tab1 = QtWidgets.QWidget()
        tab1_layout = QtWidgets.QHBoxLayout()
        tab1_layout.addWidget(Color("yellow"))
        tab1_layout.addWidget(Color("red"))
        tab1.setLayout(tab1_layout)

        tab2 = QtWidgets.QWidget()
        tab2_layout = QtWidgets.QVBoxLayout()
        tab2_layout.addWidget(Color("red"))
        tab2_layout.addWidget(Color("yellow"))
        tab2_layout.addWidget(Color("purple"))
        tab2.setLayout(tab2_layout)

        tab3 = QtWidgets.QWidget()
        tab3_layout = QtWidgets.QStackedLayout()
        tab3_layout.addWidget(Color("red"))
        tab3_layout.addWidget(Color("yellow"))
        tab3_layout.addWidget(Color("purple"))
        tab3.setLayout(tab3_layout)

        tab = TabWidget()
        tab.addTab(tab1, QtGui.QIcon("files/project.png"), "Project")
        tab.addTab(tab2, QtGui.QIcon("files/transcribe.png"), "Transcribe")
        tab.addTab(tab3, QtGui.QIcon("files/translate.png"), "Translate")
        # tab.setStyleSheet(
        #     """
        # TabWidget::tab-bar {
        #     alignment: left;
        # }"""
        # )

        grid = QtWidgets.QGridLayout(self)
        grid.addWidget(tab)

        self.resize(640, 480)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # app.setStyle("Oxygen")
    window = Template()
    window.show()
    sys.exit(app.exec())

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabBar, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
import sys


class MyTabBar(QTabBar):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # add some tabs to the tab bar
        self.addTab("Tab 1")
        self.addTab("Tab 2")
        self.addTab("Tab 3")

        # connect the tabBarClicked signal to a slot
        self.tabBarClicked.connect(self.handleTabBarClicked)

    def handleTabBarClicked(self, index):
        # print the index of the clicked tab
        print(f"Clicked tab: {index}")


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # create a central widget for the main window
        central_widget = QWidget()
        central_layout = QVBoxLayout()
        central_widget.setLayout(central_layout)

        # create a custom tab bar and add it to the central widget
        tab_bar = MyTabBar()
        central_layout.addWidget(tab_bar)

        # create some widgets to add to the tabs
        tab1_widget = QWidget()
        tab1_layout = QVBoxLayout()
        tab1_layout.addWidget(QPushButton("Button 1"))
        tab1_layout.addWidget(QPushButton("Button 2"))
        tab1_widget.setLayout(tab1_layout)

        tab2_widget = QWidget()
        tab2_layout = QVBoxLayout()
        tab2_layout.addWidget(QPushButton("Button 3"))
        tab2_layout.addWidget(QPushButton("Button 4"))
        tab2_widget.setLayout(tab2_layout)

        tab3_widget = QWidget()
        tab3_layout = QVBoxLayout()
        tab3_layout.addWidget(QPushButton("Button 5"))
        tab3_layout.addWidget(QPushButton("Button 6"))
        tab3_widget.setLayout(tab3_layout)

        # tab_bar.addTab("Tab 1")
        # tab_bar.addTab("Tab 2")
        # tab_bar.addTab("Tab 3")
        tab_bar.setTabToolTip(0, "Tooltip for Tab 1")
        tab_bar.setTabToolTip(1, "Tooltip for Tab 2")
        tab_bar.setTabToolTip(2, "Tooltip for Tab 3")

        # set the central widget of the main window
        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())

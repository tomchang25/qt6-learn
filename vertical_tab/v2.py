from PyQt6 import QtCore, QtGui, QtWidgets


class Color(QtWidgets.QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QtGui.QPalette.ColorRole.Window, QtGui.QColor(color))
        self.setPalette(palette)


class TabBar(QtWidgets.QTabBar):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.tabBarSize = QtCore.QSize(120, 40)
        self.hoverColor = QtGui.QColor(255, 0, 255)
        self.selectedColor = QtGui.QColor(0, 255, 255)

    def tabSizeHint(self, index):
        return self.tabBarSize

    def paintEvent(self, event: QtGui.QPaintEvent):
        painter_style = QtWidgets.QStylePainter(self)
        painter_qp = QtGui.QPainter(self)
        option_style = QtWidgets.QStyleOptionTab()

        for index in range(self.count()):
            self.initStyleOption(option_style, index)
            tab_rect = self.tabRect(index)

            # Hover check
            if self.tabRect(index).contains(self.mapFromGlobal(QtGui.QCursor.pos())):
                painter_qp.fillRect(tab_rect, self.hoverColor)

            # Click check
            if self.currentIndex() == index:
                painter_qp.fillRect(tab_rect, self.selectedColor)

            # Draw the tabbar
            painter_style.save()

            s = option_style.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(option_style.rect.center())

            option_style.rect = r

            c = tab_rect.center()
            painter_style.translate(c)
            painter_style.rotate(90)
            painter_style.translate(-c)
            painter_style.drawControl(QtWidgets.QStyle.ControlElement.CE_TabBarTabLabel, option_style)

            painter_style.restore()


class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        self.setTabBar(TabBar(self))
        self.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    # QtWidgets.QApplication.setStyle(ProxyStyle())

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

    w = TabWidget()
    w.addTab(tab1, QtGui.QIcon("zoom.png"), "ABC")
    w.addTab(tab2, QtGui.QIcon("zoom-in.png"), "ABCDEFGH")
    w.addTab(tab3, QtGui.QIcon("zoom-out.png"), "XYZ")

    w.resize(640, 480)
    w.show()

    sys.exit(app.exec())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainGui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Afropony(object):
    def setupUi(self, Afropony):
        Afropony.setObjectName("Afropony")
        Afropony.resize(780, 500)
        Afropony.setMinimumSize(QtCore.QSize(780, 500))
        Afropony.setMaximumSize(QtCore.QSize(780, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Afropony.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Afropony)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-40, -110, 881, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Watch_Dogs - Dedsec Street Art by Patrick Desgreniers, Sidonie Weber, Mathieu Leduc.jpg"))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, -10, 221, 21))
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(110, 0, 221, 481))
        self.line_2.setLineWidth(2)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-10, 0, 231, 491))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/Loading.gif"))
        self.label_2.setObjectName("label_2")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 220, 481))
        self.scrollArea.setMaximumSize(QtCore.QSize(220, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 220, 481))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(200, 0, 20, 481))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        Afropony.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Afropony)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        Afropony.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Afropony)
        self.statusbar.setObjectName("statusbar")
        Afropony.setStatusBar(self.statusbar)

        self.retranslateUi(Afropony)
        QtCore.QMetaObject.connectSlotsByName(Afropony)

    def retranslateUi(self, Afropony):
        _translate = QtCore.QCoreApplication.translate
        Afropony.setWindowTitle(_translate("Afropony", "Afropony"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Afropony = QtWidgets.QMainWindow()
    ui = Ui_Afropony()
    ui.setupUi(Afropony)
    Afropony.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        MainWindow.setMinimumSize(QtCore.QSize(900, 600))
        MainWindow.setMaximumSize(QtCore.QSize(900, 600))
        MainWindow.setWindowTitle("Kenshi Mod Manager")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Netherlands))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 598))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.listWidget = QtWidgets.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.listWidget.setDragEnabled(True)
        self.listWidget.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.listWidget.setDefaultDropAction(QtCore.Qt.TargetMoveAction)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.listWidget.setObjectName("listWidget")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.playButton = QtWidgets.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(740, 531, 151, 61))
        self.playButton.setObjectName("playButton")
        self.configButton = QtWidgets.QPushButton(self.centralwidget)
        self.configButton.setGeometry(QtCore.QRect(575, 531, 151, 61))
        self.configButton.setObjectName("configButton")
        self.rootPath = QtWidgets.QLineEdit(self.centralwidget)
        self.rootPath.setGeometry(QtCore.QRect(455, 70, 400, 20))
        self.rootPath.setObjectName("rootPath")
        self.workshopPath = QtWidgets.QLineEdit(self.centralwidget)
        self.workshopPath.setGeometry(QtCore.QRect(455, 180, 400, 20))
        self.workshopPath.setObjectName("workshopPath")
        self.rootLabel = QtWidgets.QLabel(self.centralwidget)
        self.rootLabel.setGeometry(QtCore.QRect(460, 20, 391, 51))
        self.rootLabel.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.rootLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.rootLabel.setTextFormat(QtCore.Qt.AutoText)
        self.rootLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rootLabel.setWordWrap(False)
        self.rootLabel.setObjectName("rootLabel")
        self.workshopLabel = QtWidgets.QLabel(self.centralwidget)
        self.workshopLabel.setGeometry(QtCore.QRect(460, 99, 391, 81))
        self.workshopLabel.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.workshopLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.workshopLabel.setTextFormat(QtCore.Qt.AutoText)
        self.workshopLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.workshopLabel.setWordWrap(False)
        self.workshopLabel.setObjectName("workshopLabel")
        self.pathButton = QtWidgets.QPushButton(self.centralwidget)
        self.pathButton.setGeometry(QtCore.QRect(410, 531, 151, 61))
        self.pathButton.setObjectName("pathButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.playButton.setText(_translate("MainWindow", "Play"))
        self.configButton.setText(_translate("MainWindow", "Save Config"))
        self.rootLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Root Path</span><br/><br/>Put the root folder of kenshi here (Where the exe of kenshi is located) </p></body></html>"))
        self.workshopLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Workshop Path<br/></span><br/>Put the folder where your kenshi workshop mods are located, usually it\'s in:</p><p>&lt;WhereSteamIs&gt;/steamapps/workshop/content/233860 </p></body></html>"))
        self.pathButton.setText(_translate("MainWindow", "Save paths"))

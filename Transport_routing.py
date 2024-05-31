# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Transport_routing.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 650)
        MainWindow.setMaximumSize(QSize(1000000, 1000000))
        MainWindow.setStyleSheet(u"background-color:rgba(0, 0, 15, 30);\n"
"font-family: Noto Sans SC")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(569, -1, 231, 281))
        self.frame.setStyleSheet(u"background-color: rgb(11, 7, 17);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 231, 41))
        self.label.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 243, 211, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(35, 32, 39);")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 80, 211, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(32, 30, 45);")
        self.lineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 150, 211, 31))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(32, 30, 45);")
        self.lineEdit_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(10, 210, 211, 31))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(32, 30, 45);")
        self.lineEdit_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 180, 231, 31))
        self.label_6.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_6.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label_6.setTextFormat(Qt.TextFormat.RichText)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 110, 231, 31))
        self.label_7.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_7.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label_7.setTextFormat(Qt.TextFormat.RichText)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 50, 231, 31))
        self.label_8.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_8.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label_8.setTextFormat(Qt.TextFormat.RichText)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(569, 279, 231, 371))
        self.frame_2.setStyleSheet(u"background-color: rgb(11, 7, 17);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_4 = QLineEdit(self.frame_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(10, 80, 211, 31))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(32, 30, 45);")
        self.lineEdit_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_5 = QLineEdit(self.frame_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(10, 190, 211, 31))
        self.lineEdit_5.setStyleSheet(u"background-color: rgb(32, 30, 45);")
        self.lineEdit_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lineEdit_6 = QLineEdit(self.frame_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(10, 300, 211, 31))
        self.lineEdit_6.setStyleSheet(u"background-color: rgb(32, 30, 45);")
        self.lineEdit_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 231, 41))
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label_2.setTextFormat(Qt.TextFormat.RichText)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(10, 120, 211, 31))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(35, 32, 39);")
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 230, 211, 31))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(35, 32, 39);")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 50, 231, 31))
        self.label_3.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_3.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label_3.setTextFormat(Qt.TextFormat.RichText)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 160, 231, 31))
        self.label_4.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label_4.setTextFormat(Qt.TextFormat.RichText)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 270, 231, 31))
        self.label_5.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_5.setStyleSheet(u"color: white;\n"
"font-weight: bold;\n"
"font-size: 10pt;\n"
"background-color:none;\n"
"border: none")
        self.label_5.setTextFormat(Qt.TextFormat.RichText)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(10, 340, 211, 31))
        self.pushButton_4.setStyleSheet(u"background-color: rgb(35, 32, 39);")
        self.webEngineContainer = QWidget(self.centralwidget)
        self.webEngineContainer.setObjectName(u"webEngineContainer")
        self.webEngineContainer.setGeometry(QRect(0, 0, 571, 651))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Transport routing", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0434\u043e\u0441\u0442\u0430\u0432\u043a\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u0435\u043d\u043d\u043e\u0439 \u0438\u043d\u0442\u0435\u0440\u0432\u0430\u043b", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0435\u0441 \u0433\u0440\u0443\u0437\u0430", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b", None))
        self.lineEdit_4.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u043a\u043b\u0430\u0434\u0430", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043c\u0430\u0448\u0438\u043d", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u0437\u043e\u043f\u043e\u0434\u044c\u0435\u043c\u043d\u043e\u0441\u0442\u044c \u043c\u0430\u0448\u0438\u043d\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u0434\u0435\u043f\u043e", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi




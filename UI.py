# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledMtotOJ.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(1024, 768))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.OpenDB = QAction(MainWindow)
        self.OpenDB.setObjectName(u"OpenDB")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.ExportDB = QAction(MainWindow)
        self.ExportDB.setObjectName(u"ExportDB")
        self.SaveExcel = QAction(MainWindow)
        self.SaveExcel.setObjectName(u"SaveExcel")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1021, 721))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.AirportSelect = QListView(self.tab)
        self.AirportSelect.setObjectName(u"AirportSelect")
        self.AirportSelect.setGeometry(QRect(10, 30, 81, 91))
        self.AirportSelect.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 91, 16))
        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(140, 30, 21, 16))
        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 60, 121, 16))
        self.label_4 = QLabel(self.tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(140, 90, 54, 12))
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(140, 120, 91, 16))
        self.label_6 = QLabel(self.tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 150, 101, 16))
        self.label_7 = QLabel(self.tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 180, 91, 16))
        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(140, 210, 61, 16))
        self.label_9 = QLabel(self.tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 240, 61, 16))
        self.label_10 = QLabel(self.tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(140, 270, 61, 16))
        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(140, 300, 81, 16))
        self.AirportID = QLineEdit(self.tab)
        self.AirportID.setObjectName(u"AirportID")
        self.AirportID.setGeometry(QRect(290, 30, 113, 20))
        self.AirportName = QLineEdit(self.tab)
        self.AirportName.setObjectName(u"AirportName")
        self.AirportName.setGeometry(QRect(290, 60, 113, 20))
        self.AirportICAO = QLineEdit(self.tab)
        self.AirportICAO.setObjectName(u"AirportICAO")
        self.AirportICAO.setGeometry(QRect(290, 90, 113, 20))
        self.AirportLat = QLineEdit(self.tab)
        self.AirportLat.setObjectName(u"AirportLat")
        self.AirportLat.setGeometry(QRect(290, 120, 113, 20))
        self.AirportLongt = QLineEdit(self.tab)
        self.AirportLongt.setObjectName(u"AirportLongt")
        self.AirportLongt.setGeometry(QRect(290, 150, 113, 20))
        self.AirportElv = QLineEdit(self.tab)
        self.AirportElv.setObjectName(u"AirportElv")
        self.AirportElv.setGeometry(QRect(290, 180, 113, 20))
        self.AirportTA = QLineEdit(self.tab)
        self.AirportTA.setObjectName(u"AirportTA")
        self.AirportTA.setGeometry(QRect(290, 210, 113, 20))
        self.AirportTL = QLineEdit(self.tab)
        self.AirportTL.setObjectName(u"AirportTL")
        self.AirportTL.setGeometry(QRect(290, 240, 113, 20))
        self.AirportSpd = QLineEdit(self.tab)
        self.AirportSpd.setObjectName(u"AirportSpd")
        self.AirportSpd.setGeometry(QRect(290, 270, 113, 20))
        self.AirportSpdH = QLineEdit(self.tab)
        self.AirportSpdH.setObjectName(u"AirportSpdH")
        self.AirportSpdH.setGeometry(QRect(290, 300, 113, 20))
        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(140, 330, 151, 16))
        self.AirportAC = QLineEdit(self.tab)
        self.AirportAC.setObjectName(u"AirportAC")
        self.AirportAC.setGeometry(QRect(290, 330, 113, 20))
        self.label_24 = QLabel(self.tab)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(140, 360, 71, 16))
        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(140, 390, 141, 16))
        self.AirportAICAO = QLineEdit(self.tab)
        self.AirportAICAO.setObjectName(u"AirportAICAO")
        self.AirportAICAO.setGeometry(QRect(290, 360, 113, 20))
        self.AirportCom = QLineEdit(self.tab)
        self.AirportCom.setObjectName(u"AirportCom")
        self.AirportCom.setGeometry(QRect(290, 390, 113, 20))
        self.label_26 = QLabel(self.tab)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(140, 420, 141, 16))
        self.AirportFreq = QLineEdit(self.tab)
        self.AirportFreq.setObjectName(u"AirportFreq")
        self.AirportFreq.setGeometry(QRect(290, 420, 113, 20))
        self.label_27 = QLabel(self.tab)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(140, 450, 141, 16))
        self.AirportFreqUnit = QLineEdit(self.tab)
        self.AirportFreqUnit.setObjectName(u"AirportFreqUnit")
        self.AirportFreqUnit.setGeometry(QRect(290, 450, 113, 20))
        self.label_44 = QLabel(self.tab)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setGeometry(QRect(140, 480, 141, 16))
        self.AirportSI = QLineEdit(self.tab)
        self.AirportSI.setObjectName(u"AirportSI")
        self.AirportSI.setGeometry(QRect(290, 480, 113, 20))
        self.RunwaySelect = QListView(self.tab)
        self.RunwaySelect.setObjectName(u"RunwaySelect")
        self.RunwaySelect.setGeometry(QRect(460, 30, 81, 91))
        self.label_45 = QLabel(self.tab)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(460, 10, 91, 16))
        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 540, 1001, 21))
        self.SaveAirport = QPushButton(self.tab)
        self.SaveAirport.setObjectName(u"SaveAirport")
        self.SaveAirport.setGeometry(QRect(10, 130, 81, 23))
        self.SaveRunway = QPushButton(self.tab)
        self.SaveRunway.setObjectName(u"SaveRunway")
        self.SaveRunway.setGeometry(QRect(460, 130, 81, 23))
        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 560, 1001, 21))
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1024, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.label_2.setBuddy(self.AirportID)
        self.label_3.setBuddy(self.AirportName)
        self.label_4.setBuddy(self.AirportICAO)
        self.label_5.setBuddy(self.AirportLat)
        self.label_6.setBuddy(self.AirportLongt)
        self.label_7.setBuddy(self.AirportElv)
        self.label_8.setBuddy(self.AirportTA)
        self.label_9.setBuddy(self.AirportTL)
        self.label_10.setBuddy(self.AirportSpd)
        self.label_11.setBuddy(self.AirportSpdH)
        self.label_23.setBuddy(self.AirportAC)
        self.label_24.setBuddy(self.AirportAICAO)
        self.label_25.setBuddy(self.AirportCom)
        self.label_26.setBuddy(self.AirportFreq)
        self.label_27.setBuddy(self.AirportFreqUnit)
        self.label_44.setBuddy(self.AirportSI)
#endif // QT_CONFIG(shortcut)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.OpenDB)
        self.menu.addAction(self.SaveExcel)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fenix A320 \u5bfc\u822a\u6570\u636e\u7f16\u8f91\u5668", None))
        self.OpenDB.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u673a\u573a", None))
        self.ExportDB.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.SaveExcel.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u4e00\u4e2a\u673a\u573a\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u673a\u573a\u540d\u5b57(\u5927\u5199\u62fc\u97f3)\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ICAO\u4ee3\u7801\uff1a", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7eac\u5ea6(Latitude)\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7ecf\u5ea6(Longtitude)\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u673a\u573a\u6807\u9ad8(\u82f1\u5c3a)\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"TA(\u82f1\u5c3a)\uff1a", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"TL(\u82f1\u5c3a)\uff1a", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6\u9650\u5236\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u901f\u5ea6\u9650\u5236\u9ad8\u5ea6\uff1a", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u673a\u573a\u5730\u533a\u4ee3\u7801(\u4e2d\u56fd\u4e3aEEU)\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u60c5\u62a5\u533a\u4ee3\u7801\uff1a", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u901a\u4fe1\u65b9\u5f0f(\u597d\u50cf\u90fd\u586bTWR?)\uff1a", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u901a\u4fe1\u9891\u7387\uff1a", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u9891\u7387\u5355\u4f4d\uff1f(\u597d\u50cf\u90fd\u662fV)\uff1a", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u6807\u5fd7\uff1f(\u53ef\u4ee5\u4e0d\u586b\uff1f)\uff1a", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u8dd1\u9053\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u4f7f\u7528\u8bf4\u660e\uff1a\u4fee\u6539\u673a\u573a\u8bf7\u5148\u9009\u62e9\u4e00\u4e2a\u673a\u573a\uff0c\u7136\u540e\u5728\u539f\u6709\u7684\u57fa\u7840\u4e0a\u4fee\u6539\uff0c\u6ce8\u610f\u4e0d\u8981\u6539ID\uff0c\u4e0d\u7136\u53ef\u80fd\u5728\u5bfc\u5165\u7684\u65f6\u5019\u6ca1\u529e\u6cd5\u8986\u76d6\uff0c\u65b0\u5efa\u4e5f\u662f\u4e00\u6837\u76f4\u63a5\u586b\u5c31\u884c\uff0c\u586b\u5b8c\u70b9\u4fdd\u5b58\u4fee\u6539\u3002", None))
        self.SaveAirport.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fee\u6539", None))
        self.SaveRunway.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u4fee\u6539", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u5b8c\u6210\u4ee5\u540e\u70b9\u51fb\u83dc\u5355-\u4fdd\u5b58\uff0c\u7136\u540e\u6b64\u7a0b\u5e8f\u540c\u76ee\u5f55\u4e0b\u5c31\u4f1a\u51fa\u73b0Result.xls\uff0c\u7528Navicat\u5bfc\u5165\u5373\u53ef", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u673a\u573a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u9875", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u83dc\u5355", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi


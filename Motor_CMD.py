# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Motor_CMD.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(587, 709)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_17.setObjectName(_fromUtf8("verticalLayout_17"))
        self.how_to_label = QtGui.QLabel(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.how_to_label.setFont(font)
        self.how_to_label.setObjectName(_fromUtf8("how_to_label"))
        self.verticalLayout_17.addWidget(self.how_to_label)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem2)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.tab_4)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.tab_4)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.filename_display = QtGui.QLineEdit(self.tab_4)
        self.filename_display.setReadOnly(True)
        self.filename_display.setObjectName(_fromUtf8("filename_display"))
        self.horizontalLayout.addWidget(self.filename_display)
        self.browse_button = QtGui.QPushButton(self.tab_4)
        self.browse_button.setObjectName(_fromUtf8("browse_button"))
        self.horizontalLayout.addWidget(self.browse_button)
        self.verticalLayout_10.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout_10.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_6 = QtGui.QLabel(self.tab_4)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_7.addWidget(self.label_6)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.label_7 = QtGui.QLabel(self.tab_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_14.addWidget(self.label_7)
        self.time_cutoff = QtGui.QSpinBox(self.tab_4)
        self.time_cutoff.setProperty("value", 20)
        self.time_cutoff.setObjectName(_fromUtf8("time_cutoff"))
        self.horizontalLayout_14.addWidget(self.time_cutoff)
        self.label_8 = QtGui.QLabel(self.tab_4)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_14.addWidget(self.label_8)
        self.label_4 = QtGui.QLabel(self.tab_4)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_14.addWidget(self.label_4)
        self.DFS_cutoff = QtGui.QDoubleSpinBox(self.tab_4)
        self.DFS_cutoff.setProperty("value", 0.5)
        self.DFS_cutoff.setObjectName(_fromUtf8("DFS_cutoff"))
        self.horizontalLayout_14.addWidget(self.DFS_cutoff)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_14)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.clear_button = QtGui.QPushButton(self.tab_4)
        self.clear_button.setObjectName(_fromUtf8("clear_button"))
        self.horizontalLayout_7.addWidget(self.clear_button)
        self.verticalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.label_9 = QtGui.QLabel(self.tab_4)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_13.addWidget(self.label_9)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.output_legs = QtGui.QTextEdit(self.tab_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.output_legs.setFont(font)
        self.output_legs.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.output_legs.setLineWrapColumnOrWidth(0)
        self.output_legs.setReadOnly(True)
        self.output_legs.setObjectName(_fromUtf8("output_legs"))
        self.verticalLayout.addWidget(self.output_legs)
        self.label_23 = QtGui.QLabel(self.tab_4)
        self.label_23.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.verticalLayout.addWidget(self.label_23)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_10.addLayout(self.horizontalLayout_6)
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_11 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_11.setObjectName(_fromUtf8("verticalLayout_11"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_22 = QtGui.QHBoxLayout()
        self.horizontalLayout_22.setObjectName(_fromUtf8("horizontalLayout_22"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_6.sizePolicy().hasHeightForWidth())
        self.radioButton_6.setSizePolicy(sizePolicy)
        self.radioButton_6.setMinimumSize(QtCore.QSize(75, 0))
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.horizontalLayout_22.addWidget(self.radioButton_6)
        self.label_24 = QtGui.QLabel(self.groupBox)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.horizontalLayout_22.addWidget(self.label_24)
        self.verticalLayout_5.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        self.radioButton_7 = QtGui.QRadioButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_7.sizePolicy().hasHeightForWidth())
        self.radioButton_7.setSizePolicy(sizePolicy)
        self.radioButton_7.setMinimumSize(QtCore.QSize(75, 0))
        self.radioButton_7.setObjectName(_fromUtf8("radioButton_7"))
        self.horizontalLayout_21.addWidget(self.radioButton_7)
        self.label_16 = QtGui.QLabel(self.groupBox)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_21.addWidget(self.label_16)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.horizontalLayout_16.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_15.addWidget(self.label_14)
        self.spinBox_totalPower = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_totalPower.setMaximum(3000)
        self.spinBox_totalPower.setProperty("value", 784)
        self.spinBox_totalPower.setObjectName(_fromUtf8("spinBox_totalPower"))
        self.horizontalLayout_15.addWidget(self.spinBox_totalPower)
        self.verticalLayout_6.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.label_22 = QtGui.QLabel(self.groupBox_3)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.horizontalLayout_17.addWidget(self.label_22)
        self.spinBox_reservePower = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_reservePower.setMaximum(200)
        self.spinBox_reservePower.setProperty("value", 100)
        self.spinBox_reservePower.setObjectName(_fromUtf8("spinBox_reservePower"))
        self.horizontalLayout_17.addWidget(self.spinBox_reservePower)
        self.verticalLayout_6.addLayout(self.horizontalLayout_17)
        self.verticalLayout_8.addWidget(self.groupBox_3)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_16)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.verticalLayout_13 = QtGui.QVBoxLayout()
        self.verticalLayout_13.setObjectName(_fromUtf8("verticalLayout_13"))
        self.label_19 = QtGui.QLabel(self.tab)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.verticalLayout_13.addWidget(self.label_19)
        self.power_table = QtGui.QTextBrowser(self.tab)
        self.power_table.setObjectName(_fromUtf8("power_table"))
        self.verticalLayout_13.addWidget(self.power_table)
        self.horizontalLayout_19.addLayout(self.verticalLayout_13)
        self.verticalLayout_14 = QtGui.QVBoxLayout()
        self.verticalLayout_14.setObjectName(_fromUtf8("verticalLayout_14"))
        self.label_11 = QtGui.QLabel(self.tab)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.verticalLayout_14.addWidget(self.label_11)
        self.speed_table = QtGui.QTextBrowser(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_table.sizePolicy().hasHeightForWidth())
        self.speed_table.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.speed_table.setFont(font)
        self.speed_table.setObjectName(_fromUtf8("speed_table"))
        self.verticalLayout_14.addWidget(self.speed_table)
        self.horizontalLayout_19.addLayout(self.verticalLayout_14)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.clear_button_2 = QtGui.QPushButton(self.tab)
        self.clear_button_2.setObjectName(_fromUtf8("clear_button_2"))
        self.horizontalLayout_5.addWidget(self.clear_button_2)
        self.generate_button = QtGui.QPushButton(self.tab)
        self.generate_button.setObjectName(_fromUtf8("generate_button"))
        self.horizontalLayout_5.addWidget(self.generate_button)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_15 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_15.setObjectName(_fromUtf8("verticalLayout_15"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_9.addWidget(self.label_12)
        self.r_label = QtGui.QLabel(self.groupBox_4)
        self.r_label.setObjectName(_fromUtf8("r_label"))
        self.horizontalLayout_9.addWidget(self.r_label)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)
        self.verticalLayout_15.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_10.addWidget(self.label_13)
        self.coe_label = QtGui.QLabel(self.groupBox_4)
        self.coe_label.setObjectName(_fromUtf8("coe_label"))
        self.horizontalLayout_10.addWidget(self.coe_label)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_10.addWidget(self.label_5)
        self.int_label = QtGui.QLabel(self.groupBox_4)
        self.int_label.setObjectName(_fromUtf8("int_label"))
        self.horizontalLayout_10.addWidget(self.int_label)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem7)
        self.verticalLayout_15.addLayout(self.horizontalLayout_10)
        self.verticalLayout_12.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_16.setObjectName(_fromUtf8("verticalLayout_16"))
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName(_fromUtf8("horizontalLayout_12"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.horizontalLayout_12.addWidget(self.label_17)
        self.power_eq_label = QtGui.QLabel(self.groupBox_5)
        self.power_eq_label.setObjectName(_fromUtf8("power_eq_label"))
        self.horizontalLayout_12.addWidget(self.power_eq_label)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem8)
        self.verticalLayout_16.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.report_button = QtGui.QPushButton(self.groupBox_5)
        self.report_button.setObjectName(_fromUtf8("report_button"))
        self.horizontalLayout_18.addWidget(self.report_button)
        self.label_15 = QtGui.QLabel(self.groupBox_5)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_18.addWidget(self.label_15)
        self.Iver_lineEdit = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Iver_lineEdit.sizePolicy().hasHeightForWidth())
        self.Iver_lineEdit.setSizePolicy(sizePolicy)
        self.Iver_lineEdit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.Iver_lineEdit.setObjectName(_fromUtf8("Iver_lineEdit"))
        self.horizontalLayout_18.addWidget(self.Iver_lineEdit)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.verticalLayout_16.addLayout(self.horizontalLayout_18)
        self.verticalLayout_12.addWidget(self.groupBox_5)
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.browseDatabase_button = QtGui.QPushButton(self.groupBox_6)
        self.browseDatabase_button.setObjectName(_fromUtf8("browseDatabase_button"))
        self.horizontalLayout_2.addWidget(self.browseDatabase_button)
        self.databaseFilename_display = QtGui.QLineEdit(self.groupBox_6)
        self.databaseFilename_display.setObjectName(_fromUtf8("databaseFilename_display"))
        self.horizontalLayout_2.addWidget(self.databaseFilename_display)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.sortDatabase_button = QtGui.QPushButton(self.groupBox_6)
        self.sortDatabase_button.setObjectName(_fromUtf8("sortDatabase_button"))
        self.horizontalLayout_11.addWidget(self.sortDatabase_button)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.label_10 = QtGui.QLabel(self.groupBox_6)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_20.addWidget(self.label_10)
        self.iverNumber = QtGui.QLineEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iverNumber.sizePolicy().hasHeightForWidth())
        self.iverNumber.setSizePolicy(sizePolicy)
        self.iverNumber.setMinimumSize(QtCore.QSize(100, 0))
        self.iverNumber.setMaximumSize(QtCore.QSize(100, 16777215))
        self.iverNumber.setObjectName(_fromUtf8("iverNumber"))
        self.horizontalLayout_20.addWidget(self.iverNumber)
        self.appendDatabase_button = QtGui.QPushButton(self.groupBox_6)
        self.appendDatabase_button.setObjectName(_fromUtf8("appendDatabase_button"))
        self.horizontalLayout_20.addWidget(self.appendDatabase_button)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_20)
        self.databaseBrowser = QtGui.QTextBrowser(self.groupBox_6)
        self.databaseBrowser.setObjectName(_fromUtf8("databaseBrowser"))
        self.verticalLayout_3.addWidget(self.databaseBrowser)
        self.verticalLayout_12.addWidget(self.groupBox_6)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem13)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.verticalLayout_2.addWidget(self.label_21)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Python Motor Command Analyzer", None))
        self.label.setText(_translate("MainWindow", "OceanServer Motor Command and Power Analyzer", None))
        self.how_to_label.setText(_translate("MainWindow", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "How To", None))
        self.label_2.setText(_translate("MainWindow", "Log File:", None))
        self.browse_button.setText(_translate("MainWindow", "Browse", None))
        self.label_3.setText(_translate("MainWindow", "Mission Leg Filter", None))
        self.label_6.setText(_translate("MainWindow", "Remove Mission Leg if:", None))
        self.label_7.setText(_translate("MainWindow", "Leg Time (sec) <", None))
        self.label_8.setText(_translate("MainWindow", "OR", None))
        self.label_4.setText(_translate("MainWindow", "Depth From Surface (m)  <", None))
        self.clear_button.setText(_translate("MainWindow", "Clear Fields", None))
        self.label_9.setText(_translate("MainWindow", "Resulting Mission Legs", None))
        self.label_23.setText(_translate("MainWindow", "Step  \"-1\"  represents hotel load. (Average power draw while Iver is parked AND motor rpm is 0)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Load Log File", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Table Parameters:", None))
        self.groupBox.setTitle(_translate("MainWindow", "Motor Prefix:", None))
        self.radioButton_6.setText(_translate("MainWindow", "6 - Analog", None))
        self.label_24.setText(_translate("MainWindow", "TextLabel", None))
        self.radioButton_7.setText(_translate("MainWindow", "7 - Smart", None))
        self.label_16.setText(_translate("MainWindow", "TextLabel", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Battery Specs:", None))
        self.label_14.setText(_translate("MainWindow", "Total Power (Wh)", None))
        self.label_22.setText(_translate("MainWindow", "Reserve Power(Wh)", None))
        self.label_19.setText(_translate("MainWindow", "Power Table", None))
        self.label_11.setText(_translate("MainWindow", "Speed Table", None))
        self.clear_button_2.setText(_translate("MainWindow", "Clear Fields", None))
        self.generate_button.setText(_translate("MainWindow", "Generate", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Power AND Speed Table", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Motor CMD Regression Analysis", None))
        self.label_12.setText(_translate("MainWindow", "Coefficient of Determination [R Squared]:", None))
        self.r_label.setText(_translate("MainWindow", "RSquared Value", None))
        self.label_13.setText(_translate("MainWindow", "Motor CMD = Speed (kn)  *", None))
        self.coe_label.setText(_translate("MainWindow", "coefficient", None))
        self.label_5.setText(_translate("MainWindow", "+", None))
        self.int_label.setText(_translate("MainWindow", "intercept", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Power Regression Analysis", None))
        self.label_17.setText(_translate("MainWindow", "Power (watts) = ", None))
        self.power_eq_label.setText(_translate("MainWindow", "Cubic Function", None))
        self.report_button.setText(_translate("MainWindow", "Create Report", None))
        self.label_15.setText(_translate("MainWindow", "Iver Number:", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Append Database", None))
        self.browseDatabase_button.setText(_translate("MainWindow", "Browse", None))
        self.sortDatabase_button.setText(_translate("MainWindow", "Sort", None))
        self.label_10.setText(_translate("MainWindow", "Iver Number", None))
        self.appendDatabase_button.setText(_translate("MainWindow", "Append", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Quick Report", None))
        self.label_20.setText(_translate("MainWindow", "Created by Nicholas Goumas at OceanServer Technology Inc.", None))
        self.label_21.setText(_translate("MainWindow", "Goumas@ocean-server.com", None))

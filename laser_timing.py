# Form implementation generated from reading ui file '.\laser_timing.ui'
#
# Created by: PyQt6 UI code generator 6.8.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1023, 349)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 981, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.v1_timing_qs = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.v1_timing_qs.setDecimals(3)
        self.v1_timing_qs.setMaximum(100000.0)
        self.v1_timing_qs.setObjectName("v1_timing_qs")
        self.gridLayout.addWidget(self.v1_timing_qs, 1, 4, 1, 1)
        self.v2_timing_diode = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.v2_timing_diode.setDecimals(3)
        self.v2_timing_diode.setMaximum(100000.0)
        self.v2_timing_diode.setObjectName("v2_timing_diode")
        self.gridLayout.addWidget(self.v2_timing_diode, 2, 2, 1, 1)
        self.v1_power = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v1_power.sizePolicy().hasHeightForWidth())
        self.v1_power.setSizePolicy(sizePolicy)
        self.v1_power.setMaximum(100)
        self.v1_power.setSliderPosition(100)
        self.v1_power.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.v1_power.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.v1_power.setTickInterval(10)
        self.v1_power.setObjectName("v1_power")
        self.gridLayout.addWidget(self.v1_power, 1, 10, 1, 1)
        self.c2_trig_qs = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c2_trig_qs.setCheckable(True)
        self.c2_trig_qs.setChecked(False)
        self.c2_trig_qs.setObjectName("c2_trig_qs")
        self.gridLayout.addWidget(self.c2_trig_qs, 6, 3, 1, 1)
        self.v1_enabled = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v1_enabled.setCheckable(True)
        self.v1_enabled.setChecked(False)
        self.v1_enabled.setObjectName("v1_enabled")
        self.gridLayout.addWidget(self.v1_enabled, 1, 6, 1, 1)
        self.c5_power = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c5_power.sizePolicy().hasHeightForWidth())
        self.c5_power.setSizePolicy(sizePolicy)
        self.c5_power.setMaximum(100)
        self.c5_power.setSliderPosition(100)
        self.c5_power.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.c5_power.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.c5_power.setTickInterval(10)
        self.c5_power.setObjectName("c5_power")
        self.gridLayout.addWidget(self.c5_power, 9, 10, 1, 1)
        self.c2_power = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c2_power.sizePolicy().hasHeightForWidth())
        self.c2_power.setSizePolicy(sizePolicy)
        self.c2_power.setMaximum(100)
        self.c2_power.setSliderPosition(100)
        self.c2_power.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.c2_power.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.c2_power.setTickInterval(10)
        self.c2_power.setObjectName("c2_power")
        self.gridLayout.addWidget(self.c2_power, 6, 10, 1, 1)
        self.c4_timing_diode = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c4_timing_diode.setDecimals(3)
        self.c4_timing_diode.setMaximum(100000.0)
        self.c4_timing_diode.setObjectName("c4_timing_diode")
        self.gridLayout.addWidget(self.c4_timing_diode, 8, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.c4_com = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.c4_com.setObjectName("c4_com")
        self.c4_com.addItem("")
        self.gridLayout.addWidget(self.c4_com, 8, 7, 1, 1)
        self.c2_init = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c2_init.setCheckable(True)
        self.c2_init.setChecked(False)
        self.c2_init.setObjectName("c2_init")
        self.gridLayout.addWidget(self.c2_init, 6, 9, 1, 1)
        self.c2_trig_diode = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c2_trig_diode.setCheckable(True)
        self.c2_trig_diode.setChecked(False)
        self.c2_trig_diode.setObjectName("c2_trig_diode")
        self.gridLayout.addWidget(self.c2_trig_diode, 6, 1, 1, 1)
        self.c1_enabled = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c1_enabled.setCheckable(True)
        self.c1_enabled.setChecked(False)
        self.c1_enabled.setObjectName("c1_enabled")
        self.gridLayout.addWidget(self.c1_enabled, 4, 6, 1, 1)
        self.c3_enabled = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c3_enabled.setCheckable(True)
        self.c3_enabled.setChecked(False)
        self.c3_enabled.setObjectName("c3_enabled")
        self.gridLayout.addWidget(self.c3_enabled, 7, 6, 1, 1)
        self.v2_trig_diode = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v2_trig_diode.setCheckable(True)
        self.v2_trig_diode.setChecked(False)
        self.v2_trig_diode.setObjectName("v2_trig_diode")
        self.gridLayout.addWidget(self.v2_trig_diode, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 7, 0, 1, 1)
        self.c2_enabled = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c2_enabled.setCheckable(True)
        self.c2_enabled.setChecked(False)
        self.c2_enabled.setObjectName("c2_enabled")
        self.gridLayout.addWidget(self.c2_enabled, 6, 6, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.v2_timing_qs = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.v2_timing_qs.setDecimals(3)
        self.v2_timing_qs.setMaximum(100000.0)
        self.v2_timing_qs.setObjectName("v2_timing_qs")
        self.gridLayout.addWidget(self.v2_timing_qs, 2, 4, 1, 1)
        self.c5_trig_diode = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c5_trig_diode.setCheckable(True)
        self.c5_trig_diode.setChecked(False)
        self.c5_trig_diode.setObjectName("c5_trig_diode")
        self.gridLayout.addWidget(self.c5_trig_diode, 9, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 7, 1, 1)
        self.c5_timing_diode = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c5_timing_diode.setDecimals(3)
        self.c5_timing_diode.setMaximum(100000.0)
        self.c5_timing_diode.setObjectName("c5_timing_diode")
        self.gridLayout.addWidget(self.c5_timing_diode, 9, 2, 1, 1)
        self.c1_init = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c1_init.setCheckable(True)
        self.c1_init.setChecked(False)
        self.c1_init.setObjectName("c1_init")
        self.gridLayout.addWidget(self.c1_init, 4, 9, 1, 1)
        self.c1_power = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c1_power.sizePolicy().hasHeightForWidth())
        self.c1_power.setSizePolicy(sizePolicy)
        self.c1_power.setMaximum(100)
        self.c1_power.setSliderPosition(100)
        self.c1_power.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.c1_power.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.c1_power.setTickInterval(10)
        self.c1_power.setObjectName("c1_power")
        self.gridLayout.addWidget(self.c1_power, 4, 10, 1, 1)
        self.c4_trig_qs = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c4_trig_qs.setCheckable(True)
        self.c4_trig_qs.setChecked(False)
        self.c4_trig_qs.setObjectName("c4_trig_qs")
        self.gridLayout.addWidget(self.c4_trig_qs, 8, 3, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 9, 1, 1)
        self.c1_trig_diode = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c1_trig_diode.setCheckable(True)
        self.c1_trig_diode.setChecked(False)
        self.c1_trig_diode.setObjectName("c1_trig_diode")
        self.gridLayout.addWidget(self.c1_trig_diode, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 6, 1, 1)
        self.c1_timing_diode = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c1_timing_diode.setDecimals(3)
        self.c1_timing_diode.setMaximum(100000.0)
        self.c1_timing_diode.setObjectName("c1_timing_diode")
        self.gridLayout.addWidget(self.c1_timing_diode, 4, 2, 1, 1)
        self.c5_init = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c5_init.setStyleSheet("")
        self.c5_init.setCheckable(True)
        self.c5_init.setChecked(False)
        self.c5_init.setObjectName("c5_init")
        self.gridLayout.addWidget(self.c5_init, 9, 9, 1, 1)
        self.v2_enabled = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v2_enabled.setCheckable(True)
        self.v2_enabled.setChecked(False)
        self.v2_enabled.setObjectName("v2_enabled")
        self.gridLayout.addWidget(self.v2_enabled, 2, 6, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 3, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 9, 0, 1, 1)
        self.v1_trig_diode = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v1_trig_diode.setCheckable(True)
        self.v1_trig_diode.setChecked(False)
        self.v1_trig_diode.setObjectName("v1_trig_diode")
        self.gridLayout.addWidget(self.v1_trig_diode, 1, 1, 1, 1)
        self.v1_timing_diode = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.v1_timing_diode.setDecimals(3)
        self.v1_timing_diode.setMaximum(100000.0)
        self.v1_timing_diode.setObjectName("v1_timing_diode")
        self.gridLayout.addWidget(self.v1_timing_diode, 1, 2, 1, 1)
        self.c5_enabled = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c5_enabled.setCheckable(True)
        self.c5_enabled.setChecked(False)
        self.c5_enabled.setObjectName("c5_enabled")
        self.gridLayout.addWidget(self.c5_enabled, 9, 6, 1, 1)
        self.c4_enabled = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c4_enabled.setCheckable(True)
        self.c4_enabled.setChecked(False)
        self.c4_enabled.setObjectName("c4_enabled")
        self.gridLayout.addWidget(self.c4_enabled, 8, 6, 1, 1)
        self.c4_timing_qs = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c4_timing_qs.setDecimals(3)
        self.c4_timing_qs.setMaximum(100000.0)
        self.c4_timing_qs.setObjectName("c4_timing_qs")
        self.gridLayout.addWidget(self.c4_timing_qs, 8, 4, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 10, 1, 1)
        self.v1_trig_qs = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v1_trig_qs.setCheckable(True)
        self.v1_trig_qs.setChecked(False)
        self.v1_trig_qs.setObjectName("v1_trig_qs")
        self.gridLayout.addWidget(self.v1_trig_qs, 1, 3, 1, 1)
        self.c4_power = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c4_power.sizePolicy().hasHeightForWidth())
        self.c4_power.setSizePolicy(sizePolicy)
        self.c4_power.setMaximum(100)
        self.c4_power.setSliderPosition(100)
        self.c4_power.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.c4_power.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.c4_power.setTickInterval(10)
        self.c4_power.setObjectName("c4_power")
        self.gridLayout.addWidget(self.c4_power, 8, 10, 1, 1)
        self.c2_timing_diode = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c2_timing_diode.setDecimals(3)
        self.c2_timing_diode.setMaximum(100000.0)
        self.c2_timing_diode.setObjectName("c2_timing_diode")
        self.gridLayout.addWidget(self.c2_timing_diode, 6, 2, 1, 1)
        self.c3_init = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c3_init.setCheckable(True)
        self.c3_init.setChecked(False)
        self.c3_init.setObjectName("c3_init")
        self.gridLayout.addWidget(self.c3_init, 7, 9, 1, 1)
        self.v1_ip = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.v1_ip.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v1_ip.sizePolicy().hasHeightForWidth())
        self.v1_ip.setSizePolicy(sizePolicy)
        self.v1_ip.setMinimumSize(QtCore.QSize(0, 0))
        self.v1_ip.setMaximumSize(QtCore.QSize(130, 20))
        self.v1_ip.setBaseSize(QtCore.QSize(0, 0))
        self.v1_ip.setObjectName("v1_ip")
        self.gridLayout.addWidget(self.v1_ip, 1, 7, 1, 1)
        self.c1_trig_qs = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c1_trig_qs.setCheckable(True)
        self.c1_trig_qs.setChecked(False)
        self.c1_trig_qs.setObjectName("c1_trig_qs")
        self.gridLayout.addWidget(self.c1_trig_qs, 4, 3, 1, 1)
        self.c3_com = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.c3_com.setObjectName("c3_com")
        self.c3_com.addItem("")
        self.gridLayout.addWidget(self.c3_com, 7, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)
        self.c1_timing_qs = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c1_timing_qs.setDecimals(3)
        self.c1_timing_qs.setMaximum(100000.0)
        self.c1_timing_qs.setObjectName("c1_timing_qs")
        self.gridLayout.addWidget(self.c1_timing_qs, 4, 4, 1, 1)
        self.c5_timing_qs = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c5_timing_qs.setDecimals(3)
        self.c5_timing_qs.setMaximum(100000.0)
        self.c5_timing_qs.setObjectName("c5_timing_qs")
        self.gridLayout.addWidget(self.c5_timing_qs, 9, 4, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.c4_init = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c4_init.setCheckable(True)
        self.c4_init.setChecked(False)
        self.c4_init.setObjectName("c4_init")
        self.gridLayout.addWidget(self.c4_init, 8, 9, 1, 1)
        self.c3_timing_diode = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c3_timing_diode.setDecimals(3)
        self.c3_timing_diode.setMaximum(100000.0)
        self.c3_timing_diode.setObjectName("c3_timing_diode")
        self.gridLayout.addWidget(self.c3_timing_diode, 7, 2, 1, 1)
        self.c3_trig_qs = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c3_trig_qs.setCheckable(True)
        self.c3_trig_qs.setChecked(False)
        self.c3_trig_qs.setObjectName("c3_trig_qs")
        self.gridLayout.addWidget(self.c3_trig_qs, 7, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 0, 1, 1)
        self.c4_trig_diode = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c4_trig_diode.setCheckable(True)
        self.c4_trig_diode.setChecked(False)
        self.c4_trig_diode.setObjectName("c4_trig_diode")
        self.gridLayout.addWidget(self.c4_trig_diode, 8, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
        self.c3_timing_qs = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c3_timing_qs.setDecimals(3)
        self.c3_timing_qs.setMaximum(100000.0)
        self.c3_timing_qs.setObjectName("c3_timing_qs")
        self.gridLayout.addWidget(self.c3_timing_qs, 7, 4, 1, 1)
        self.c1_com = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.c1_com.setObjectName("c1_com")
        self.c1_com.addItem("")
        self.gridLayout.addWidget(self.c1_com, 4, 7, 1, 1)
        self.label_15 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 8, 0, 1, 1)
        self.c5_com = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.c5_com.setObjectName("c5_com")
        self.c5_com.addItem("")
        self.gridLayout.addWidget(self.c5_com, 9, 7, 1, 1)
        self.c3_trig_diode = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c3_trig_diode.setCheckable(True)
        self.c3_trig_diode.setChecked(False)
        self.c3_trig_diode.setObjectName("c3_trig_diode")
        self.gridLayout.addWidget(self.c3_trig_diode, 7, 1, 1, 1)
        self.v2_power = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v2_power.sizePolicy().hasHeightForWidth())
        self.v2_power.setSizePolicy(sizePolicy)
        self.v2_power.setMaximum(100)
        self.v2_power.setSliderPosition(100)
        self.v2_power.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.v2_power.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.v2_power.setTickInterval(10)
        self.v2_power.setObjectName("v2_power")
        self.gridLayout.addWidget(self.v2_power, 2, 10, 1, 1)
        self.v1_init = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v1_init.setCheckable(True)
        self.v1_init.setChecked(False)
        self.v1_init.setObjectName("v1_init")
        self.gridLayout.addWidget(self.v1_init, 1, 9, 1, 1)
        self.c2_timing_qs = QtWidgets.QDoubleSpinBox(parent=self.gridLayoutWidget)
        self.c2_timing_qs.setDecimals(3)
        self.c2_timing_qs.setMaximum(100000.0)
        self.c2_timing_qs.setObjectName("c2_timing_qs")
        self.gridLayout.addWidget(self.c2_timing_qs, 6, 4, 1, 1)
        self.v2_init = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v2_init.setCheckable(True)
        self.v2_init.setChecked(False)
        self.v2_init.setObjectName("v2_init")
        self.gridLayout.addWidget(self.v2_init, 2, 9, 1, 1)
        self.c5_trig_qs = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.c5_trig_qs.setCheckable(True)
        self.c5_trig_qs.setChecked(False)
        self.c5_trig_qs.setObjectName("c5_trig_qs")
        self.gridLayout.addWidget(self.c5_trig_qs, 9, 3, 1, 1)
        self.v2_trig_qs = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.v2_trig_qs.setCheckable(True)
        self.v2_trig_qs.setChecked(False)
        self.v2_trig_qs.setObjectName("v2_trig_qs")
        self.gridLayout.addWidget(self.v2_trig_qs, 2, 3, 1, 1)
        self.c3_power = QtWidgets.QSlider(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c3_power.sizePolicy().hasHeightForWidth())
        self.c3_power.setSizePolicy(sizePolicy)
        self.c3_power.setMaximum(100)
        self.c3_power.setSliderPosition(100)
        self.c3_power.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.c3_power.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.c3_power.setTickInterval(10)
        self.c3_power.setObjectName("c3_power")
        self.gridLayout.addWidget(self.c3_power, 7, 10, 1, 1)
        self.c2_com = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.c2_com.setObjectName("c2_com")
        self.c2_com.addItem("")
        self.gridLayout.addWidget(self.c2_com, 6, 7, 1, 1)
        self.v1_mac = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.v1_mac.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v1_mac.sizePolicy().hasHeightForWidth())
        self.v1_mac.setSizePolicy(sizePolicy)
        self.v1_mac.setMaximumSize(QtCore.QSize(120, 20))
        self.v1_mac.setObjectName("v1_mac")
        self.gridLayout.addWidget(self.v1_mac, 1, 8, 1, 1)
        self.v2_mac = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.v2_mac.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v2_mac.sizePolicy().hasHeightForWidth())
        self.v2_mac.setSizePolicy(sizePolicy)
        self.v2_mac.setMaximumSize(QtCore.QSize(120, 20))
        self.v2_mac.setObjectName("v2_mac")
        self.gridLayout.addWidget(self.v2_mac, 2, 8, 1, 1)
        self.v2_ip = QtWidgets.QTextEdit(parent=self.gridLayoutWidget)
        self.v2_ip.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.v2_ip.sizePolicy().hasHeightForWidth())
        self.v2_ip.setSizePolicy(sizePolicy)
        self.v2_ip.setMinimumSize(QtCore.QSize(0, 0))
        self.v2_ip.setMaximumSize(QtCore.QSize(130, 20))
        self.v2_ip.setBaseSize(QtCore.QSize(0, 0))
        self.v2_ip.setObjectName("v2_ip")
        self.gridLayout.addWidget(self.v2_ip, 2, 7, 1, 1)
        self.label_19 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 8, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.doubleSpinBox.setGeometry(QtCore.QRect(130, 10, 91, 21))
        self.doubleSpinBox.setDecimals(3)
        self.doubleSpinBox.setMaximum(100000.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.send_times = QtWidgets.QPushButton(parent=self.centralwidget)
        self.send_times.setGeometry(QtCore.QRect(240, 10, 75, 24))
        self.send_times.setCheckable(False)
        self.send_times.setChecked(False)
        self.send_times.setObjectName("send_times")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Laser control"))
        self.c2_trig_qs.setText(_translate("MainWindow", "External"))
        self.v1_enabled.setText(_translate("MainWindow", "Enable"))
        self.label_2.setText(_translate("MainWindow", "Laser"))
        self.c4_com.setItemText(0, _translate("MainWindow", "None"))
        self.c2_init.setText(_translate("MainWindow", "Initialize"))
        self.c2_trig_diode.setText(_translate("MainWindow", "External"))
        self.c1_enabled.setText(_translate("MainWindow", "Enable"))
        self.c3_enabled.setText(_translate("MainWindow", "Enable"))
        self.v2_trig_diode.setText(_translate("MainWindow", "External"))
        self.label_14.setText(_translate("MainWindow", "CNI 3"))
        self.c2_enabled.setText(_translate("MainWindow", "Enable"))
        self.label_10.setText(_translate("MainWindow", "Viron 2"))
        self.c5_trig_diode.setText(_translate("MainWindow", "External"))
        self.label_8.setText(_translate("MainWindow", "Connection"))
        self.c1_init.setText(_translate("MainWindow", "Initialize"))
        self.c4_trig_qs.setText(_translate("MainWindow", "External"))
        self.label_17.setText(_translate("MainWindow", "Initialize"))
        self.c1_trig_diode.setText(_translate("MainWindow", "External"))
        self.label_7.setText(_translate("MainWindow", "Enabled"))
        self.c5_init.setText(_translate("MainWindow", "Initialize"))
        self.v2_enabled.setText(_translate("MainWindow", "Enable"))
        self.label_6.setText(_translate("MainWindow", "QS trigger"))
        self.label_16.setText(_translate("MainWindow", "CNI 5"))
        self.v1_trig_diode.setText(_translate("MainWindow", "External"))
        self.c5_enabled.setText(_translate("MainWindow", "Enable"))
        self.c4_enabled.setText(_translate("MainWindow", "Enable"))
        self.label_18.setText(_translate("MainWindow", "Power (%)"))
        self.v1_trig_qs.setText(_translate("MainWindow", "External"))
        self.c3_init.setText(_translate("MainWindow", "Initialize"))
        self.v1_ip.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">192.168.103.105:25</p></body></html>"))
        self.c1_trig_qs.setText(_translate("MainWindow", "External"))
        self.c3_com.setItemText(0, _translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "Diode timing (ns)"))
        self.label_3.setText(_translate("MainWindow", "Diode trigger"))
        self.label_12.setText(_translate("MainWindow", "CNI 1"))
        self.c4_init.setText(_translate("MainWindow", "Initialize"))
        self.c3_trig_qs.setText(_translate("MainWindow", "External"))
        self.label_13.setText(_translate("MainWindow", "CNI 2"))
        self.c4_trig_diode.setText(_translate("MainWindow", "External"))
        self.label_9.setText(_translate("MainWindow", "Viron 1"))
        self.label_5.setText(_translate("MainWindow", "QS timing (ns)"))
        self.c1_com.setItemText(0, _translate("MainWindow", "None"))
        self.label_15.setText(_translate("MainWindow", "CNI 4"))
        self.c5_com.setItemText(0, _translate("MainWindow", "None"))
        self.c3_trig_diode.setText(_translate("MainWindow", "External"))
        self.v1_init.setText(_translate("MainWindow", "Initialize"))
        self.v2_init.setText(_translate("MainWindow", "Initialize"))
        self.c5_trig_qs.setText(_translate("MainWindow", "External"))
        self.v2_trig_qs.setText(_translate("MainWindow", "External"))
        self.c2_com.setItemText(0, _translate("MainWindow", "None"))
        self.v1_mac.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00:80:A3:6B:E4:1D</p></body></html>"))
        self.v2_mac.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">00:80:A3:6B:E4:1E</p></body></html>"))
        self.v2_ip.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">192.168.103.107:27</p></body></html>"))
        self.label_19.setText(_translate("MainWindow", "MAC"))
        self.label.setText(_translate("MainWindow", "Overall timing (ns)"))
        self.send_times.setText(_translate("MainWindow", "Set times"))

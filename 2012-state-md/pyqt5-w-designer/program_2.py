# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Kisun\Desktop\skillsusa-practice\2012-state-md\pyqt5-w-designer\program_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1204, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.customer_name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.customer_name_edit.setObjectName("customer_name_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.customer_name_edit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pizzas_ordering_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.pizzas_ordering_combobox.setObjectName("pizzas_ordering_combobox")
        self.pizzas_ordering_combobox.addItem("")
        self.pizzas_ordering_combobox.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pizzas_ordering_combobox)
        self.horizontalLayout_4.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.screen_1_box = QtWidgets.QGroupBox(self.centralwidget)
        self.screen_1_box.setStyleSheet("QGroupBox {border: none}")
        self.screen_1_box.setTitle("")
        self.screen_1_box.setObjectName("screen_1_box")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.screen_1_box)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pizza_one_groupbox_1 = QtWidgets.QGroupBox(self.screen_1_box)
        self.pizza_one_groupbox_1.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pizza_one_groupbox_1.sizePolicy().hasHeightForWidth())
        self.pizza_one_groupbox_1.setSizePolicy(sizePolicy)
        self.pizza_one_groupbox_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pizza_one_groupbox_1.setObjectName("pizza_one_groupbox_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.pizza_one_groupbox_1)
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.pizza_one_groupbox_1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -51, 531, 348))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.formLayout_2 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_9)
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.size_large_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.size_large_radio.setText("")
        self.size_large_radio.setObjectName("size_large_radio")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.size_large_radio)
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.size_medium_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.size_medium_radio.setText("")
        self.size_medium_radio.setObjectName("size_medium_radio")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.size_medium_radio)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.size_small_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.size_small_radio.setText("")
        self.size_small_radio.setObjectName("size_small_radio")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.size_small_radio)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_8.setMinimumSize(QtCore.QSize(25, 0))
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_8)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_37)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label_38)
        self.label_30 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_30.setObjectName("label_30")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.toppings_spinbox = QtWidgets.QSpinBox(self.scrollAreaWidgetContents)
        self.toppings_spinbox.setObjectName("toppings_spinbox")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.toppings_spinbox)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_9.setMinimumSize(QtCore.QSize(25, 0))
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.formLayout_2.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_9)
        self.label_31 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.formLayout_2.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.label_31)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.shape_round_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.shape_round_radio.setText("")
        self.shape_round_radio.setObjectName("shape_round_radio")
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.shape_round_radio)
        self.label_16 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.shape_square_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.shape_square_radio.setText("")
        self.shape_square_radio.setObjectName("shape_square_radio")
        self.formLayout_2.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.shape_square_radio)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_10.setMinimumSize(QtCore.QSize(25, 0))
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.formLayout_2.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.line_10)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.formLayout_2.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.label_39)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.label_15 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.shape_thick_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.shape_thick_radio.setText("")
        self.shape_thick_radio.setObjectName("shape_thick_radio")
        self.formLayout_2.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.shape_thick_radio)
        self.shape_thin_radio = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.shape_thin_radio.setText("")
        self.shape_thin_radio.setObjectName("shape_thin_radio")
        self.formLayout_2.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.shape_thin_radio)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.horizontalLayout_5.addWidget(self.pizza_one_groupbox_1)
        self.pizza_two_groupbox_1 = QtWidgets.QGroupBox(self.screen_1_box)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pizza_two_groupbox_1.sizePolicy().hasHeightForWidth())
        self.pizza_two_groupbox_1.setSizePolicy(sizePolicy)
        self.pizza_two_groupbox_1.setAlignment(QtCore.Qt.AlignCenter)
        self.pizza_two_groupbox_1.setObjectName("pizza_two_groupbox_1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.pizza_two_groupbox_1)
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.pizza_two_groupbox_1)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 530, 348))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_17)
        self.label_18 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.size_large_radio_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.size_large_radio_2.setText("")
        self.size_large_radio_2.setObjectName("size_large_radio_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.size_large_radio_2)
        self.label_19 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.size_medium_radio_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.size_medium_radio_2.setText("")
        self.size_medium_radio_2.setObjectName("size_medium_radio_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.size_medium_radio_2)
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.size_small_radio_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.size_small_radio_2.setText("")
        self.size_small_radio_2.setObjectName("size_small_radio_2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.size_small_radio_2)
        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_11.setMinimumSize(QtCore.QSize(25, 0))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.line_11)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_40)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.formLayout_3.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.label_41)
        self.label_32 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_32.setObjectName("label_32")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.toppings_spinbox_2 = QtWidgets.QSpinBox(self.scrollAreaWidgetContents_2)
        self.toppings_spinbox_2.setObjectName("toppings_spinbox_2")
        self.formLayout_3.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.toppings_spinbox_2)
        self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_12.setMinimumSize(QtCore.QSize(25, 0))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.formLayout_3.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.line_12)
        self.label_33 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.formLayout_3.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.label_33)
        self.label_21 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_21.setObjectName("label_21")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.shape_round_radio_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.shape_round_radio_2.setText("")
        self.shape_round_radio_2.setObjectName("shape_round_radio_2")
        self.formLayout_3.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.shape_round_radio_2)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_22.setObjectName("label_22")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.shape_square_radio_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.shape_square_radio_2.setText("")
        self.shape_square_radio_2.setObjectName("shape_square_radio_2")
        self.formLayout_3.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.shape_square_radio_2)
        self.line_13 = QtWidgets.QFrame(self.scrollAreaWidgetContents_2)
        self.line_13.setMinimumSize(QtCore.QSize(25, 0))
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.formLayout_3.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.line_13)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.formLayout_3.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.label_42)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_23.setObjectName("label_23")
        self.formLayout_3.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_24 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_24.setObjectName("label_24")
        self.formLayout_3.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.shape_thick_radio_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.shape_thick_radio_2.setText("")
        self.shape_thick_radio_2.setObjectName("shape_thick_radio_2")
        self.formLayout_3.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.shape_thick_radio_2)
        self.shape_thin_radio_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.shape_thin_radio_2.setText("")
        self.shape_thin_radio_2.setObjectName("shape_thin_radio_2")
        self.formLayout_3.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.shape_thin_radio_2)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea_2)
        self.horizontalLayout_5.addWidget(self.pizza_two_groupbox_1)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.screen_1_box)
        self.screen_2_box = QtWidgets.QGroupBox(self.centralwidget)
        self.screen_2_box.setStyleSheet("QGroupBox {border: none}")
        self.screen_2_box.setTitle("")
        self.screen_2_box.setObjectName("screen_2_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.screen_2_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_48 = QtWidgets.QLabel(self.screen_2_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_48.setFont(font)
        self.label_48.setAlignment(QtCore.Qt.AlignCenter)
        self.label_48.setObjectName("label_48")
        self.verticalLayout_2.addWidget(self.label_48)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.pizza_one_groupbox_2 = QtWidgets.QGroupBox(self.screen_2_box)
        self.pizza_one_groupbox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pizza_one_groupbox_2.sizePolicy().hasHeightForWidth())
        self.pizza_one_groupbox_2.setSizePolicy(sizePolicy)
        self.pizza_one_groupbox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pizza_one_groupbox_2.setObjectName("pizza_one_groupbox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.pizza_one_groupbox_2)
        self.verticalLayout_5.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.pizza_one_groupbox_2)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 531, 163))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.formLayout_4 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_3)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.size_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.size_label.setObjectName("size_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.size_label)
        self.size_cost_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.size_cost_label.setObjectName("size_cost_label")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.size_cost_label)
        self.toppings_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.toppings_label.setObjectName("toppings_label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toppings_label)
        self.toppings_cost_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.toppings_cost_label.setObjectName("toppings_cost_label")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toppings_cost_label)
        self.shape_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.shape_label.setObjectName("shape_label")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.shape_label)
        self.shape_cost_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.shape_cost_label.setObjectName("shape_cost_label")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.shape_cost_label)
        self.crust_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.crust_label.setObjectName("crust_label")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.crust_label)
        self.crust_cost_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.crust_cost_label.setObjectName("crust_cost_label")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.crust_cost_label)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line)
        self.label_45 = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.label_45.setObjectName("label_45")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.subcost_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.subcost_label.setObjectName("subcost_label")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.subcost_label)
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.addWidget(self.scrollArea_3)
        self.horizontalLayout_9.addWidget(self.pizza_one_groupbox_2)
        self.pizza_two_groupbox_2 = QtWidgets.QGroupBox(self.screen_2_box)
        self.pizza_two_groupbox_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pizza_two_groupbox_2.sizePolicy().hasHeightForWidth())
        self.pizza_two_groupbox_2.setSizePolicy(sizePolicy)
        self.pizza_two_groupbox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pizza_two_groupbox_2.setObjectName("pizza_two_groupbox_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pizza_two_groupbox_2)
        self.verticalLayout_7.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.scrollArea_4 = QtWidgets.QScrollArea(self.pizza_two_groupbox_2)
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollArea_4.setObjectName("scrollArea_4")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 530, 163))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.formLayout_5 = QtWidgets.QFormLayout(self.scrollAreaWidgetContents_4)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_7 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.size_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.size_label_2.setObjectName("size_label_2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.size_label_2)
        self.size_cost_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.size_cost_label_2.setObjectName("size_cost_label_2")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.size_cost_label_2)
        self.toppings_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.toppings_label_2.setObjectName("toppings_label_2")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.toppings_label_2)
        self.toppings_cost_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.toppings_cost_label_2.setObjectName("toppings_cost_label_2")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.toppings_cost_label_2)
        self.shape_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.shape_label_2.setObjectName("shape_label_2")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.shape_label_2)
        self.shape_cost_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.shape_cost_label_2.setObjectName("shape_cost_label_2")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.shape_cost_label_2)
        self.crust_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.crust_label_2.setObjectName("crust_label_2")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.crust_label_2)
        self.crust_cost_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.crust_cost_label_2.setObjectName("crust_cost_label_2")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.crust_cost_label_2)
        self.line_2 = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_2)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_46.setObjectName("label_46")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.subcost_label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.subcost_label_2.setObjectName("subcost_label_2")
        self.formLayout_5.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.subcost_label_2)
        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)
        self.verticalLayout_7.addWidget(self.scrollArea_4)
        self.horizontalLayout_9.addWidget(self.pizza_two_groupbox_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.label_47 = QtWidgets.QLabel(self.screen_2_box)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.verticalLayout_2.addWidget(self.label_47)
        self.verticalLayout.addWidget(self.screen_2_box)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.clear_button = QtWidgets.QPushButton(self.centralwidget)
        self.clear_button.setObjectName("clear_button")
        self.gridLayout.addWidget(self.clear_button, 0, 3, 1, 1)
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setObjectName("calculate_button")
        self.gridLayout.addWidget(self.calculate_button, 0, 1, 1, 2)
        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setObjectName("exit_button")
        self.gridLayout.addWidget(self.exit_button, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1204, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pizza Ordering Program"))
        self.label_4.setText(_translate("MainWindow", "Contestant #"))
        self.label_5.setText(_translate("MainWindow", "Pizza Ordering Program"))
        self.label_3.setText(_translate("MainWindow", "Program #"))
        self.label.setText(_translate("MainWindow", "Customer Name"))
        self.label_2.setText(_translate("MainWindow", "Pizzas ordering"))
        self.pizzas_ordering_combobox.setItemText(0, _translate("MainWindow", "1"))
        self.pizzas_ordering_combobox.setItemText(1, _translate("MainWindow", "2"))
        self.pizza_one_groupbox_1.setTitle(_translate("MainWindow", "Pizza #1"))
        self.label_9.setText(_translate("MainWindow", "Size"))
        self.label_10.setText(_translate("MainWindow", "Large - $15.95"))
        self.label_11.setText(_translate("MainWindow", "Medium - $12.95"))
        self.label_12.setText(_translate("MainWindow", "Small - $10.95"))
        self.label_37.setText(_translate("MainWindow", "Toppings"))
        self.label_38.setText(_translate("MainWindow", "Cost per topping: $1.25"))
        self.label_30.setText(_translate("MainWindow", "Toppings"))
        self.label_31.setText(_translate("MainWindow", "Shape"))
        self.label_13.setText(_translate("MainWindow", "Round"))
        self.label_16.setText(_translate("MainWindow", "Square"))
        self.label_39.setText(_translate("MainWindow", "Crust"))
        self.label_14.setText(_translate("MainWindow", "Thick"))
        self.label_15.setText(_translate("MainWindow", "Thin"))
        self.pizza_two_groupbox_1.setTitle(_translate("MainWindow", "Pizza #2"))
        self.label_17.setText(_translate("MainWindow", "Size"))
        self.label_18.setText(_translate("MainWindow", "Large - $15.95"))
        self.label_19.setText(_translate("MainWindow", "Medium - $12.95"))
        self.label_20.setText(_translate("MainWindow", "Small - $10.95"))
        self.label_40.setText(_translate("MainWindow", "Toppings"))
        self.label_41.setText(_translate("MainWindow", "Cost per topping: $1.25"))
        self.label_32.setText(_translate("MainWindow", "Toppings"))
        self.label_33.setText(_translate("MainWindow", "Shape"))
        self.label_21.setText(_translate("MainWindow", "Round"))
        self.label_22.setText(_translate("MainWindow", "Square"))
        self.label_42.setText(_translate("MainWindow", "Crust"))
        self.label_23.setText(_translate("MainWindow", "Thick"))
        self.label_24.setText(_translate("MainWindow", "Thin"))
        self.label_48.setText(_translate("MainWindow", "Customer Name: Customer"))
        self.pizza_one_groupbox_2.setTitle(_translate("MainWindow", "Pizza #1"))
        self.label_6.setText(_translate("MainWindow", "Your order:"))
        self.size_label.setText(_translate("MainWindow", "Size - Large"))
        self.size_cost_label.setText(_translate("MainWindow", "$15.95"))
        self.toppings_label.setText(_translate("MainWindow", "Toppings - 4"))
        self.toppings_cost_label.setText(_translate("MainWindow", "$5.00"))
        self.shape_label.setText(_translate("MainWindow", "Shape - Round"))
        self.shape_cost_label.setText(_translate("MainWindow", "$0.00"))
        self.crust_label.setText(_translate("MainWindow", "Crust - Thick"))
        self.crust_cost_label.setText(_translate("MainWindow", "$0.00"))
        self.label_45.setText(_translate("MainWindow", "Subtotal"))
        self.subcost_label.setText(_translate("MainWindow", "$20.95"))
        self.pizza_two_groupbox_2.setTitle(_translate("MainWindow", "Pizza #2"))
        self.label_7.setText(_translate("MainWindow", "Your order:"))
        self.size_label_2.setText(_translate("MainWindow", "Size - Large"))
        self.size_cost_label_2.setText(_translate("MainWindow", "$15.95"))
        self.toppings_label_2.setText(_translate("MainWindow", "Toppings - 4"))
        self.toppings_cost_label_2.setText(_translate("MainWindow", "$5.00"))
        self.shape_label_2.setText(_translate("MainWindow", "Shape - Round"))
        self.shape_cost_label_2.setText(_translate("MainWindow", "$0.00"))
        self.crust_label_2.setText(_translate("MainWindow", "Crust - Thick"))
        self.crust_cost_label_2.setText(_translate("MainWindow", "$0.00"))
        self.label_46.setText(_translate("MainWindow", "Subtotal"))
        self.subcost_label_2.setText(_translate("MainWindow", "$20.95"))
        self.label_47.setText(_translate("MainWindow", "Total: $20.95"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))

# Form implementation generated from reading ui file 'd:\LTTKUD\N06_LTUDKT_68IT1,2_BTNhomSo1\view\finalgui.ui'
#
# Created by: PyQt6 UI code generator 6.9.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("")
        self.groupBox = QtWidgets.QGroupBox(parent=Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 611, 114))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setStyleSheet("QPushButton {\n"
"    background-color: #2d2d2d;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #3c3c3c;\n"
"}\n"
"")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addBtn.sizePolicy().hasHeightForWidth())
        self.addBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.addBtn.setFont(font)
        self.addBtn.setStyleSheet("background-color: #4caf50\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\LTTKUD\\N06_LTUDKT_68IT1,2_BTNhomSo1\\view\\icon/add48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addBtn.setIcon(icon)
        self.addBtn.setIconSize(QtCore.QSize(48, 48))
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.editBtn = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editBtn.sizePolicy().hasHeightForWidth())
        self.editBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.editBtn.setFont(font)
        self.editBtn.setStyleSheet("background-color: #2196f3")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("d:\\LTTKUD\\N06_LTUDKT_68IT1,2_BTNhomSo1\\view\\icon/edit48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.editBtn.setIcon(icon1)
        self.editBtn.setIconSize(QtCore.QSize(48, 48))
        self.editBtn.setObjectName("editBtn")
        self.horizontalLayout.addWidget(self.editBtn)
        self.delBtn = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delBtn.sizePolicy().hasHeightForWidth())
        self.delBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.delBtn.setFont(font)
        self.delBtn.setStyleSheet("background-color: #f44336")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("d:\\LTTKUD\\N06_LTUDKT_68IT1,2_BTNhomSo1\\view\\icon/del48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.delBtn.setIcon(icon2)
        self.delBtn.setIconSize(QtCore.QSize(48, 48))
        self.delBtn.setObjectName("delBtn")
        self.horizontalLayout.addWidget(self.delBtn)
        self.line = QtWidgets.QFrame(parent=self.groupBox)
        self.line.setStyleSheet("background-color : #fff")
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.comboBox = QtWidgets.QComboBox(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.tableStudent = QtWidgets.QTableView(parent=Form)
        self.tableStudent.setGeometry(QtCore.QRect(10, 160, 1171, 651))
        self.tableStudent.setStyleSheet("color: white;")
        self.tableStudent.setObjectName("tableStudent")
        self.comboKey1 = QtWidgets.QComboBox(parent=Form)
        self.comboKey1.setGeometry(QtCore.QRect(760, 30, 111, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboKey1.sizePolicy().hasHeightForWidth())
        self.comboKey1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboKey1.setFont(font)
        self.comboKey1.setStyleSheet("color: white;")
        self.comboKey1.setObjectName("comboKey1")
        self.comboKey1.addItem("")
        self.comboKey1.addItem("")
        self.comboKey1.addItem("")
        self.txtKey1 = QtWidgets.QLineEdit(parent=Form)
        self.txtKey1.setGeometry(QtCore.QRect(890, 30, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.txtKey1.setFont(font)
        self.txtKey1.setStyleSheet("color: white;")
        self.txtKey1.setObjectName("txtKey1")
        self.search1Btn = QtWidgets.QPushButton(parent=Form)
        self.search1Btn.setGeometry(QtCore.QRect(1120, 30, 31, 31))
        self.search1Btn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("d:\\LTTKUD\\N06_LTUDKT_68IT1,2_BTNhomSo1\\view\\../icon/sreach48.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.search1Btn.setIcon(icon3)
        self.search1Btn.setIconSize(QtCore.QSize(20, 20))
        self.search1Btn.setObjectName("search1Btn")
        self.txtKey2 = QtWidgets.QLineEdit(parent=Form)
        self.txtKey2.setGeometry(QtCore.QRect(890, 90, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.txtKey2.setFont(font)
        self.txtKey2.setStyleSheet("color: white;")
        self.txtKey2.setObjectName("txtKey2")
        self.search2Btn = QtWidgets.QPushButton(parent=Form)
        self.search2Btn.setGeometry(QtCore.QRect(1120, 90, 31, 31))
        self.search2Btn.setText("")
        self.search2Btn.setIcon(icon3)
        self.search2Btn.setIconSize(QtCore.QSize(20, 20))
        self.search2Btn.setObjectName("search2Btn")
        self.comboKey2 = QtWidgets.QComboBox(parent=Form)
        self.comboKey2.setGeometry(QtCore.QRect(760, 90, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.comboKey2.setFont(font)
        self.comboKey2.setStyleSheet("color: white;")
        self.comboKey2.setObjectName("comboKey2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Functions"))
        self.addBtn.setText(_translate("Form", "Add"))
        self.editBtn.setText(_translate("Form", "Edit"))
        self.delBtn.setText(_translate("Form", "Delete"))
        self.comboBox.setCurrentText(_translate("Form", "All"))
        self.comboBox.setItemText(0, _translate("Form", "All"))
        self.comboBox.setItemText(1, _translate("Form", "Regular"))
        self.comboBox.setItemText(2, _translate("Form", "InService"))
        self.comboKey1.setItemText(0, _translate("Form", "ID"))
        self.comboKey1.setItemText(1, _translate("Form", "Name"))
        self.comboKey1.setItemText(2, _translate("Form", "Department"))

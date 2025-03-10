# Form implementation generated from reading ui file 'UI_Files/disabled.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.disabledList_frame = QtWidgets.QFrame(parent=Form)
        self.disabledList_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.disabledList_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.disabledList_frame.setObjectName("disabledList_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.disabledList_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.disabledList_frame)
        self.lineEdit.setBaseSize(QtCore.QSize(0, 24))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.disabledList = QtWidgets.QListWidget(parent=self.disabledList_frame)
        self.disabledList.setObjectName("disabledList")
        self.verticalLayout_2.addWidget(self.disabledList)
        self.disabledNote = QtWidgets.QLabel(parent=self.disabledList_frame)
        self.disabledNote.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.disabledNote.setWordWrap(True)
        self.disabledNote.setObjectName("disabledNote")
        self.verticalLayout_2.addWidget(self.disabledNote)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            5,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem1)
        self.applyButton = QtWidgets.QPushButton(parent=self.disabledList_frame)
        self.applyButton.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.applyButton.setObjectName("applyButton")
        self.horizontalLayout_2.addWidget(self.applyButton)
        self.cancelButton = QtWidgets.QPushButton(parent=self.disabledList_frame)
        self.cancelButton.setCursor(
            QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor)
        )
        self.cancelButton.setObjectName("cancelButton")
        self.horizontalLayout_2.addWidget(self.cancelButton)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            5,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.verticalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addWidget(self.disabledList_frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(
            _translate("Form", "Process Name, e.g. explorer.exe")
        )
        self.disabledNote.setText(
            _translate(
                "Form",
                "Note: Adding any process to this list would turn off the functionality of this section for that.",
            )
        )
        self.applyButton.setText(_translate("Form", "Apply"))
        self.cancelButton.setText(_translate("Form", "Cancel"))

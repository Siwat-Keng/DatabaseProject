from PyQt5 import QtCore, QtGui, QtWidgets
import DiseaseController

class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 361)
        self.lineEdit = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 20, 161, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 141, 20))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(150, 70, 171, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 70, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 131, 20))
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(self.Dialog)
        self.comboBox.setGeometry(QtCore.QRect(160, 240, 151, 22))
        self.comboBox.setObjectName("comboBox")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(150, 120, 161, 87))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label_7 = QtWidgets.QLabel(self.Dialog)
        self.label_7.setGeometry(QtCore.QRect(50, 240, 91, 20))
        self.label_7.setObjectName("label_7")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 310, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 310, 121, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.edit)
        self.pushButton_2.clicked.connect(self.back)        

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Edit by Disease ID :"))
        self.label_5.setText(_translate("Dialog", " Disease Name :"))
        self.label_6.setText(_translate("Dialog", "Disease Description :"))
        self.label_7.setText(_translate("Dialog", "Cure by Drug :"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.pushButton.setText(_translate("Dialog", "Edit"))

    def show(self):
        self.Dialog.show()


    def edit(self):
        diseaseID = self.lineEdit.text()
        diseaseName = self.lineEdit_3.text()
        diseaseDesc = self.plainTextEdit.toPlainText()
        Drug = str(self.comboBox.currentText())
        #TODO edit diseaseName diseaseDesc and Drug by diseaseID


    def back(self):
        self.ui = DiseaseController.Ui_Dialog()
        self.Dialog.hide()
        self.ui.show() 
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())

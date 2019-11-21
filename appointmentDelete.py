from PyQt5 import QtCore, QtGui, QtWidgets
import patientController


class Ui_Dialog(object):
    def __init__(self):
        self.Dialog = QtWidgets.QDialog()
        self.Dialog.setObjectName("Dialog")
        self.Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(self.Dialog)
        self.pushButton.setGeometry(QtCore.QRect(96, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(246, 220, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(176, 110, 161, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 141, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 40, 171, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.Dialog)
        self.label_3.setGeometry(QtCore.QRect(60, 40, 101, 20))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(self.Dialog)
        QtCore.QMetaObject.connectSlotsByName(self.Dialog)

        self.pushButton.clicked.connect(self.delete)
        self.pushButton_2.clicked.connect(self.cancel)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Delete"))
        self.pushButton_2.setText(_translate("Dialog", "Cancel"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Selected Appointment :"))
        self.label_3.setText(_translate("Dialog", "Appointment ID :"))

    def show(self):
        self.Dialog.show()

    def delete(self):
        appointID = self.lineEdit_2.text()
        #TODO add appointment(from database) to self.textBrowser then delete???

        #example
        self.textBrowser.add("appointment1")
        self.textBrowser.add("appointment2")
        self.textBrowser.add("appointment3")
        

    def cancel(self):
        self.ui = patientController.Ui_Dialog()
        self.ui.show()
        self.Dialog.close()
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv) 
    ui = Ui_Dialog()
    ui.show()
    sys.exit(app.exec_())

# Form implementation generated from reading ui file 'exca_sum.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SumWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        MainWindow.setMaximumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_summary = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_summary.setGeometry(QtCore.QRect(140, 30, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setUnderline(True)
        self.label_summary.setFont(font)
        self.label_summary.setObjectName("label_summary")
        self.input_income = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_income.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.input_income.setObjectName("input_income")
        self.input_goal = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_goal.setGeometry(QtCore.QRect(90, 180, 113, 20))
        self.input_goal.setObjectName("input_goal")
        self.label_goal = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_goal.setGeometry(QtCore.QRect(30, 180, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_goal.setFont(font)
        self.label_goal.setObjectName("label_goal")
        self.label_income = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_income.setGeometry(QtCore.QRect(20, 100, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_income.setFont(font)
        self.label_income.setObjectName("label_income")
        self.button_upda = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_upda.setGeometry(QtCore.QRect(250, 120, 91, 51))
        self.button_upda.setObjectName("button_upda")
        self.label_month = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_month.setGeometry(QtCore.QRect(30, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_month.setFont(font)
        self.label_month.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_month.setLineWidth(2)
        self.label_month.setObjectName("label_month")
        self.label_time = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_time.setGeometry(QtCore.QRect(30, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_time.setFont(font)
        self.label_time.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_time.setLineWidth(2)
        self.label_time.setObjectName("label_time")
        self.label_status = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(30, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_status.setFont(font)
        self.label_status.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_status.setLineWidth(2)
        self.label_status.setObjectName("label_status")
        self.label_out_month = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_out_month.setGeometry(QtCore.QRect(200, 250, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_out_month.setFont(font)
        self.label_out_month.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_out_month.setLineWidth(2)
        self.label_out_month.setText("")
        self.label_out_month.setObjectName("label_out_month")
        self.label_out_time = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_out_time.setGeometry(QtCore.QRect(200, 280, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_out_time.setFont(font)
        self.label_out_time.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_out_time.setLineWidth(2)
        self.label_out_time.setText("")
        self.label_out_time.setObjectName("label_out_time")
        self.label_out_status = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_out_status.setGeometry(QtCore.QRect(200, 310, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_out_status.setFont(font)
        self.label_out_status.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.label_out_status.setLineWidth(2)
        self.label_out_status.setText("")
        self.label_out_status.setObjectName("label_out_status")
        self.input_save = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.input_save.setGeometry(QtCore.QRect(90, 140, 113, 20))
        self.input_save.setText("")
        self.input_save.setObjectName("input_save")
        self.label_savings = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_savings.setGeometry(QtCore.QRect(10, 140, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_savings.setFont(font)
        self.label_savings.setObjectName("label_savings")
        self.button_return = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button_return.setGeometry(QtCore.QRect(10, 10, 91, 61))
        self.button_return.setObjectName("button_return")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ExCA_Summary"))
        self.label_summary.setText(_translate("MainWindow", "Summary"))
        self.label_goal.setText(_translate("MainWindow", "GOAL:"))
        self.label_income.setText(_translate("MainWindow", "INCOME:"))
        self.button_upda.setText(_translate("MainWindow", "UPDATE"))
        self.label_month.setText(_translate("MainWindow", "Monthly Profit"))
        self.label_time.setText(_translate("MainWindow", "Time To Reach Goal"))
        self.label_status.setText(_translate("MainWindow", "$ Status"))
        self.label_savings.setText(_translate("MainWindow", "SAVINGS:"))
        self.button_return.setText(_translate("MainWindow", "RETURN"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

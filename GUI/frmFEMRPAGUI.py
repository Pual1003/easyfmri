# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'frmFEMRPAGUI.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmFEMRPA(object):
    def setupUi(self, frmFEMRPA):
        frmFEMRPA.setObjectName("frmFEMRPA")
        frmFEMRPA.resize(758, 691)
        self.btnInFile = QtWidgets.QPushButton(frmFEMRPA)
        self.btnInFile.setGeometry(QtCore.QRect(690, 20, 51, 32))
        self.btnInFile.setObjectName("btnInFile")
        self.label_33 = QtWidgets.QLabel(frmFEMRPA)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 131, 16))
        self.label_33.setObjectName("label_33")
        self.btnOutFile = QtWidgets.QPushButton(frmFEMRPA)
        self.btnOutFile.setGeometry(QtCore.QRect(690, 60, 51, 32))
        self.btnOutFile.setObjectName("btnOutFile")
        self.txtInFile = QtWidgets.QLineEdit(frmFEMRPA)
        self.txtInFile.setGeometry(QtCore.QRect(160, 20, 521, 21))
        self.txtInFile.setText("")
        self.txtInFile.setObjectName("txtInFile")
        self.btnConvert = QtWidgets.QPushButton(frmFEMRPA)
        self.btnConvert.setGeometry(QtCore.QRect(590, 640, 141, 32))
        self.btnConvert.setObjectName("btnConvert")
        self.label_35 = QtWidgets.QLabel(frmFEMRPA)
        self.label_35.setGeometry(QtCore.QRect(30, 60, 111, 16))
        self.label_35.setObjectName("label_35")
        self.txtOutFile = QtWidgets.QLineEdit(frmFEMRPA)
        self.txtOutFile.setGeometry(QtCore.QRect(160, 60, 521, 21))
        self.txtOutFile.setText("")
        self.txtOutFile.setObjectName("txtOutFile")
        self.btnClose = QtWidgets.QPushButton(frmFEMRPA)
        self.btnClose.setGeometry(QtCore.QRect(30, 640, 141, 32))
        self.btnClose.setObjectName("btnClose")
        self.tabWidget = QtWidgets.QTabWidget(frmFEMRPA)
        self.tabWidget.setGeometry(QtCore.QRect(30, 100, 701, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.txtOTask = QtWidgets.QLineEdit(self.tab)
        self.txtOTask.setGeometry(QtCore.QRect(420, 290, 113, 21))
        self.txtOTask.setObjectName("txtOTask")
        self.txtmLabel = QtWidgets.QComboBox(self.tab)
        self.txtmLabel.setGeometry(QtCore.QRect(260, 170, 121, 26))
        self.txtmLabel.setEditable(True)
        self.txtmLabel.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtmLabel.setObjectName("txtmLabel")
        self.cbmLabel = QtWidgets.QCheckBox(self.tab)
        self.cbmLabel.setGeometry(QtCore.QRect(140, 170, 121, 20))
        self.cbmLabel.setObjectName("cbmLabel")
        self.txtScan = QtWidgets.QComboBox(self.tab)
        self.txtScan.setGeometry(QtCore.QRect(260, 450, 121, 26))
        self.txtScan.setEditable(True)
        self.txtScan.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtScan.setObjectName("txtScan")
        self.txtTask = QtWidgets.QComboBox(self.tab)
        self.txtTask.setGeometry(QtCore.QRect(260, 290, 121, 26))
        self.txtTask.setEditable(True)
        self.txtTask.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtTask.setObjectName("txtTask")
        self.txtSubject = QtWidgets.QComboBox(self.tab)
        self.txtSubject.setGeometry(QtCore.QRect(260, 250, 121, 26))
        self.txtSubject.setEditable(True)
        self.txtSubject.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtSubject.setObjectName("txtSubject")
        self.txtOmLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOmLabel.setGeometry(QtCore.QRect(420, 170, 113, 21))
        self.txtOmLabel.setObjectName("txtOmLabel")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 60, 16))
        self.label_2.setObjectName("label_2")
        self.txtODM = QtWidgets.QLineEdit(self.tab)
        self.txtODM.setGeometry(QtCore.QRect(420, 130, 113, 21))
        self.txtODM.setObjectName("txtODM")
        self.cbTask = QtWidgets.QCheckBox(self.tab)
        self.cbTask.setGeometry(QtCore.QRect(140, 290, 81, 20))
        self.cbTask.setChecked(True)
        self.cbTask.setObjectName("cbTask")
        self.txtDM = QtWidgets.QComboBox(self.tab)
        self.txtDM.setGeometry(QtCore.QRect(260, 130, 121, 26))
        self.txtDM.setEditable(True)
        self.txtDM.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtDM.setObjectName("txtDM")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(140, 90, 60, 16))
        self.label_3.setObjectName("label_3")
        self.cbNScan = QtWidgets.QCheckBox(self.tab)
        self.cbNScan.setGeometry(QtCore.QRect(140, 450, 91, 20))
        self.cbNScan.setChecked(False)
        self.cbNScan.setObjectName("cbNScan")
        self.cbCond = QtWidgets.QCheckBox(self.tab)
        self.cbCond.setGeometry(QtCore.QRect(140, 410, 101, 20))
        self.cbCond.setChecked(True)
        self.cbCond.setObjectName("cbCond")
        self.txtCol = QtWidgets.QComboBox(self.tab)
        self.txtCol.setGeometry(QtCore.QRect(260, 210, 121, 26))
        self.txtCol.setEditable(True)
        self.txtCol.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCol.setObjectName("txtCol")
        self.cbCol = QtWidgets.QCheckBox(self.tab)
        self.cbCol.setGeometry(QtCore.QRect(140, 210, 111, 20))
        self.cbCol.setChecked(True)
        self.cbCol.setObjectName("cbCol")
        self.txtOCond = QtWidgets.QLineEdit(self.tab)
        self.txtOCond.setGeometry(QtCore.QRect(420, 410, 113, 21))
        self.txtOCond.setObjectName("txtOCond")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(300, 20, 61, 16))
        self.label.setObjectName("label")
        self.txtOLabel = QtWidgets.QLineEdit(self.tab)
        self.txtOLabel.setGeometry(QtCore.QRect(420, 90, 113, 21))
        self.txtOLabel.setObjectName("txtOLabel")
        self.txtCounter = QtWidgets.QComboBox(self.tab)
        self.txtCounter.setGeometry(QtCore.QRect(260, 370, 121, 26))
        self.txtCounter.setEditable(True)
        self.txtCounter.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCounter.setObjectName("txtCounter")
        self.txtOScan = QtWidgets.QLineEdit(self.tab)
        self.txtOScan.setGeometry(QtCore.QRect(420, 450, 113, 21))
        self.txtOScan.setObjectName("txtOScan")
        self.cbCounter = QtWidgets.QCheckBox(self.tab)
        self.cbCounter.setGeometry(QtCore.QRect(140, 370, 81, 20))
        self.cbCounter.setChecked(False)
        self.cbCounter.setObjectName("cbCounter")
        self.txtOCol = QtWidgets.QLineEdit(self.tab)
        self.txtOCol.setGeometry(QtCore.QRect(420, 210, 113, 21))
        self.txtOCol.setObjectName("txtOCol")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(450, 20, 61, 16))
        self.label_5.setObjectName("label_5")
        self.txtData = QtWidgets.QComboBox(self.tab)
        self.txtData.setGeometry(QtCore.QRect(260, 50, 121, 26))
        self.txtData.setEditable(True)
        self.txtData.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtData.setObjectName("txtData")
        self.txtRun = QtWidgets.QComboBox(self.tab)
        self.txtRun.setGeometry(QtCore.QRect(260, 330, 121, 26))
        self.txtRun.setEditable(True)
        self.txtRun.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtRun.setObjectName("txtRun")
        self.txtCond = QtWidgets.QComboBox(self.tab)
        self.txtCond.setGeometry(QtCore.QRect(260, 410, 121, 26))
        self.txtCond.setEditable(True)
        self.txtCond.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.txtCond.setObjectName("txtCond")
        self.txtOCounter = QtWidgets.QLineEdit(self.tab)
        self.txtOCounter.setGeometry(QtCore.QRect(420, 370, 113, 21))
        self.txtOCounter.setObjectName("txtOCounter")
        self.txtOSubject = QtWidgets.QLineEdit(self.tab)
        self.txtOSubject.setGeometry(QtCore.QRect(420, 250, 113, 21))
        self.txtOSubject.setObjectName("txtOSubject")
        self.cbRun = QtWidgets.QCheckBox(self.tab)
        self.cbRun.setGeometry(QtCore.QRect(140, 330, 81, 20))
        self.cbRun.setChecked(True)
        self.cbRun.setObjectName("cbRun")
        self.txtOData = QtWidgets.QLineEdit(self.tab)
        self.txtOData.setGeometry(QtCore.QRect(420, 50, 113, 21))
        self.txtOData.setObjectName("txtOData")
        self.txtORun = QtWidgets.QLineEdit(self.tab)
        self.txtORun.setGeometry(QtCore.QRect(420, 330, 113, 21))
        self.txtORun.setObjectName("txtORun")
        self.cbSubject = QtWidgets.QCheckBox(self.tab)
        self.cbSubject.setGeometry(QtCore.QRect(140, 250, 111, 20))
        self.cbSubject.setChecked(True)
        self.cbSubject.setObjectName("cbSubject")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 130, 111, 16))
        self.label_4.setObjectName("label_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 201, 16))
        self.label_6.setObjectName("label_6")
        self.txtSigma = QtWidgets.QSpinBox(self.tab_2)
        self.txtSigma.setGeometry(QtCore.QRect(250, 20, 171, 24))
        self.txtSigma.setMinimum(1)
        self.txtSigma.setMaximum(1000000000)
        self.txtSigma.setObjectName("txtSigma")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(frmFEMRPA)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmFEMRPA)
        frmFEMRPA.setTabOrder(self.txtInFile, self.btnInFile)
        frmFEMRPA.setTabOrder(self.btnInFile, self.txtOutFile)
        frmFEMRPA.setTabOrder(self.txtOutFile, self.btnOutFile)
        frmFEMRPA.setTabOrder(self.btnOutFile, self.tabWidget)
        frmFEMRPA.setTabOrder(self.tabWidget, self.cbmLabel)
        frmFEMRPA.setTabOrder(self.cbmLabel, self.cbCol)
        frmFEMRPA.setTabOrder(self.cbCol, self.cbTask)
        frmFEMRPA.setTabOrder(self.cbTask, self.cbRun)
        frmFEMRPA.setTabOrder(self.cbRun, self.cbCounter)
        frmFEMRPA.setTabOrder(self.cbCounter, self.cbCond)
        frmFEMRPA.setTabOrder(self.cbCond, self.cbNScan)
        frmFEMRPA.setTabOrder(self.cbNScan, self.txtData)
        frmFEMRPA.setTabOrder(self.txtData, self.txtSubject)
        frmFEMRPA.setTabOrder(self.txtSubject, self.txtmLabel)
        frmFEMRPA.setTabOrder(self.txtmLabel, self.txtCol)
        frmFEMRPA.setTabOrder(self.txtCol, self.txtDM)
        frmFEMRPA.setTabOrder(self.txtDM, self.txtTask)
        frmFEMRPA.setTabOrder(self.txtTask, self.txtRun)
        frmFEMRPA.setTabOrder(self.txtRun, self.txtCounter)
        frmFEMRPA.setTabOrder(self.txtCounter, self.txtScan)
        frmFEMRPA.setTabOrder(self.txtScan, self.txtOData)
        frmFEMRPA.setTabOrder(self.txtOData, self.txtOLabel)
        frmFEMRPA.setTabOrder(self.txtOLabel, self.txtOSubject)
        frmFEMRPA.setTabOrder(self.txtOSubject, self.txtOmLabel)
        frmFEMRPA.setTabOrder(self.txtOmLabel, self.txtOCol)
        frmFEMRPA.setTabOrder(self.txtOCol, self.txtODM)
        frmFEMRPA.setTabOrder(self.txtODM, self.txtOTask)
        frmFEMRPA.setTabOrder(self.txtOTask, self.txtORun)
        frmFEMRPA.setTabOrder(self.txtORun, self.txtOCounter)
        frmFEMRPA.setTabOrder(self.txtOCounter, self.txtOCond)
        frmFEMRPA.setTabOrder(self.txtOCond, self.txtOScan)
        frmFEMRPA.setTabOrder(self.txtOScan, self.txtCond)
        frmFEMRPA.setTabOrder(self.txtCond, self.btnConvert)
        frmFEMRPA.setTabOrder(self.btnConvert, self.btnClose)

    def retranslateUi(self, frmFEMRPA):
        _translate = QtCore.QCoreApplication.translate
        frmFEMRPA.setWindowTitle(_translate("frmFEMRPA", "Multi Region Pattern Analysis (Snapshots)"))
        self.btnInFile.setText(_translate("frmFEMRPA", "..."))
        self.label_33.setText(_translate("frmFEMRPA", "Input Data"))
        self.btnOutFile.setText(_translate("frmFEMRPA", "..."))
        self.btnConvert.setText(_translate("frmFEMRPA", "Convert"))
        self.label_35.setText(_translate("frmFEMRPA", "Output Data"))
        self.btnClose.setText(_translate("frmFEMRPA", "Close"))
        self.txtOTask.setText(_translate("frmFEMRPA", "task"))
        self.cbmLabel.setText(_translate("frmFEMRPA", "Label (matrix)"))
        self.txtOmLabel.setText(_translate("frmFEMRPA", "mlabel"))
        self.label_2.setText(_translate("frmFEMRPA", "Data"))
        self.txtODM.setText(_translate("frmFEMRPA", "design"))
        self.cbTask.setText(_translate("frmFEMRPA", "Task"))
        self.label_3.setText(_translate("frmFEMRPA", "Label"))
        self.cbNScan.setText(_translate("frmFEMRPA", "NScan"))
        self.cbCond.setText(_translate("frmFEMRPA", "Condition"))
        self.cbCol.setText(_translate("frmFEMRPA", "Coordinate"))
        self.txtOCond.setText(_translate("frmFEMRPA", "condition"))
        self.label.setText(_translate("frmFEMRPA", "Input"))
        self.txtOLabel.setText(_translate("frmFEMRPA", "label"))
        self.txtOScan.setText(_translate("frmFEMRPA", "nscan"))
        self.cbCounter.setText(_translate("frmFEMRPA", "Counter"))
        self.txtOCol.setText(_translate("frmFEMRPA", "coordinate"))
        self.label_5.setText(_translate("frmFEMRPA", "Output"))
        self.txtOCounter.setText(_translate("frmFEMRPA", "counter"))
        self.txtOSubject.setText(_translate("frmFEMRPA", "subject"))
        self.cbRun.setText(_translate("frmFEMRPA", "Run"))
        self.txtOData.setText(_translate("frmFEMRPA", "data"))
        self.txtORun.setText(_translate("frmFEMRPA", "run"))
        self.cbSubject.setText(_translate("frmFEMRPA", "Subject"))
        self.label_4.setText(_translate("frmFEMRPA", "Design Matrix"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("frmFEMRPA", "Data"))
        self.label_6.setText(_translate("frmFEMRPA", "Sigma (Gaussian kernel)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("frmFEMRPA", "Parameters"))


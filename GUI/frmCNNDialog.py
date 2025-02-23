# Copyright (c) 2014--2019 Muhammad Yousefnezhad
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from PyQt5.QtWidgets import *
import PyQt5.QtCore as QtCore


class frmPool(QDialog):
    def __init__(self):
        super().__init__()
        self.pool = None
        self.kernel = None
        self.isAdd = False
        self.title = 'Add a Pool'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 150
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label1 = QLabel()
        self.label1.setText("Pool Type:")
        self.cbType = QComboBox()
        self.cbType.addItem("Max Pool","max3")
        self.cbType.addItem("Average Pool", "avg3")
        self.label2 = QLabel()
        self.label2.setText("Kernel Size:")
        self.txtKernel = QSpinBox()
        self.txtKernel.setMinimum(1)
        self.txtKernel.setMaximum(100000)
        self.txtKernel.setValue(2)
        self.btnAdd = QPushButton()
        self.btnAdd.setText("Add")
        self.btnAdd.clicked.connect(self.btnAdd_onclick)
        self.btnExit = QPushButton()
        self.btnExit.setText("Exit")
        self.btnExit.clicked.connect(self.btnExit_onclick)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.cbType)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.txtKernel)
        self.layout.addWidget(self.btnAdd)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
        self.exec_()

    def btnExit_onclick(self):
        self.close()

    def btnAdd_onclick(self):
        self.pool = self.cbType.currentData()
        self.kernel = self.txtKernel.value()
        self.isAdd = True
        self.close()


class frmAF(QDialog):
    def __init__(self):
        super().__init__()
        self.func = None
        self.isAdd = False
        self.title = 'Add a Activation Function'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 150
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label1 = QLabel()
        self.label1.setText("Function type:")
        self.cbType = QComboBox()
        self.cbType.addItem("relu")
        self.cbType.addItem("sigmoid")
        self.cbType.addItem("tanh")
        self.cbType.addItem("softmax")
        self.cbType.addItem("softmin")
        self.btnAdd = QPushButton()
        self.btnAdd.setText("Add")
        self.btnAdd.clicked.connect(self.btnAdd_onclick)
        self.btnExit = QPushButton()
        self.btnExit.setText("Exit")
        self.btnExit.clicked.connect(self.btnExit_onclick)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.cbType)
        self.layout.addWidget(self.btnAdd)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
        self.exec_()

    def btnExit_onclick(self):
        self.close()

    def btnAdd_onclick(self):
        self.func = self.cbType.currentText()
        self.isAdd = True
        self.close()


class frmConv(QDialog):
    def __init__(self):
        super().__init__()
        self.isAdd = False

        self.Channel = None
        self.Kernel = None
        self.Bias = None
        self.Stride = None
        self.Groups = None
        self.Padding = None
        self.Dilation = None

        self.title = 'Add a Conv net'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label1 = QLabel()
        self.label1.setText("Out channel size:")
        self.txtChannel = QSpinBox()
        self.txtChannel.setMinimum(1)
        self.txtChannel.setMaximum(100000)
        self.txtChannel.setValue(1)

        self.label2 = QLabel()
        self.label2.setText("Kernel: e.g. 2 or (2, 3, 3)")
        self.txtKernel = QLineEdit()
        self.txtKernel.setText("2")


        self.label3 = QLabel()
        self.label3.setText("Stride:")
        self.txtStride = QSpinBox()
        self.txtStride.setMinimum(1)
        self.txtStride.setMaximum(100000)
        self.txtStride.setValue(1)

        self.label4 = QLabel()
        self.label4.setText("Padding:")
        self.txtPadding = QSpinBox()
        self.txtPadding.setMinimum(0)
        self.txtPadding.setMaximum(100000)
        self.txtPadding.setValue(0)


        self.label5 = QLabel()
        self.label5.setText("Dilation:")
        self.txtDilation = QSpinBox()
        self.txtDilation.setMinimum(1)
        self.txtDilation.setMaximum(100000)
        self.txtDilation.setValue(1)

        self.label6 = QLabel()
        self.label6.setText("Groups:")
        self.txtGroups = QSpinBox()
        self.txtGroups.setMinimum(1)
        self.txtGroups.setMaximum(100000)
        self.txtGroups.setValue(1)


        self.cbBais = QCheckBox()
        self.cbBais.setText("Bias")
        self.cbBais.setChecked(True)

        self.btnAdd = QPushButton()
        self.btnAdd.setText("Add")
        self.btnAdd.clicked.connect(self.btnAdd_onclick)
        self.btnExit = QPushButton()
        self.btnExit.setText("Exit")
        self.btnExit.clicked.connect(self.btnExit_onclick)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.txtChannel)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.txtKernel)
        self.layout.addWidget(self.label3)
        self.layout.addWidget(self.txtStride)
        self.layout.addWidget(self.label4)
        self.layout.addWidget(self.txtPadding)
        self.layout.addWidget(self.label5)
        self.layout.addWidget(self.txtDilation)
        self.layout.addWidget(self.label6)
        self.layout.addWidget(self.txtGroups)
        self.layout.addWidget(self.cbBais)
        self.layout.addWidget(self.btnAdd)
        self.layout.addWidget(self.btnExit)
        self.setLayout(self.layout)
        self.exec_()

    def btnExit_onclick(self):
        self.close()

    def btnAdd_onclick(self):
        self.Bias = self.cbBais.isChecked()
        self.Groups = self.txtGroups.value()
        self.Kernel = self.txtKernel.text()
        self.Stride = self.txtStride.value()
        self.Dilation = self.txtDilation.value()
        self.Padding = self.txtPadding.value()
        self.Channel = self.txtChannel.value()
        self.isAdd = True
        self.close()
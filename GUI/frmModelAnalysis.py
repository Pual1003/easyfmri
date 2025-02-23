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


import sys

from GUI.frmModelAnalysisGUI import *
from Base.tools import Tools


class MainWindow(QtWidgets.QMainWindow):
    parent = None

    def __init__(self, parentin=None):
        super().__init__()
        global parent
        if parentin is not None:
            parent = parentin

    def closeEvent(self, event):
        global parent
        try:
            if parent is not None:
                parent.show()
        except:
            pass

    pass


class frmModelAnalysis(Ui_frmModelAnalysis):
    ui = Ui_frmModelAnalysis()
    dialog = None

    # This function is run when the main form start
    # and initiate the default parameters.
    def show(self, parentin=None):
        from Base.utility import getVersion, getBuild
        global dialog, ui, parent
        ui = Ui_frmModelAnalysis()
        QtWidgets.QApplication.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
        if parentin is not None:
            dialog = MainWindow(parentin)
        else:
            dialog = MainWindow()
        ui.setupUi(dialog)
        self.set_events(self)

        tools = Tools()
        tools.combo(ui.cbTools)


        ui.tabWidget.setCurrentIndex(0)
        # Unsupervised
        ui.cbMAU.addItem("MatLab, PyTorch: Shared Similarity Analysis", 30000)
        ui.cbMAU.addItem("MatLab, SK Clustering: Agglomerative",10002)
        ui.cbMAU.addItem("MatLab, SK Clustering: Birch",10003)
        ui.cbMAU.addItem("MatLab, SK Clustering: Gaussian Mixture",10004)
        ui.cbMAU.addItem("MatLab, SK Clustering: KMeans",10000)
        ui.cbMAU.addItem("MatLab, SK Clustering: Spectral",10001)
        ui.cbMAU.addItem("MatLab, SK RSA: Session Level Representational Similarity Analysis",20007)
        ui.cbMAU.addItem("MatLab, SK RSA: Group Level Representational Similarity Analysis",20008)
        ui.cbMAU.addItem("MatLab, NumPy RSA: Session Level Representational Similarity Analysis",20000)
        ui.cbMAU.addItem("MatLab, NumPy RSA: Group Level Representational Similarity Analysis",20001)
        ui.cbMAU.addItem("MatLab, PyTorch RSA: Session Level Gradient Representational Similarity Analysis",20002)
        ui.cbMAU.addItem("MatLab, PyTorch RSA: Group Level Gradient Representational Similarity Analysis",20003)

        # Supervised
        ui.cbMAS.addItem("MatLab, MVPA, PyTorch: GPU Support Vector Machine",10003)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: AdaBoost",80005)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Decision Tree",80001)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Gaussian Naive Bayes",80000)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Linear Support Vector Machine (liblinear)",10001)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Multi-Layer Perceptron (MLP)",80002)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Nu Support Vector Machine (libsvm)",10002)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Random Forest",80004)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Stochastic Gradient Descent based approaches",80003)
        ui.cbMAS.addItem("MatLab, MVPA, SK Classification: Support Vector Machine (libsvm)",10000)

        dialog.setWindowTitle("easy fMRI model analysis - V" + getVersion() + "B" + getBuild())
        dialog.setWindowFlags(dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        dialog.setWindowFlags(dialog.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        dialog.setFixedSize(dialog.size())
        dialog.show()

    # This function initiate the events procedures
    def set_events(self):
        ui.btnClose.clicked.connect(self.btnClose_click)
        ui.btnMASRun.clicked.connect(self.btnMAS_click)
        ui.btnMAURun.clicked.connect(self.btnMAU_click)
        ui.btnTools.clicked.connect(self.btnTools_click)



    # Exit function
    def btnClose_click(self):
        global dialog, parent
        dialog.close()

    def btnTools_click(self):
        tools = Tools()
        tools.run(ui.cbTools.currentData())


    def btnMAU_click(self):
        MAID = ui.cbMAU.currentData()
        if MAID == 10000:
            from GUI.frmMAKMeans import frmMAKMeans
            frmMAKMeans.show(frmMAKMeans)
            return
        if MAID == 10001:
            from GUI.frmMASpectral import frmMASpectral
            frmMASpectral.show(frmMASpectral)
            return
        if MAID == 10002:
            from GUI.frmMAAgglomerative import frmMAAgglomerative
            frmMAAgglomerative.show(frmMAAgglomerative)
            return
        if MAID == 10003:
            from GUI.frmMABirch import frmMABirch
            frmMABirch.show(frmMABirch)
            return
        if MAID == 10004:
            from GUI.frmMAGaussian import frmMAGaussian
            frmMAGaussian.show(frmMAGaussian)
            return
        if MAID == 20000:
            from GUI.frmMARSA import frmMARSA
            frmMARSA.show(frmMARSA)
            return
        if MAID == 20001:
            from GUI.frmMAGRSA import frmMAGRSA
            frmMAGRSA.show(frmMAGRSA)
            return
        if MAID == 20007:
            from GUI.frmMASKRSA import frmMASKRSA
            frmMASKRSA.show(frmMASKRSA)
            return
        if MAID == 20008:
            from GUI.frmMASKGRSA import frmMASKGRSA
            frmMASKGRSA.show(frmMASKGRSA)
            return
        if MAID == 20002:
            from GUI.frmMAGrRSA import frmMAGrRSA
            frmMAGrRSA.show(frmMAGrRSA)
            return
        if MAID == 20003:
            from GUI.frmMAGGrRSA import frmMAGGrRSA
            frmMAGGrRSA.show(frmMAGGrRSA)
            return
        if MAID == 30000:
            from GUI.frmMASSA import frmMASSA
            frmMASSA.show(frmMASSA)
            return


    def btnMAS_click(self):
        MAID = ui.cbMAS.currentData()
        if MAID == 10000:
            from GUI.frmMASVM import frmMASVM
            frmMASVM.show(frmMASVM)
            return
        if MAID == 10001:
            from GUI.frmMALSVM import frmMALSVM
            frmMALSVM.show(frmMALSVM)
            return
        if MAID == 10002:
            from GUI.frmMANuSVM import frmMANuSVM
            frmMANuSVM.show(frmMANuSVM)
            return
        if MAID == 10003:
            from GUI.frmMAGPUSVM import frmMASVM
            frmMASVM.show(frmMASVM)
            return
        if MAID == 80000:
            from GUI.frmMAGNB import frmMAGNB
            frmMAGNB.show(frmMAGNB)
            return
        if MAID == 80001:
            from GUI.frmMADT import frmMADT
            frmMADT.show(frmMADT)
            return
        if MAID == 80002:
            from GUI.frmMAMLP import frmMAMLP
            frmMAMLP.show(frmMAMLP)
            return
        if MAID == 80003:
            from GUI.frmMASGDC import frmMASGDC
            frmMASGDC.show(frmMASGDC)
            return
        if MAID == 80004:
            from GUI.frmMARFC import frmMARFC
            frmMARFC.show(frmMARFC)
            return
        if MAID == 80005:
            from GUI.frmMAAdaBoost import frmMAAdaBoost
            frmMAAdaBoost.show(frmMAAdaBoost)
            return

# Auto Run
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    frmModelAnalysis.show(frmModelAnalysis)
    sys.exit(app.exec_())

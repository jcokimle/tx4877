import sys

from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QDialog

from about import Ui_Dialog
from mainwindow import Ui_MainWindow
from millerrabin import MillerRabin
from pm1pollard import Pm1Pollard
from primegen import PrimeGen


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.mr = MillerRabin()
        self.pm = Pm1Pollard()
        self.pg = PrimeGen()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.actionA_propos, QtCore.SIGNAL(_fromUtf8("triggered()")), self.open_about)
        QtCore.QObject.connect(self.ui.btn_mr_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_mr)
        QtCore.QObject.connect(self.ui.btn_mr_step, QtCore.SIGNAL(_fromUtf8("clicked()")), self.step_mr)
        QtCore.QObject.connect(self.ui.btn_mr_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reset_mr)
        QtCore.QObject.connect(self.ui.btn_pm_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_pm)
        QtCore.QObject.connect(self.ui.btn_pg_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_pg)

    def open_about(self):
        dial = QDialog()
        self.about = Ui_Dialog()
        self.about.setupUi(dial)
        dial.exec()

    def run_mr(self):
        if not self.mr.step_by_step:
            self.mr.initialize(int(self.ui.txt_mr_n.text()), int(self.ui.txt_mr_k.text()))
        self.mr.run()
        if self.mr.is_prime:
            self.ui.txt_mr_res.setText("Prime")
        else:
            self.ui.txt_mr_res.setText("Not prime")
        self.ui.txt_mr_exec.appendPlainText(self.mr.get_state())

    def step_mr(self):
        if not self.mr.step_by_step:
            self.mr.initialize(int(self.ui.txt_mr_n.text()), int(self.ui.txt_mr_k.text()))
        self.mr.step()
        if self.mr.is_over:
            if self.mr.is_prime:
                self.ui.txt_mr_res.setText("Prime")
            else:
                self.ui.txt_mr_res.setText("Not prime")
        else:
            self.ui.txt_mr_res.setText("")
        self.ui.txt_mr_exec.appendPlainText(self.mr.get_state())

    def reset_mr(self):
        self.ui.txt_mr_exec.setPlainText("")
        self.ui.txt_mr_res.setText("")

    def run_pm(self):
        self.pm.initialize(int(self.ui.txt_pm_n.text()), int(self.ui.txt_pm_b.text()), int(self.ui.txt_pm_it.text()))
        self.pm.run()
        if self.pm.g == 0 or self.pm.g == 1:
            self.ui.txt_pm_res.setText("Factorization failed")
        else:
            self.ui.txt_pm_res.setText("Success: %d" % self.pm.g)

    def run_pg(self):
        self.pg.initialize(int(self.ui.txt_pg_size.text()))
        self.pg.run()
        self.ui.txt_pg_res.setText(str(self.pg.cand))

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

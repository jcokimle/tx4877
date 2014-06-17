import sys

from PyQt4 import QtCore
from PyQt4.QtGui import QApplication, QMainWindow, QDialog

from tx4877.about import Ui_Dialog
from tx4877.mainwindow import Ui_MainWindow
from tx4877.millerrabin import MillerRabin
from tx4877.pm1pollard import Pm1Pollard
from tx4877.primegen import PrimeGen


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        self.mr = MillerRabin()
        self.pm = Pm1Pollard()
        self.pg = PrimeGen()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connecting signals and slots
        QtCore.QObject.connect(self.ui.actionA_propos, QtCore.SIGNAL(_fromUtf8("triggered()")), self.open_about)
        QtCore.QObject.connect(self.ui.btn_mr_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_mr)
        QtCore.QObject.connect(self.ui.btn_mr_step, QtCore.SIGNAL(_fromUtf8("clicked()")), self.step_mr)
        QtCore.QObject.connect(self.ui.btn_mr_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reset_mr)
        QtCore.QObject.connect(self.ui.btn_pm_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_pm)
        QtCore.QObject.connect(self.ui.btn_pm_step, QtCore.SIGNAL(_fromUtf8("clicked()")), self.step_pm)
        QtCore.QObject.connect(self.ui.btn_pm_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reset_pm)
        QtCore.QObject.connect(self.ui.btn_pg_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run_pg)
        QtCore.QObject.connect(self.ui.btn_pg_step, QtCore.SIGNAL(_fromUtf8("clicked()")), self.step_pg)
        QtCore.QObject.connect(self.ui.btn_pg_reset, QtCore.SIGNAL(_fromUtf8("clicked()")), self.reset_pg)

    def open_about(self):
        dial = QDialog()
        self.about = Ui_Dialog()
        self.about.setupUi(dial)
        dial.exec()

    ''' Miller Rabin '''
    def run_mr(self):
        if not self.mr.step_by_step:
            self.reset_mr()
            self.mr.initialize(int(self.ui.txt_mr_n.text()), int(self.ui.txt_mr_k.text()))
        self.mr.run()
        self.add_log_mr(self.mr.log_msg)
        if self.mr.is_prime:
            self.ui.txt_mr_res.setText("Prime")
        else:
            self.ui.txt_mr_res.setText("Composite")

    def step_mr(self):
        if not self.mr.step_by_step:
            self.reset_mr()
            self.mr.initialize(int(self.ui.txt_mr_n.text()), int(self.ui.txt_mr_k.text()))
        self.mr.step()
        self.add_log_mr(self.mr.log_msg)
        if self.mr.is_over:
            if self.mr.is_prime:
                self.ui.txt_mr_res.setText("Prime")
            else:
                self.ui.txt_mr_res.setText("Composite")
        else:
            self.ui.txt_mr_res.setText("")

    def reset_mr(self):
        self.ui.txt_mr_exec.setPlainText("")
        self.ui.txt_mr_res.setText("")
        self.mr.step_by_step = False

    ''' Pm1 Pollard '''
    def run_pm(self):
        if not self.pm.step_by_step:
            self.reset_pm()
            self.pm.initialize(int(self.ui.txt_pm_n.text()), int(self.ui.txt_pm_b.text()), int(self.ui.txt_pm_it.text()))
        self.pm.run()
        self.add_log_pm(self.pm.log_msg)
        if self.pm.g == 0 or self.pm.g == 1:
            self.ui.txt_pm_res.setText("Factorization failed")
        else:
            self.ui.txt_pm_res.setText("Success: %d" % self.pm.g)

    def step_pm(self):
        if not self.pm.step_by_step:
            self.reset_pm()
            self.pm.initialize(int(self.ui.txt_pm_n.text()), int(self.ui.txt_pm_b.text()), int(self.ui.txt_pm_it.text()))
        self.pm.step()
        self.add_log_pm(self.pm.log_msg)
        if self.pm.is_over:
            if self.pm.g == 0 or self.pm.g == 1:
                self.ui.txt_pm_res.setText("Factorization failed")
            else:
                self.ui.txt_pm_res.setText("Success: %d" % self.pm.g)
        else:
            self.ui.txt_pm_res.setText("")

    def reset_pm(self):
        self.ui.txt_pm_exec.setPlainText("")
        self.ui.txt_pm_res.setText("")
        self.pm.step_by_step = False

    ''' Prime Gen '''
    def run_pg(self):
        if not self.pg.step_by_step:
            self.reset_pg()
            self.pg.initialize(int(self.ui.txt_pg_size.text()))
        self.pg.run()
        self.add_log_pg(self.pg.log_msg)
        self.ui.txt_pg_res.setText(str(self.pg.cand))

    def step_pg(self):
        if not self.pg.step_by_step:
            self.reset_pg()
            self.pg.initialize(int(self.ui.txt_pg_size.text()))
        self.pg.step()
        self.add_log_pg(self.pg.log_msg)
        if self.pg.is_over:
            self.ui.txt_pg_res.setText(str(self.pg.cand))
        else:
            self.ui.txt_pg_res.setText("")

    def reset_pg(self):
        self.ui.txt_pg_exec.setPlainText("")
        self.ui.txt_pg_res.setText("")
        self.pg.step_by_step = False

    def add_log_mr(self, log):
        self._add_log(log, self.ui.txt_mr_exec)

    def add_log_pm(self, log):
        self._add_log(log, self.ui.txt_pm_exec)

    def add_log_pg(self, log):
        self._add_log(log, self.ui.txt_pg_exec)

    def _add_log(self, log, txt_wdgt):
        txt_wdgt.setPlainText(log)
        txt_wdgt.verticalScrollBar().setSliderPosition(txt_wdgt.verticalScrollBar().maximum())

if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

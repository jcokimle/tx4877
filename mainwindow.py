# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Jun  2 14:06:34 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(570, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(570, 500))
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(570, 459))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(530, 440))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMinimumSize(QtCore.QSize(524, 414))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.txt_mr_n = QtGui.QLineEdit(self.tab)
        self.txt_mr_n.setObjectName(_fromUtf8("txt_mr_n"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_mr_n)
        self.label_2 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.txt_mr_k = QtGui.QLineEdit(self.tab)
        self.txt_mr_k.setObjectName(_fromUtf8("txt_mr_k"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txt_mr_k)
        self.label_3 = QtGui.QLabel(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txt_mr_res = QtGui.QLineEdit(self.tab)
        self.txt_mr_res.setReadOnly(True)
        self.txt_mr_res.setObjectName(_fromUtf8("txt_mr_res"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txt_mr_res)
        spacerItem = QtGui.QSpacerItem(75, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtGui.QFormLayout.LabelRole, spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_mr_run = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mr_run.sizePolicy().hasHeightForWidth())
        self.btn_mr_run.setSizePolicy(sizePolicy)
        self.btn_mr_run.setObjectName(_fromUtf8("btn_mr_run"))
        self.horizontalLayout.addWidget(self.btn_mr_run)
        self.btn_mr_step = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mr_step.sizePolicy().hasHeightForWidth())
        self.btn_mr_step.setSizePolicy(sizePolicy)
        self.btn_mr_step.setObjectName(_fromUtf8("btn_mr_step"))
        self.horizontalLayout.addWidget(self.btn_mr_step)
        self.btn_mr_reset = QtGui.QPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mr_reset.sizePolicy().hasHeightForWidth())
        self.btn_mr_reset.setSizePolicy(sizePolicy)
        self.btn_mr_reset.setObjectName(_fromUtf8("btn_mr_reset"))
        self.horizontalLayout.addWidget(self.btn_mr_reset)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.txt_mr_exec = QtGui.QPlainTextEdit(self.tab)
        self.txt_mr_exec.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txt_mr_exec.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.txt_mr_exec.setObjectName(_fromUtf8("txt_mr_exec"))
        self.verticalLayout_2.addWidget(self.txt_mr_exec)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_2.sizePolicy().hasHeightForWidth())
        self.tab_2.setSizePolicy(sizePolicy)
        self.tab_2.setMinimumSize(QtCore.QSize(524, 414))
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txt_pm_n = QtGui.QLineEdit(self.tab_2)
        self.txt_pm_n.setObjectName(_fromUtf8("txt_pm_n"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_pm_n)
        self.label_5 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txt_pm_b = QtGui.QLineEdit(self.tab_2)
        self.txt_pm_b.setObjectName(_fromUtf8("txt_pm_b"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.txt_pm_b)
        self.label_6 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_6)
        self.txt_pm_it = QtGui.QLineEdit(self.tab_2)
        self.txt_pm_it.setObjectName(_fromUtf8("txt_pm_it"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.txt_pm_it)
        self.label_9 = QtGui.QLabel(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_9)
        self.txt_pm_res = QtGui.QLineEdit(self.tab_2)
        self.txt_pm_res.setReadOnly(True)
        self.txt_pm_res.setObjectName(_fromUtf8("txt_pm_res"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.txt_pm_res)
        spacerItem1 = QtGui.QSpacerItem(75, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_2.setItem(4, QtGui.QFormLayout.LabelRole, spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btn_pm_run = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pm_run.sizePolicy().hasHeightForWidth())
        self.btn_pm_run.setSizePolicy(sizePolicy)
        self.btn_pm_run.setObjectName(_fromUtf8("btn_pm_run"))
        self.horizontalLayout_3.addWidget(self.btn_pm_run)
        self.btn_pm_step = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pm_step.sizePolicy().hasHeightForWidth())
        self.btn_pm_step.setSizePolicy(sizePolicy)
        self.btn_pm_step.setObjectName(_fromUtf8("btn_pm_step"))
        self.horizontalLayout_3.addWidget(self.btn_pm_step)
        self.btn_pm_reset = QtGui.QPushButton(self.tab_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pm_reset.sizePolicy().hasHeightForWidth())
        self.btn_pm_reset.setSizePolicy(sizePolicy)
        self.btn_pm_reset.setObjectName(_fromUtf8("btn_pm_reset"))
        self.horizontalLayout_3.addWidget(self.btn_pm_reset)
        self.formLayout_2.setLayout(4, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.txt_pm_exec = QtGui.QPlainTextEdit(self.tab_2)
        self.txt_pm_exec.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txt_pm_exec.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.txt_pm_exec.setObjectName(_fromUtf8("txt_pm_exec"))
        self.verticalLayout.addWidget(self.txt_pm_exec)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_3.sizePolicy().hasHeightForWidth())
        self.tab_3.setSizePolicy(sizePolicy)
        self.tab_3.setMinimumSize(QtCore.QSize(524, 414))
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_3)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_7 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txt_pg_size = QtGui.QLineEdit(self.tab_3)
        self.txt_pg_size.setObjectName(_fromUtf8("txt_pg_size"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_pg_size)
        self.label_8 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_8)
        self.txt_pg_res = QtGui.QLineEdit(self.tab_3)
        self.txt_pg_res.setReadOnly(True)
        self.txt_pg_res.setObjectName(_fromUtf8("txt_pg_res"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.txt_pg_res)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.btn_pg_run = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pg_run.sizePolicy().hasHeightForWidth())
        self.btn_pg_run.setSizePolicy(sizePolicy)
        self.btn_pg_run.setObjectName(_fromUtf8("btn_pg_run"))
        self.horizontalLayout_5.addWidget(self.btn_pg_run)
        self.btn_pg_step = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pg_step.sizePolicy().hasHeightForWidth())
        self.btn_pg_step.setSizePolicy(sizePolicy)
        self.btn_pg_step.setObjectName(_fromUtf8("btn_pg_step"))
        self.horizontalLayout_5.addWidget(self.btn_pg_step)
        self.btn_pg_reset = QtGui.QPushButton(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pg_reset.sizePolicy().hasHeightForWidth())
        self.btn_pg_reset.setSizePolicy(sizePolicy)
        self.btn_pg_reset.setObjectName(_fromUtf8("btn_pg_reset"))
        self.horizontalLayout_5.addWidget(self.btn_pg_reset)
        self.formLayout_3.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        spacerItem2 = QtGui.QSpacerItem(75, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_3.setItem(2, QtGui.QFormLayout.LabelRole, spacerItem2)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.txt_pg_exec = QtGui.QPlainTextEdit(self.tab_3)
        self.txt_pg_exec.setLineWrapMode(QtGui.QPlainTextEdit.NoWrap)
        self.txt_pg_exec.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.txt_pg_exec.setObjectName(_fromUtf8("txt_pg_exec"))
        self.verticalLayout_3.addWidget(self.txt_pg_exec)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.horizontalLayout_6.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionA_propos = QtGui.QAction(MainWindow)
        self.actionA_propos.setObjectName(_fromUtf8("actionA_propos"))
        self.menuFichier.addAction(self.actionQuitter)
        self.menu.addAction(self.actionA_propos)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuitter, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "CryptAlgos", None))
        self.label.setText(_translate("MainWindow", "N", None))
        self.txt_mr_n.setText(_translate("MainWindow", "0", None))
        self.label_2.setText(_translate("MainWindow", "K", None))
        self.txt_mr_k.setText(_translate("MainWindow", "10", None))
        self.label_3.setText(_translate("MainWindow", "Result", None))
        self.btn_mr_run.setText(_translate("MainWindow", "Run", None))
        self.btn_mr_step.setText(_translate("MainWindow", "Step", None))
        self.btn_mr_reset.setText(_translate("MainWindow", "Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Miller Rabin", None))
        self.label_4.setText(_translate("MainWindow", "N", None))
        self.txt_pm_n.setText(_translate("MainWindow", "1", None))
        self.label_5.setText(_translate("MainWindow", "B", None))
        self.txt_pm_b.setText(_translate("MainWindow", "0", None))
        self.label_6.setText(_translate("MainWindow", "It", None))
        self.txt_pm_it.setText(_translate("MainWindow", "10", None))
        self.label_9.setText(_translate("MainWindow", "Result", None))
        self.btn_pm_run.setText(_translate("MainWindow", "Run", None))
        self.btn_pm_step.setText(_translate("MainWindow", "Step", None))
        self.btn_pm_reset.setText(_translate("MainWindow", "Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Pm1 Pollard", None))
        self.label_7.setText(_translate("MainWindow", "Size", None))
        self.txt_pg_size.setText(_translate("MainWindow", "1", None))
        self.label_8.setText(_translate("MainWindow", "Result", None))
        self.btn_pg_run.setText(_translate("MainWindow", "Run", None))
        self.btn_pg_step.setText(_translate("MainWindow", "Step", None))
        self.btn_pg_reset.setText(_translate("MainWindow", "Reset", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Prime Gen", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menu.setTitle(_translate("MainWindow", "Aide", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
        self.actionA_propos.setText(_translate("MainWindow", "A propos", None))


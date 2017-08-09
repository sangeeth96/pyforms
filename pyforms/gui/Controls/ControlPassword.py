#!/usr/bin/python
# -*- coding: utf-8 -*-

from pyforms.gui.Controls.ControlText import ControlText

from pysettings import conf

if conf.PYFORMS_USE_QT5:
	from PyQt5.QtWidgets import QLineEdit
else:
	from PyQt4.QtGui import QLineEdit

class ControlPassword(ControlText):
    def init_form(self):
        super(ControlPassword, self).init_form()
        
        self.form.label.setAccessibleName('ControlPassword-label')
        self.form.lineEdit.setEchoMode(QLineEdit.Password)
# -*- coding: utf-8 -*-
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from PyQt5 import QtGui, QtWidgets , QtCore
from PyQt5.QtWidgets import QWidget , QTextEdit , QVBoxLayout , QHBoxLayout ,QPushButton , QLabel
from PyQt5.QtGui import QIcon
import ast , os
from newopen import Open
import icons_resource
import osCommands

home_address = os.path.expanduser("~")
config_folder = str(home_address) + "/.config/persepolis_download_manager"

#setting
setting_file = config_folder + '/setting'
f = Open(setting_file)
setting_file_lines = f.readlines()
f.close()
setting_dict_str = str(setting_file_lines[0].strip())
setting_dict = ast.literal_eval(setting_dict_str) 

icons = ':/' + str(setting_dict['icons']) + '/'


class ErrorWindow(QWidget):
    def __init__(self , text):
        super().__init__()
#finding windows_size
        self.setMinimumSize(QtCore.QSize(363, 300))
        self.setWindowIcon(QIcon.fromTheme('persepolis',QIcon(':/icon.svg')))
        self.setWindowTitle('Persepolis Download Manager')
 
        verticalLayout = QVBoxLayout(self)
        horizontalLayout = QHBoxLayout()
        horizontalLayout.addStretch(1)

        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)
        self.text_edit.insertPlainText(text)

        verticalLayout.addWidget(self.text_edit)

        self.label = QLabel(self)
        self.label.setText('<b>Persepolis Reset!Restart persepolis.</b>')
        verticalLayout.addWidget(self.label)
        
        self.label2 = QLabel(self)
        self.label2.setText('Please copy this error message and press "Report Issue" button\nand open a new issue in Github for it.\nWe answer you as soon as possible. \nreporting this issue help us to improve persepolis.\nThank you!')
        verticalLayout.addWidget(self.label2)

        self.report_pushButton = QPushButton(self)
        self.report_pushButton.setText("Report Issue")
        horizontalLayout.addWidget(self.report_pushButton)

        self.close_pushButton = QPushButton(self)
        self.close_pushButton.setText('close')
        horizontalLayout.addWidget(self.close_pushButton)

        verticalLayout.addLayout(horizontalLayout)

        self.report_pushButton.clicked.connect(self.reportPushButtonPressed)
        self.close_pushButton.clicked.connect(self.closePushButtonPressed)

    def reportPushButtonPressed(self,button):
        osCommands.xdgOpen('https://github.com/persepolisdm/persepolis/issues')

    def closePushButtonPressed(self,button):
        self.close()


        
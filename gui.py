""" 
The GUI must add the ability to load social media and email accounts directly from within PyppetMaster.  This is just a sketch of what is required.
"""

import sys
import os
import time
import random
import string
import re
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QTextEdit, QGridLayout, QMessageBox, QFileDialog, QComboBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Sock Puppets'
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 640
        self.initUI()

    def initUI(self):


        grid_layout = QGridLayout()

        title_label = QLabel('Sock Puppets')


        title_label_font = title_label.font()
        title_label_font.setPointSize(20)
        title_label_font.setBold(True)


        title_label.setFont(title_label_font)

        grid_layout.addWidget(title_label, 0, 0, 3, 1)

        persona_name_label = QLabel('Persona Name:')

        grid_layout.addWidget(persona_name_label, 3, 0)
       
        self.persona_name_text_field = QLineEdit()

        grid_layout.addWidget(self.persona_name_text_field, 3, 1, 1, 2)

        persona_email_label = QLabel('Persona Email:')

        grid_layout.addWidget(persona_email_label, 4, 0)
       
        self.persona_email_text_field = QLineEdit()

        grid_layout.addWidget(self.persona_email_text_field, 4, 1, 1, 2)

        persona_phone_number_label = QLabel('Persona Phone Number:')

        grid_layout.addWidget(persona_phone_number_label, 5, 0)
     
        self.persona_phone_number_text_field = QLineEdit()

        grid_layout.addWidget(self.persona_phone_number_text_field, 5, 1, 1, 2)

        persona_social_network_accounts = QLabel('Persona Social Network Accounts:')

        grid_layout.addWidget(persona_social_network_accounts, 6, 0)
       
        self.persona_social_network_accounts = QTextEdit()
       
        self.persona_social_network_accounts.setFixedHeight(50)

        grid_layout.addWidget(self.persona_social_network_accounts, 7, 0)
       
        self.persona_combo_box = QComboBox()

        grid_layout.addWidget(self.persona_combo_box, 10, 0)

        new_button = QPushButton('New')

        grid_layout.addWidget(new_button, 11, 0)

        save_button = QPushButton('Save')

        grid_layout.addWidget(save_button, 11, 1)

        edit_button = QPushButton('Edit')

        grid_layout.addWidget(edit_button, 11, 2)

        delete_button = QPushButton('Delete')

        grid_layout.addWidget(delete_button, 12, 0)
       
        self.persona_combo_box = QComboBox()

        grid_layout.addWidget(self.persona_combo_box, 10, 0)
       
        search_button = QPushButton('Search')

        grid_layout.addWidget(search_button, 13, 0)
       
        import_button = QPushButton('Import')

        grid_layout.addWidget(import_button, 14, 0)

        export_button = QPushButton('Export')

        grid_layout.addWidget(export_button, 15, 0)

        self.persona_combo_box = QComboBox()

        grid_layout.addWidget(self.persona_combo_box, 10, 0)

        signup_button = QPushButton('Sign Up')

        grid_layout.addWidget(signup_button, 16, 0)

        self.setLayout(grid_layout)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        new_button.clicked.connect(self.new_button_clicked)
        save_button.clicked.connect(self.save_button_clicked)
        edit_button.clicked.connect(self.edit_button_clicked)
        delete_button.clicked.connect(self.delete_button_clicked)
        search_button.clicked.connect(self.search_button_clicked)
        import_button.clicked.connect(self.import_button_clicked)
        export_button.clicked.connect(self.export_button_clicked)
        signup_button.clicked.connect(self.signup_button_clicked)

        self.show()
###remove print() code below

    @pyqtSlot()
    def new_button_clicked(self):
        print('New button clicked')

    @pyqtSlot()
    def save_button_clicked(self):
        print('Save button clicked')

    @pyqtSlot()
    def edit_button_clicked(self):
        print('Edit button clicked')

    @pyqtSlot()
    def delete_button_clicked(self):
        print('Delete button clicked')

    @pyqtSlot()
    def search_button_clicked(self):
        print('Search button clicked')

    @pyqtSlot()
    def import_button_clicked(self):
        print('Import button clicked')

    @pyqtSlot()
    def export_button_clicked(self):
        print('Export button clicked')

    @pyqtSlot()
    def signup_button_clicked(self):
        print('Sign Up button clicked')

       
if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = App()
     sys.exit(app.exec_())

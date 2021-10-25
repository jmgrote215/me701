#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a quit
button. When we press the button,
the application terminates. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: January 2018
"""

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QRadioButton, QHBoxLayout

class Example(QWidget): #Example inherits from Widget. Example is a Widget
    
    def __init__(self):
        super().__init__() #super is the base class you know
        
        self.initUI() #sequence of things that are defined.
        
        
    def initUI(self):               
        
        qbtn = QPushButton('Quit', self) 
        led=QRadioButton('light',self)

        layout = QHBoxLayout()

        layout.addWidget(qbtn)
        layout.addWidget(led)

        self.setLayout(layout)

        #qbtn.pressed.connect(led)

        """"made a button, and a layout of a 1x2 layout"""

        qbtn.clicked.connect(QApplication.instance().quit) 
        """
        #this is the main interaction. quit is a fxn. telling ("callback fxn") the
        #connect or whatever to call quit. pass a fuxn as an argument. clicked is the signal attached to the slot. "s&s is just callback fxns"
        qapp is a class that is most likely a singleton (only 1 object of this class can be produced. instance is called and 
        returns the 1 object-represent the entire gui. has an object called quit. )
        
        """
        
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show() #must be present. here it is hidden inside the construction of the class. can be in if__name__
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example() 
    sys.exit(app.exec_())


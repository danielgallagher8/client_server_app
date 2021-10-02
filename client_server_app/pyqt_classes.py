# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:13:03 2021

@author: danie
"""

#Import libraries
import sys
from socket_classes import Send, Receive
from PyQt5.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QAction
        )

#Define classes
class App(QMainWindow):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Test App')
        self.resize(800, 400)
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout()
        self.centralWidget.setLayout(self.layout)
    
class Window(App):
    
    def __init__(self, host, port):
        super().__init__()
        self.display()
        self.send = Send(host, port)
    
    def menu(self):
        menu_bar = self.menuBar()
        main_menu = menu_bar.addMenu("&Finances")
        main_menu.addAction(self.binance_action)
        main_menu.addAction(self.barclays_action)
        main_menu.addAction(self.monzo_action)
    
    def menu_actions(self):
        self.binance_action = QAction("&Binance", self)
        self.barclays_action = QAction("&Barclays", self)
        self.monzo_action = QAction("&Monzo", self)
    
    def display(self):
        self.menu_actions()
        self.menu()
        self.submit_button = QPushButton('Click', self)
        self.layout.addWidget(self.submit_button)
    
    def closeEvent(self, event):
        self.send.send_data('Closing app')

class RunApp:
    
    def __init__(self, host, port):
        self.send = Send(host, port)
        self.app = QApplication(sys.argv)
        self.window = Window(host, port)
    
    def window_button(self):
        self.send.send_data('Clicked "Click Button"')
    
    def window_binance(self):
        self.send.send_data('Clicked "Binance"')
    
    def window_barclays(self):
        self.send.send_data('Clicked "Barclays"')
    
    def window_monzo(self):
        self.send.send_data('Clicked "Monzo"')
    
    def window_actions(self):
        self.window.submit_button.clicked.connect(self.window_button)
        self.window.binance_action.triggered.connect(self.window_binance)
        self.window.barclays_action.triggered.connect(self.window_barclays)
        self.window.monzo_action.triggered.connect(self.window_monzo)
    
    def actions(self):
        self.window_actions()
    
    def run(self):
        self.actions()
        self.window.show()
        sys.exit(self.app.exec_())
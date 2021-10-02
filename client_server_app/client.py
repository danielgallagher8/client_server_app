# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 23:16:40 2021

@author: danie
"""

import sys
import socket
from datetime import datetime
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton, QApplication

"""
def log(logs):
    now = datetime.now().strftime("%H:%M:%S")
    print("{} || {}".format(now, logs))
"""

class Client:
    
    def __init__(self, host="127.0.0.1", port=65432):
        self.host = host
        self.port = port
        
    """
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            data = None
            while data != b'close':
                input_data = str.encode(input())
                s.sendall(input_data)
                data = s.recv(1024)
        print('Received:', repr(data))
    """
    
    def send_data(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            data = str.encode(data)
            s.sendall(data)

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
    
    def __init__(self):
        super().__init__()
        self.display()
    
    def display(self):
        self.submit_button = QPushButton('Click', self)
        self.layout.addWidget(self.submit_button)

class RunApp:
    
    def __init__(self):
        self.client = Client()
        self.app = QApplication(sys.argv)
        self.window = Window()
    
    def client_send(self):
        self.client.send_data('Clicked')
    
    def window_actions(self):
        self.window.submit_button.clicked.connect(self.client_send)
    
    def actions(self):
        self.window_actions()
    
    def run(self):
        self.actions()
        self.window.show()
        sys.exit(self.app.exec_())
    
if __name__ == '__main__':
    r = RunApp()
    r.run()
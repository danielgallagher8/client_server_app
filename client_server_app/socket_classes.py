# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 19:11:27 2021

@author: danie
"""

#Import libraries
import socket
from logging import log

#Define classes
class Send:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def send_data(self, data):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            data = str.encode(data)
            s.sendall(data)

class Receive:
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def receive_data(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            log('Starting...')
            while True:
                s.listen()
                conn, addr = s.accept()
                data = conn.recv(1024)
                data = data.decode("utf-8")
                log(data)
        